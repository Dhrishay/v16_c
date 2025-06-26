/** @odoo-module **/

import "website_sale.website_sale";
import publicWidget from "web.public.widget";
import { session } from "@web/session";
import { qweb, _t } from "web.core";
import ajax from 'web.ajax';
import VariantMixin from 'sale.VariantMixin';

publicWidget.registry.WebsiteSale.include({

    _onChangeCombination: async function(ev, $parent, combination) {
        this._super.apply(this, arguments);
        $.blockUI();
        $('.blockOverlay').css({
            'background-color': 'transparent'
        })
        if (combination.is_combination_possible == false) {
            if (!$('.toast').length) {
                VariantMixin.showToast('error', "This combination does not exist.");
            }
        }
        setTimeout(async function() {
            if (combination.is_customisable) {
                $('.is_custimizable_block').removeClass('d-none')
                $('.customization-desktop-view').removeClass('d-none')
                $('.customization-desktop-view').tooltip({
                    title: `<div href="#is_custimizable_block"><img src="${combination.product_img}" style="display: block;"></div>`,
                    html: true,
                    placement: 'bottom',
                    container: '.customization-card-tooltip',
                });

            } else {
                $('.is_custimizable_block').addClass('d-none')
                $('.customization-card-tooltip').addClass('d-none')
            }
            var product_id = combination.product_id
            var current = this;
            ajax.jsonRpc("/get/product/files", 'call', {
                'product_id': product_id,
            }).then(function(data) {
                $('.attachment_content').remove();
                $('.class_dynamic_product_attachment').append($(qweb.render('cr_web_portal.attachment_files_owl_template', {
                    'product_variant': data
                })));
                $('.default_code').empty();
                $('.default_code').text(data.internal_ref);
                $('.product_qty_price_table').remove();
                if (data.dynamic_html) {
                    $('.dynamic_content').append(data.dynamic_html)
                }
            });
            const quantity = $parent.find('.css_quantity');
            const productPriceTag = $parent.find('.exclusive_price_tag');
            if (combination.prevent_zero_price_sale) {
                if(quantity.hasClass('d-none')){
                    quantity.removeClass('d-none').addClass('d-inline-flex');
                }else{
                     quantity.addClass('d-inline-flex');
                }
                productPriceTag.removeClass('d-inline-block').addClass('d-none');
            }else{
                 productPriceTag.removeClass('d-none').addClass('d-inline-block');
            }
            if ($("meta[itemprop='availability']").length) {
                $("meta[itemprop='availability']").remove();
                $("<meta itemprop='availability' content='" + combination['is_product_instock_schema'] + "'/>").insertAfter($("[itemprop='price']"));
            } else {
                $("<meta itemprop='availability' content='" + combination['is_product_instock_schema'] + "'/>").insertAfter($("[itemprop='price']"));
            }

            $.unblockUI();
        }, 500)

    },

});

publicWidget.registry.websiteSaleCart.include({
    _onClickDeleteProduct: function (ev) {
        ev.preventDefault();
        $(ev.currentTarget).parent().parent().find('.js_quantity').val(0).trigger('change');

    },
});