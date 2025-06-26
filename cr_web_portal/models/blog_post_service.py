# -*- coding: utf-8 -*-
import logging
import pdb

from odoo import api, fields, models, tools, SUPERUSER_ID, _
from odoo.addons.http_routing.models.ir_http import unslug, slug
from odoo.osv import expression


class BlogPostService(models.Model):
    _name = 'blog.post.service'
    _description = 'Blog Post Service'

    name = fields.Char(string='Name')

class BlogPost(models.Model):
    _inherit = 'blog.post'

    service_id = fields.Many2one('blog.post.service',string="Service")
    blog_box_image = fields.Binary(string="Blog Box Image")
    blog_box_image_filename = fields.Char(string="Blog Box Image File Name")
    # blog_box_image_url = fields.Char(compute="_compute_blog_box_image_url",store=True)

    def _get_box_image(self,id):
        if self.blog_box_image:
            return "url('/web/image/blog.post/"+str(id)+"/blog_box_image')"
        else:
            return ''

    @api.model
    def _search_get_detail(self, website, order, options):
        with_description = options['displayDescription']
        with_date = options['displayDetail']
        blog = options.get('blog')
        tags = options.get('tag')
        date_begin = options.get('date_begin')
        date_end = options.get('date_end')
        state = options.get('state')
        domain = [website.website_domain()]
        if blog:
            if not isinstance(blog, list):
                active_blog_ids = blog and [unslug(b)[1] for b in blog.split(',')] or []
                blog = active_blog_ids
            domain.append([('blog_id.id', 'in',blog)])
        if tags:
            domain.append([('tag_ids', 'in', tags)])
        if date_begin and date_end:
            domain.append([("post_date", ">=", date_begin), ("post_date", "<=", date_end)])
        if self.env.user.has_group('website.group_website_designer'):
            if state == "published":
                domain.append([("website_published", "=", True), ("post_date", "<=", fields.Datetime.now())])
            elif state == "unpublished":
                domain.append(['|', ("website_published", "=", False), ("post_date", ">", fields.Datetime.now())])
        else:
            domain.append([("post_date", "<=", fields.Datetime.now())])
        search_fields = ['name', 'author_name']

        def search_in_tags(env, search_term):
            tags_like_search = env['blog.tag'].search([('name', 'ilike', search_term)])
            return [('tag_ids', 'in', tags_like_search.ids)]

        fetch_fields = ['name', 'website_url']
        mapping = {
            'name': {'name': 'name', 'type': 'text', 'match': True},
            'website_url': {'name': 'website_url', 'type': 'text', 'truncate': False},
        }
        if with_description:
            search_fields.append('content')
            fetch_fields.append('content')
            mapping['description'] = {'name': 'content', 'type': 'text', 'html': True, 'match': True}
        if with_date:
            fetch_fields.append('published_date')
            mapping['detail'] = {'name': 'published_date', 'type': 'date'}
        return {
            'model': 'blog.post',
            'base_domain': domain,
            'search_fields': search_fields,
            'search_extra': search_in_tags,
            'fetch_fields': fetch_fields,
            'mapping': mapping,
            'icon': 'fa-rss',
        }