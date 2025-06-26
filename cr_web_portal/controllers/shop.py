# -*- coding: utf-8 -*-


import json
import logging
from datetime import datetime
from werkzeug.exceptions import Forbidden, NotFound
from werkzeug.urls import url_decode, url_encode, url_parse
from odoo.http import request
from odoo import fields, http, SUPERUSER_ID, tools, _
from odoo.addons.http_routing.models.ir_http import slug
from odoo.addons.website.controllers.main import QueryURL
from odoo.tools import lazy
import itertools

_logger = logging.getLogger(__name__)
from odoo.tools.json import scriptsafe as json_scriptsafe
from odoo.addons.website_sale.controllers.main import WebsiteSale
from odoo.addons.website_sale.controllers.main import TableCompute
import re
from textwrap import shorten
from odoo.tools import OrderedSet, escape_psql, html_escape as escape
from odoo.addons.website.controllers.main import Website
logger = logging.getLogger(__name__)

# override this method for exact search functionality
@http.route('/website/snippet/autocomplete', type='json', auth='public', website=True)
def autocomplete(self, search_type=None, term=None, order=None, limit=5, max_nb_chars=999, options=None):
    """
    Returns list of results according to the term and options

    :param str search_type: indicates what to search within, 'all' matches all available types
    :param str term: search term written by the user
    :param str order:
    :param int limit: number of results to consider, defaults to 5
    :param int max_nb_chars: max number of characters for text fields
    :param dict options: options map containing
        allowFuzzy: enables the fuzzy matching when truthy
        fuzzy (boolean): True when called after finding a name through fuzzy matching

    :returns: dict (or False if no result) containing
        - 'results' (list): results (only their needed field values)
                note: the monetary fields will be strings properly formatted and
                already containing the currency
        - 'results_count' (int): the number of results in the database
                that matched the search query
        - 'parts' (dict): presence of fields across all results
        - 'fuzzy_search': search term used instead of requested search
    """
    order = self._get_search_order(order)
    options = options or {}
    results_count, search_results, fuzzy_term = request.website._search_with_fuzzy(search_type, term, limit, order,options)
    if not results_count:
        return {
            'results': [],
            'results_count': 0,
            'parts': {},
        }
    term = fuzzy_term or term
    search_results = request.website._search_render_results(search_results, limit)

    mappings = []
    results_data = []
    for search_result in search_results:
        if search_result.get('model') and search_result.get('model') == 'product.template':
            for res in search_result['results_data']:
                product_id = request.env['product.product'].sudo().search(
                    [('default_code', '=', term), ('sale_ok', '=', True), ('product_tmpl_id', '=', int(res['id']))])
                if product_id and len(product_id.ids) == 1:
                    res['website_url'] = product_id.website_url
                    image = product_id._get_image_holder()
                    res['image_url'] = f'/web/image/{image._name}/{image.id}/image_1920'
        results_data += search_result['results_data']
        mappings.append(search_result['mapping'])
    if search_type == 'all':
        # Only supported order for 'all' is on name
        results_data.sort(key=lambda r: r.get('name', ''), reverse='name desc' in order)
    results_data = results_data[:limit]
    result = []
    for record in results_data:
        mapping = record['_mapping']
        mapped = {
            '_fa': record.get('_fa'),
        }
        for mapped_name, field_meta in mapping.items():
            value = record.get(field_meta.get('name'))
            if not value:
                mapped[mapped_name] = ''
                continue
            field_type = field_meta.get('type')
            if field_type == 'text':
                if value and field_meta.get('truncate', True):
                    value = shorten(value, max_nb_chars, placeholder='...')
                if field_meta.get('match') and value and term:
                    pattern = '|'.join(map(re.escape, term.split()))
                    if pattern:
                        parts = re.split(f'({pattern})', value, flags=re.IGNORECASE)
                        if len(parts) > 1:
                            value = request.env['ir.ui.view'].sudo()._render_template(
                                "website.search_text_with_highlight",
                                {'parts': parts}
                            )
                            field_type = 'html'

            if field_type not in ('image', 'binary') and ('ir.qweb.field.%s' % field_type) in request.env:
                opt = {}
                if field_type == 'monetary':
                    opt['display_currency'] = options['display_currency']
                value = request.env[('ir.qweb.field.%s' % field_type)].value_to_html(value, opt)
            mapped[mapped_name] = escape(value)
            if search_type == 'blogs':
                Blog_posts = request.env['blog.post'].sudo()
                rec_id = int(record['id'])
                rec_bg = ''
                rec = Blog_posts.search([('id', '=', rec_id)])
                if rec:
                    rec_bg = rec._get_background().replace("url(", "").replace(")", "")
                mapped['web_bg'] = rec_bg
        result.append(mapped)

    return {
        'results': result,
        'results_count': results_count,
        'parts': {key: True for mapping in mappings for key in mapping},
        'fuzzy_search': fuzzy_term,
    }

Website.autocomplete = autocomplete

from odoo.addons.payment import utils as payment_utils



class WebsiteSaleShop(WebsiteSale):

    def _get_search_options(
        self, category=None, attrib_values=None, pricelist=None, min_price=0.0, max_price=0.0, conversion_rate=1, **post
    ):
        return {
            'displayDescription': True,
            'displayDetail': True,
            'displayExtraDetail': True,
            'displayExtraLink': True,
            'displayImage': True,
            'allowFuzzy': not post.get('noFuzzy'),
            'category': category if category else None,
            'min_price': min_price / conversion_rate,
            'max_price': max_price / conversion_rate,
            'attrib_values': attrib_values,
            'display_currency': pricelist.currency_id,
        }

    def _get_mandatory_fields_billing(self, country_id=False):
        """Extend mandatory fields to add new industry main category and sub category fields """
        res = super()._get_mandatory_fields_billing(country_id)
        res += ["industry_main_category", "industry_sub_category","phone"]
        return res

    def _get_mandatory_fields_shipping(self, country_id=False):
        """Extend mandatory fields to add new industry main category and sub category fields """
        res = super()._get_mandatory_fields_shipping(country_id)
        res += ["industry_main_category", "industry_sub_category","phone"]
        return res

    @http.route()
    def shop(self, page=0, category=None, search='', min_price=0.0, max_price=0.0, ppg=False, **post):
        add_qty = int(post.get('add_qty', 1))
        try:
            min_price = float(min_price)
        except ValueError:
            min_price = 0
        try:
            max_price = float(max_price)
        except ValueError:
            max_price = 0

        if post and 'category_select' in post.keys():
            if post['category_select'] != '':
                del post['category_select']

        sortby_set = []
        if post and 'sort_by' in post.keys():
            if post['sort_by'] != '':
                sortby_set.append(post['sort_by'])
                post['order'] = post['sort_by']
                del post['sort_by']

        category_ids = []
        category_from_menu_or_footer = 0
        if category:
            category_ids.append(int(category))
            category_from_menu_or_footer = int(category)

        Category = request.env['product.public.category']
        category = Category


        if len(request.httprequest.args.getlist('category_select')) > 0:
            for cat in list(request.httprequest.args.getlist('category_select')):
                if cat != '':
                    val = int(cat.split('-')[1]) if int(cat.split('-')[1]) not in category_ids else False
                    if val:
                        category_ids.append(val)

        if category:
            category = Category.search([('id', '=', category)])
            if not category or not category.can_access_from_current_website():
                raise NotFound()
        else:
            category = Category


        website = request.env['website'].get_current_website()
        if ppg:
            try:
                ppg = int(ppg)
                post['ppg'] = ppg
            except ValueError:
                ppg = False
        if not ppg:
            ppg = website.shop_ppg or 20

        ppr = website.shop_ppr or 4

        attrib_list = request.httprequest.args.getlist('attrib')
        attrib_values = [[int(x) for x in v.split("-")] for v in attrib_list if v]
        attributes_ids = {v[0] for v in attrib_values}
        attrib_set = {v[1] for v in attrib_values}
        keep = QueryURL('/shop', **self._shop_get_query_url_kwargs(category and int(category), search, min_price, max_price, **post))
        now = datetime.timestamp(datetime.now())
        pricelist = request.env['product.pricelist'].browse(request.session.get('website_sale_current_pl'))
        if not pricelist or request.session.get('website_sale_pricelist_time', 0) < now - 60*60: # test: 1 hour in session
            pricelist = website.get_current_pricelist()
            request.session['website_sale_pricelist_time'] = now
            request.session['website_sale_current_pl'] = pricelist.id

        request.update_context(pricelist=pricelist.id, partner=request.env.user.partner_id)

        filter_by_price_enabled = website.is_view_active('website_sale.filter_products_price')
        if filter_by_price_enabled:
            company_currency = website.company_id.sudo().currency_id
            conversion_rate = request.env['res.currency']._get_conversion_rate(
                company_currency, pricelist.currency_id, request.website.company_id, fields.Date.today())
        else:
            conversion_rate = 1

        url = "/shop"
        if search:
            post["search"] = search
        if attrib_list:
            post['attrib'] = attrib_list
        if list(request.httprequest.args.getlist('category_select')):
            post['category_select'] = list(request.httprequest.args.getlist('category_select'))


        options = self._get_search_options(
            category=category_ids,
            attrib_values=attrib_values,
            pricelist=pricelist,
            min_price=min_price,
            max_price=max_price,
            conversion_rate=conversion_rate,
            **post
        )


        fuzzy_search_term, product_count, search_product = self._shop_lookup_products(attrib_set, options, post, search, website)

        filter_by_price_enabled = website.is_view_active('website_sale.filter_products_price')
        if filter_by_price_enabled:
            # TODO Find an alternative way to obtain the domain through the search metadata.
            Product = request.env['product.template'].with_context(bin_size=True)
            domain = self._get_search_domain(search, category, attrib_values)

            # This is ~4 times more efficient than a search for the cheapest and most expensive products
            query = Product._where_calc(domain)
            Product._apply_ir_rules(query, 'read')
            from_clause, where_clause, where_params = query.get_sql()
            query = f"""
                   SELECT COALESCE(MIN(list_price), 0) * {conversion_rate}, COALESCE(MAX(list_price), 0) * {conversion_rate}
                     FROM {from_clause}
                    WHERE {where_clause}
               """
            request.env.cr.execute(query, where_params)
            available_min_price, available_max_price = request.env.cr.fetchone()

            if min_price or max_price:
                if min_price:
                    min_price = min_price if min_price <= available_max_price else available_min_price
                    post['min_price'] = min_price
                if max_price:
                    max_price = max_price if max_price >= available_min_price else available_max_price
                    post['max_price'] = max_price

        website_domain = website.website_domain()
        categs_domain = [('parent_id', '=', False)] + website_domain
        if search:
            search_categories = Category.search(
                [('product_tmpl_ids', 'in', search_product.ids)] + website_domain
            ).parents_and_self
            categs_domain.append(('id', 'in', search_categories.ids))
        else:
            search_categories = Category
        categs = lazy(lambda: Category.search(categs_domain))

        if category:
            url = "/shop/category/%s" % slug(category)
        pager = website.pager(url=url, total=len(search_product), page=page, step=ppg, scope=5, url_args=post)
        offset = pager['offset']
        products = search_product[offset:offset + ppg]

        ProductAttribute = request.env['product.attribute']
        if products:
            # get all products without limit
            attributes = lazy(lambda: ProductAttribute.search([
                ('product_tmpl_ids', 'in', search_product.ids),
                ('visibility', '=', 'visible'),
            ]))
        else:
            attributes = lazy(lambda: ProductAttribute.browse(attributes_ids))

        variant_dict = {}
        attributes_value_ids = {v[1] for v in attrib_values}
        temp_list = []
        all_combinations = []
        if len(attributes_value_ids) > 1:
            for r in range(1, len(attributes_value_ids) + 1):
                combinations_r = list(itertools.combinations(attributes_value_ids, r))
                all_combinations.extend(combinations_r)

        if all_combinations:
            product_ids = request.env['product.product'].sudo().search([('product_tmpl_id', 'in', products.ids)])
            for attr_values in all_combinations:
                for x in product_ids:
                    if all(atb in iter(x.product_template_variant_value_ids.mapped('product_attribute_value_id').ids) for atb in list(attr_values)):
                        variant_dict[x.product_tmpl_id.id] = (x.website_url, x)
                        temp_list.append(x.product_tmpl_id.id)
                    elif any(atb in iter(x.product_template_variant_value_ids.mapped('product_attribute_value_id').ids) for atb in list(attr_values)):
                        if x.product_tmpl_id.id not in temp_list:
                            variant_dict[x.product_tmpl_id.id] = (x.website_url, x)

        if search.strip() and products:
            if not variant_dict:
                product_ids = request.env['product.product'].sudo().search([('product_tmpl_id', 'in', products.ids)])
                for product_variant in product_ids:
                    if product_variant.default_code and product_variant.default_code == search.strip():
                        variant_dict[product_variant.product_tmpl_id.id] = (product_variant.website_url, product_variant)

        layout_mode = request.session.get('website_sale_shop_layout_mode')
        if not layout_mode:
            if website.viewref('website_sale.products_list_view').active:
                layout_mode = 'list'
            else:
                layout_mode = 'grid'
            request.session['website_sale_shop_layout_mode'] = layout_mode

        products_prices = lazy(lambda: products._get_sales_prices(pricelist))

        fiscal_position_id = website._get_current_fiscal_position_id(request.env.user.partner_id)

        if len(sortby_set) > 0:
            order = sortby_set[0]
        else:
            order = 'website_sequence asc'
        mobile_rows = lazy(lambda: TableCompute().process(products, ppg, 2))

        values = {
            'search': fuzzy_search_term or search,
            'original_search': fuzzy_search_term and search,
            'order': order,
            'sortby_set': sortby_set,
            'category': category,
            'attrib_values': attrib_values,
            'attrib_set': attrib_set,
            'category_set': category_ids,
            'pager': pager,
            'pricelist': pricelist,
            'add_qty': add_qty,
            'products': products,
            'search_product': search_product,
            'search_count': product_count,  # common for all searchbox
            'bins': lazy(lambda: TableCompute().process(products, ppg, ppr)),
            'mobile_rows': mobile_rows,
            'ppg': ppg,
            'ppr': ppr,
            'categories': categs,
            'attributes': attributes,
            'keep': keep,
            'search_categories_ids': search_categories.ids,
            'layout_mode': layout_mode,
            'products_prices': products_prices,
            'get_product_prices': lambda product: lazy(lambda: products_prices[product.id]),
            'float_round': tools.float_round,
            'fiscal_position_id': fiscal_position_id,
        }
        if filter_by_price_enabled:
            values['min_price'] = min_price or available_min_price
            values['max_price'] = max_price or available_max_price
            values['available_min_price'] = tools.float_round(available_min_price, 2)
            values['available_max_price'] = tools.float_round(available_max_price, 2)
        if category:
            values['main_object'] = category
        values.update(self._get_additional_shop_values(values))
        values['variant_url'] = variant_dict
        return request.render("website_sale.products", values)

    @http.route()
    def cart_update_json(self, product_id, line_id=None, add_qty=None, set_qty=None, display=True, product_custom_attribute_values=None, no_variant_attribute_values=None, **kw):
        order = request.website.sale_get_order(force_create=True)
        if order.state != 'draft':
            request.website.sale_reset()
            if kw.get('force_create'):
                order = request.website.sale_get_order(force_create=True)
            else:
                return {}

        if product_custom_attribute_values:
            product_custom_attribute_values = json_scriptsafe.loads(product_custom_attribute_values)

        if no_variant_attribute_values:
            no_variant_attribute_values = json_scriptsafe.loads(no_variant_attribute_values)
      
        if isinstance(set_qty, int) and set_qty <= 0 and order and order.service and order.order_line and 1 >= len(order.order_line.filtered(lambda x: not x.is_delivery and not x.is_downpayment and not x.display_type)):
            order.service = False

        values = order._cart_update(
            product_id=product_id,
            line_id=line_id,
            add_qty=add_qty,
            set_qty=set_qty,
            product_custom_attribute_values=product_custom_attribute_values,
            no_variant_attribute_values=no_variant_attribute_values,
            **kw
        )

        request.session['website_sale_cart_quantity'] = order.cart_quantity

        if not order.cart_quantity:
            request.website.sale_reset()
            return values

        values['cart_quantity'] = order.cart_quantity
        values['minor_amount'] = payment_utils.to_minor_currency_units(
            order.amount_total, order.currency_id
        ),
        values['amount'] = order.amount_total

        if not display:
            return values

        values['website_sale.cart_lines'] = request.env['ir.ui.view']._render_template(
            "website_sale.cart_lines", {
                'website_sale_order': order,
                'date': fields.Date.today(),
                'suggested_products': order._cart_accessories()
            }
        )
        values['website_sale.short_cart_summary'] = request.env['ir.ui.view']._render_template(
            "website_sale.short_cart_summary", {
                'website_sale_order': order,
            }
        )
        return values

    @http.route(['/shop/cart/check_stock_and_update_json'], type='json', auth="public", methods=['POST'], website=True, csrf=False)
    def check_stock_and_update_json(
            self, product_id, line_id=None, add_qty=None, set_qty=None, display=True,
            product_custom_attribute_values=None, no_variant_attribute_values=None, **kw
    ):

        order = request.website.sale_get_order(force_create=True)
        if order.state != 'draft':
            request.website.sale_reset()
            if kw.get('force_create'):
                order = request.website.sale_get_order(force_create=True)
            else:
                return {}

        if product_custom_attribute_values:
            product_custom_attribute_values = json_scriptsafe.loads(product_custom_attribute_values)

        if no_variant_attribute_values:
            no_variant_attribute_values = json_scriptsafe.loads(no_variant_attribute_values)

        if isinstance(set_qty, int) and set_qty <= 0 and order and order.service and order.order_line and 1 >= len(
                order.order_line.filtered(lambda x: not x.is_delivery and not x.is_downpayment and not x.display_type)):
            order.service = False

        values = order._cart_update(
            product_id=product_id,
            line_id=line_id,
            add_qty=add_qty,
            set_qty=set_qty,
            product_custom_attribute_values=product_custom_attribute_values,
            no_variant_attribute_values=no_variant_attribute_values,
            **kw
        )

        request.session['website_sale_cart_quantity'] = order.cart_quantity

        if not order.cart_quantity:
            request.website.sale_reset()
            return values

        values['cart_quantity'] = order.cart_quantity
        values['minor_amount'] = payment_utils.to_minor_currency_units(
            order.amount_total, order.currency_id
        ),
        values['amount'] = order.amount_total

        if not display:
            return values

        values['website_sale.cart_lines'] = request.env['ir.ui.view']._render_template(
            "website_sale.cart_lines", {
                'website_sale_order': order,
                'date': fields.Date.today(),
                'suggested_products': order._cart_accessories()
            }
        )
        values['website_sale.short_cart_summary'] = request.env['ir.ui.view']._render_template(
            "website_sale.short_cart_summary", {
                'website_sale_order': order,
            }
        )
        useable_product_id = request.env['product.product'].sudo().browse([product_id])
        if useable_product_id and not useable_product_id.allow_out_of_stock_order:
            values['qty_available'] = useable_product_id.qty_available
            values['sale_delay'] = useable_product_id.sale_delay
            if useable_product_id.qty_available < float(values['quantity']):
                values['stock_unavialable'] = True
        return values

    @http.route()
    def address(self, **kw):
        Partner = request.env['res.partner'].with_context(show_address=1).sudo()
        order = request.website.sale_get_order()

        industry_id = kw.get('industry_id', False)
        sub_category_id = kw.get('sub_category_id', False)
        selected_phone_country_id = kw.get('selected_phone_country_id',False)
        phone = kw.get('phone',False)
        new_billing_partner_id = 'new_billing_partner_id' in kw.keys()

        if new_billing_partner_id:
            del kw['new_billing_partner_id']
        if selected_phone_country_id and phone:
            partner_country_id = request.env['res.country'].sudo().browse(int(selected_phone_country_id))
            new_phone = '+' + str(partner_country_id.phone_code) + ' ' + kw.get('phone','')
            kw.update({'phone': new_phone})
            del kw['selected_phone_country_id']

        if industry_id and sub_category_id:
            kw['industry_main_category'] = int(industry_id)
            kw['industry_sub_category'] = int(sub_category_id)

        redirection = self.checkout_redirection(order)
        if redirection:
            return redirection

        mode = (False, False)
        can_edit_vat = False
        values, errors = {}, {}
        partner_id = int(kw.get('partner_id', -1))

        current_partner_id = request.env['res.partner'].sudo().search([('id','=',partner_id)])

        # IF PUBLIC ORDER
        if order.partner_id.id == request.website.user_id.sudo().partner_id.id:
            mode = ('new', 'billing')
            can_edit_vat = True
        # IF ORDER LINKED TO A PARTNER
        else:
            if partner_id > 0:
                if current_partner_id.type == 'invoice' and partner_id in order.partner_id.child_ids.ids:
                    mode = ('edit', 'billing')
                    can_edit_vat = order.partner_id.can_edit_vat()
                elif partner_id == order.partner_id.id:
                    mode = ('edit', 'billing')
                    can_edit_vat = order.partner_id.can_edit_vat()
                else:
                    shippings = Partner.search([('id', 'child_of', order.partner_id.commercial_partner_id.ids)])
                    if new_billing_partner_id:
                        mode = ('new', 'billing')
                        can_edit_vat = True
                    elif order.partner_id.commercial_partner_id.id == partner_id:
                        mode = ('new', 'shipping')
                        partner_id = -1
                    elif partner_id in shippings.mapped('id'):
                        mode = ('edit', 'shipping')
                    else:
                        return Forbidden()
                if mode and partner_id != -1:
                    values = Partner.browse(partner_id)
            elif partner_id == -1:
                if new_billing_partner_id:
                    mode = ('new', 'billing')
                    can_edit_vat = True
                    kw['parent_id'] = request.env.user.partner_id.id
                    kw['type'] = 'invoice'
                else:
                    mode = ('new', 'shipping')
            else:  # no mode - refresh without post?
                return request.redirect('/shop/checkout')

        # IF POSTED
        if 'submitted' in kw and request.httprequest.method == "POST":
            pre_values = self.values_preprocess(kw)
            errors, error_msg = self.checkout_form_validate(mode, kw, pre_values)
            post, errors, error_msg = self.values_postprocess(order, mode, pre_values, errors, error_msg)

            if errors:
                errors['error_message'] = error_msg
                values = kw
            else:
                if industry_id and sub_category_id:
                    post['industry_main_category'] = int(industry_id)
                    post['industry_sub_category'] = int(sub_category_id)
                if new_billing_partner_id and mode[1] == 'billing':
                    post['parent_id'] = request.env.user.partner_id.id
                    post['type'] = 'invoice'

                partner_id = self._checkout_form_save(mode, post, kw)
                # We need to validate _checkout_form_save return, because when partner_id not in shippings
                # it returns Forbidden() instead the partner_id
                if isinstance(partner_id, Forbidden):
                    return partner_id
                fpos_before = order.fiscal_position_id
                if mode[1] == 'billing':
                    if not order.partner_id:
                        order.partner_id = partner_id
                    # This is the *only* thing that the front end user will see/edit anyway when choosing billing address
                    order.partner_invoice_id = partner_id

                    if not kw.get('use_same'):
                        kw['callback'] = kw.get('callback') or \
                                         (not order.only_services and (
                                                 mode[0] == 'edit' and '/shop/checkout' or '/shop/address'))
                    # We need to update the pricelist(by the one selected by the customer), because onchange_partner reset it
                    # We only need to update the pricelist when it is not redirected to /confirm_order
                    if kw.get('callback', False) != '/shop/confirm_order':
                        request.website.sale_get_order(update_pricelist=True)
                elif mode[1] == 'shipping':
                    order.partner_shipping_id = partner_id

                if order.fiscal_position_id != fpos_before:
                    order._recompute_taxes()

                # TDE FIXME: don't ever do this
                # -> TDE: you are the guy that did what we should never do in commit e6f038a
                # order.message_partner_ids = [(4, partner_id), (3, request.website.partner_id.id)]
                if not errors:
                    return request.redirect(kw.get('callback') or '/shop/confirm_order')
        render_values = {
            'website_sale_order': order,
            'partner_id': partner_id,
            'mode': mode,
            'checkout': values,
            'can_edit_vat': can_edit_vat,
            'error': errors,
            'callback': kw.get('callback'),
            'only_services': order and order.only_services,
            'account_on_checkout': request.website.account_on_checkout,
            'is_public_user': request.website.is_public_user()
        }
        render_values.update(self._get_country_related_render_values(kw, render_values))
        return request.render("website_sale.address", render_values)

    @http.route('/render/address',type='http', auth="user",website=True)
    def render_address(self,**kw):
        if 'redirect_to_address' in dict(request.session).keys():
            redirect_to_address = request.session['redirect_to_address']
            del request.session['redirect_to_address']
            kwargs = redirect_to_address['kwargs']
            render_values = redirect_to_address['render_values']
            render_values['website_sale_order'] = request.env['sale.order'].sudo().browse(int(render_values['website_sale_order']))
            render_values.update(self._get_country_related_render_values(kw, render_values))
            return request.render("website_sale.address", render_values)

        if 'without_error_redirect' in dict(request.session).keys():
            without_error_redirect = request.session['without_error_redirect']
            del request.session['without_error_redirect']
            return request.redirect(without_error_redirect)

        if 'forbidden_error' in dict(request.session).keys():
            del request.session['forbidden_error']
            return Forbidden()

        if 'redirect_to_shop_checkout' in dict(request.session).keys():
            redirect_to_shop_checkout = request.session['redirect_to_shop_checkout']
            del request.session['redirect_to_shop_checkout']
            return request.redirect('/shop/checkout')

        if 'return_partner_id' in dict(request.session).keys():
            return_partner_id = request.session['return_partner_id']
            del request.session['return_partner_id']
            return return_partner_id

        if 'checkout_redirection' in dict(request.session).keys():
            checkout_redirection = request.session['checkout_redirection']
            del request.session['checkout_redirection']
            return request.redirect(checkout_redirection)

        return request.redirect('/shop/address')

    def _get_country_related_render_values(self, kw, render_values):
        values = render_values['checkout']
        mode = render_values['mode']
        order = render_values['website_sale_order']

        def_country_id = order.partner_id.country_id
        # IF PUBLIC ORDER
        if order.partner_id.id == request.website.user_id.sudo().partner_id.id:
            country_code = request.geoip.get('country_code')
            if country_code:
                def_country_id = request.env['res.country'].search([('code', '=', country_code)], limit=1)
            else:
                def_country_id = request.website.user_id.sudo().country_id

        country = 'country_id' in values and values['country_id'] != '' and request.env['res.country'].browse(int(values['country_id']))
        country = country and country.exists() or def_country_id

        res = {
            'country': country,
            'country_states': country.get_website_sale_states(mode=mode[1]),
            'countries': country.get_website_sale_countries(mode=mode[1]),
        }
        return res