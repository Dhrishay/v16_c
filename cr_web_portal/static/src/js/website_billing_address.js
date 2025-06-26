odoo.define('cr_web_portal.website_billing_address', function (require) {
'use strict';

    var core = require('web.core');
    var config = require('web.config');
    var publicWidget = require('web.public.widget');
    var ajax = require('web.ajax');

    publicWidget.registry.websiteSaleBillingAddress = publicWidget.Widget.extend({
        selector: '.oe_website_sale .oe_cart',
        events: {
            'click .js_change_billing': '_onClickChangeBilling',
            'click .js_edit_billing_address': '_onClickEditBillingAddress',
            'click .a_new_billing_submit': '_onClickNewBillingAddress',
        },

        async start() {
            await this._super(...arguments);
        },
        
        _onClickChangeBilling: async function (ev) {
            var $old = $('.all_billing').find('.card.border.border-primary');
            var order_id = $('#current_order_id')[0].getAttribute('value')
            var $new = $(ev.currentTarget).parent('div.one_kanban').find('.card');
            var selected_partner_id = $new[0].getAttribute('partner')

            var res = ajax.jsonRpc("/set_partner_invoice_id", 'call', {'order_id':order_id,'selected_partner_id':selected_partner_id});
            $old.find('.btn-billing').toggle();
            $old.addClass('js_change_billing');
            $old.removeClass('border border-primary');

            $new.find('.btn-billing').toggle();
            $new.removeClass('js_change_billing');
            $new.addClass('border border-primary');

            var $form = $(ev.currentTarget).parent('div.one_kanban').find('form.d-none');
            $.post($form.attr('action'), $form.serialize()+'&xhr=1');
        },
        
        _onClickEditBillingAddress: function (ev) {
            ev.preventDefault();
            $(ev.currentTarget).closest('div.one_kanban').find('form.d-none').attr('action', '/shop/address').submit();
        },
        _onClickNewBillingAddress: function (ev) {
            ev.preventDefault();
            $(ev.currentTarget).closest('div.one_kanban').find('form.form-add-new').attr('action', '/shop/address').submit();
        },

    });

});


