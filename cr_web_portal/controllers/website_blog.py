

from odoo.addons.website_blog.controllers.main import WebsiteBlog

from odoo import http
from odoo.addons.http_routing.models.ir_http import unslug, slug
from odoo.http import request
from odoo import _, api, fields, models
from odoo import tools
import werkzeug
import re
from odoo.addons.website.controllers.main import QueryURL


class MechpowerWebsiteBlog(WebsiteBlog):

    def _prepare_blog_values(self, blogs, blog=False, date_begin=False, date_end=False, tags=False, state=False,page=False, search=None):
        BlogPost = request.env['blog.post']
        BlogTag = request.env['blog.tag']

        # prepare domain
        domain = request.website.website_domain()
        active_blog_ids = blog
        if active_blog_ids:
            domain += [('blog_id.id', 'in',active_blog_ids)]

        if date_begin and date_end:
            domain += [("post_date", ">=", date_begin), ("post_date", "<=", date_end)]
        active_tag_ids = tags and [unslug(tag)[1] for tag in tags.split(',')] or []
        active_tags = BlogTag
        if active_tag_ids:
            active_tags = BlogTag.browse(active_tag_ids).exists()
            fixed_tag_slug = ",".join(slug(t) for t in active_tags)
            if fixed_tag_slug != tags:
                path = request.httprequest.full_path
                new_url = path.replace("/tag/%s" % tags, fixed_tag_slug and "/tag/%s" % fixed_tag_slug or "", 1)
                if new_url != path:  # check that really replaced and avoid loop
                    return request.redirect(new_url, 301)
            domain += [('tag_ids', 'in', active_tags.ids)]

        if request.env.user.has_group('website.group_website_designer'):
            count_domain = domain + [("website_published", "=", True), ("post_date", "<=", fields.Datetime.now())]
            published_count = BlogPost.search_count(count_domain)
            unpublished_count = BlogPost.search_count(domain) - published_count

            if state == "published":
                domain += [("website_published", "=", True), ("post_date", "<=", fields.Datetime.now())]
            elif state == "unpublished":
                domain += ['|', ("website_published", "=", False), ("post_date", ">", fields.Datetime.now())]
        else:
            domain += [("post_date", "<=", fields.Datetime.now())]

        use_cover = request.website.is_view_active('website_blog.opt_blog_cover_post')
        fullwidth_cover = request.website.is_view_active('website_blog.opt_blog_cover_post_fullwidth_design')

        # if blog, we show blog title, if use_cover and not fullwidth_cover we need pager + latest always
        offset = (page - 1) * self._blog_post_per_page
        # if not blog and use_cover and not fullwidth_cover and not tags and not date_begin and not date_end and not search:
        #     offset += 1

        options = {
            'displayDescription': True,
            'displayDetail': False,
            'displayExtraDetail': False,
            'displayExtraLink': False,
            'displayImage': False,
            'allowFuzzy': not request.params.get('noFuzzy'),
            'blog': active_blog_ids if active_blog_ids else [],
            'tag': active_tags.ids,
            'date_begin': date_begin,
            'date_end': date_end,
            'state': state,
        }
        total, details, fuzzy_search_term = request.website._search_with_fuzzy("blog_posts_only", search,limit=page * self._blog_post_per_page,order="is_published desc, post_date desc, id asc",options=options)
        posts = details[0].get('results', BlogPost)
        first_post = BlogPost
        # TODO adapt next line in master.
        if posts and not active_blog_ids and posts[0].website_published and not search:
            first_post = posts[0]
        posts = posts[offset:offset + self._blog_post_per_page]

        url_args = dict()
        if search:
            url_args["search"] = search

        if date_begin and date_end:
            url_args["date_begin"] = date_begin
            url_args["date_end"] = date_end

        pager = tools.lazy(lambda: request.website.pager(
            url=request.httprequest.path.partition('/page/')[0],
            total=total,
            page=page,
            step=self._blog_post_per_page,
            url_args=url_args,
        ))

        if not blogs:
            all_tags = request.env['blog.tag']
        else:
            all_tags = tools.lazy(lambda: blogs.all_tags(join=True) if not active_blog_ids else blogs.all_tags().get(active_blog_ids[0],request.env['blog.tag']))
        tag_category = tools.lazy(lambda: sorted(all_tags.mapped('category_id'), key=lambda category: category.name.upper()))
        other_tags = tools.lazy(lambda: sorted(all_tags.filtered(lambda x: not x.category_id), key=lambda tag: tag.name.upper()))
        nav_list = tools.lazy(self.nav_list)
        # for performance prefetch the first post with the others
        post_ids = (first_post | posts).ids
        # and avoid accessing related blogs one by one
        posts.blog_id

        return {
            'date_begin': date_begin,
            'date_end': date_end,
            'first_post': first_post.with_prefetch(post_ids),
            'other_tags': other_tags,
            'tag_category': tag_category,
            'nav_list': nav_list,
            'tags_list': self.tags_list,
            'pager': pager,
            'posts': posts.with_prefetch(post_ids),
            'tag': tags,
            'active_tag_ids': active_tags.ids,
            'active_blog_ids': active_blog_ids,
            'domain': domain,
            'state_info': state and {"state": state, "published": published_count, "unpublished": unpublished_count},
            'blogs': blogs,
            'blog': blog,
            'search': fuzzy_search_term or search,
            'search_count': total,
            'original_search': fuzzy_search_term and search,
        }

    @http.route([
        '/blog',
        '/blog/page/<int:page>',
        '/blog/tag/<string:tag>',
        '/blog/tag/<string:tag>/page/<int:page>',
        '/blog/<string:blog>',
        '/blog/<string:blog>/page/<int:page>',
        '/blog/<string:blog>/tag/<string:tag>',
        '/blog/<string:blog>/tag/<string:tag>/page/<int:page>',
    ], type='http', auth="public", website=True, sitemap=True)
    def blog(self, blog=None, tag=None, page=1, search=None, **opt):
        Blog = request.env['blog.blog']

        active_blog_ids = blog and [unslug(b)[1] for b in blog.split(',')] or []

        if active_blog_ids and isinstance(active_blog_ids, list):
            blog = Blog.browse(active_blog_ids)
            if not blog.exists():
                raise werkzeug.exceptions.NotFound()

        blogs = tools.lazy(lambda: Blog.search(request.website.website_domain(), order="create_date asc, id asc"))

        if not blog and len(blogs) == 1:
            url = QueryURL('/blog/%s' % slug(blogs[0]), search=search, **opt)()
            return request.redirect(url, code=302)

        date_begin, date_end, state = opt.get('date_begin'), opt.get('date_end'), opt.get('state')

        values = self._prepare_blog_values(blogs=blogs, blog=active_blog_ids, date_begin=date_begin, date_end=date_end, tags=tag, state=state, page=page, search=search)

        # if
        # in case of a redirection need by `_prepare_blog_values` we follow it
        if isinstance(values, werkzeug.wrappers.Response):
            return values
        if blog:
            values['main_object'] = blog[0]
            values['blog'] = blog[0]
            values['blog_url'] = QueryURL('', ['blog', 'tag'], blog=blog[0], tag=tag, date_begin=date_begin, date_end=date_end, search=search)
        else:
            values['blog_url'] = QueryURL('/blog', ['tag'], date_begin=date_begin, date_end=date_end, search=search)

        return request.render("website_blog.blog_post_short", values)
