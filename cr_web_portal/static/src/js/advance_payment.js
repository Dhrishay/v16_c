/** @odoo-module **/

import publicWidget from "web.public.widget";
import "website_sale_delivery.checkout";
import { _t } from 'web.core';

const WebsiteSaleDeliveryWidget = publicWidget.registry.websiteSaleDelivery;
publicWidget.registry.websiteSaleDelivery.include({

    _handleCarrierUpdateResultBadge: function (result) {
        var $carrierBadge = $('#delivery_carrier .o_delivery_carrier_select .custom-radio input[name="delivery_type"][value=' + result.carrier_id + ']');
        if($carrierBadge.length > 0){
            $carrierBadge = $carrierBadge.parent().parent().find('.o_wsale_delivery_badge_price')
        }
        if (result.status === true) {
             // if free delivery (`free_over` field), show 'Free', not '$0'
             if (result.is_free_delivery) {
                 $carrierBadge.text(_t('Free'));
             } else {
                 $carrierBadge.html(result.new_amount_delivery);
             }
             $carrierBadge.removeClass('o_wsale_delivery_carrier_error');
        } else {
            $carrierBadge.addClass('o_wsale_delivery_carrier_error');
            $carrierBadge.text(result.error_message);
        }
    },
});


WebsiteSaleDeliveryWidget.include({
    _handleCarrierUpdateResult: function (result) {
        this._super(...arguments);
        var min = 0.00;
        var max = 0.00;
        var advance_payment = 0.00;
         $('.order_total_value')[0].value = result.new_amount_total_raw
        var total_amount = $('.order_total_value')[0].value
        if('min' in result){
            min = result.min
        }
        if('max' in result){
            max = result.max
        }
        if('advance_payment' in result){
            advance_payment = result.advance_payment
        }
        if($('.payable_amount').length){
            for(var rec of $('.payable_amount')){
                rec.min = min;
                rec.max = max;
                rec.value = advance_payment;
            }
        }
        if ($('.remaining_amount').length) {
            for (var rec of $('.remaining_amount')) {
                var remaining = '₹ ' + ((total_amount - advance_payment).toFixed(2) || "0.00");
                rec.innerText = remaining;
            }
        }
    },
});
