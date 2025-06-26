odoo.define('cr_web_portal.payment_form', require => {
    'use strict';

    const checkoutForm = require('payment.checkout_form');
    var config = require('web.config');
    const CustomPaymentMixin = {

        //--------------------------------------------------------------------------
        // Private
        //--------------------------------------------------------------------------

        /**
         * Add `invoice_id` to the transaction route params if it is provided.
         *
         * @override method from payment.payment_form_mixin
         * @private
         * @param {string} code - The provider code of the selected payment option.
         * @param {number} paymentOptionId - The id of the selected payment option.
         * @param {string} flow - The online payment flow of the selected payment option.
         * @return {object} The extended transaction route params.
         */
        _prepareTransactionRouteParams: function (code, paymentOptionId, flow) {
            const transactionRouteParams = this._super(...arguments);
            if(config.device.isMobile){
                if ($('.payable_amount') && $('.payable_amount').length && $('.payable_amount')[0].value){
                    transactionRouteParams.amount = parseFloat($('.payable_amount')[0].value)
                    transactionRouteParams.isPartialPayment = true
                }
                if (this.$el.parent().parent().find('.portal_payable_amount') && this.$el.parent().parent().find('.portal_payable_amount').length && this.$el.parent().parent().find('.portal_payable_amount')[0].value){
                    transactionRouteParams.amount = parseFloat(this.$el.parent().parent().find('.portal_payable_amount').val())
                    transactionRouteParams.isPartialPayment = true
                }
            }else{
                if ($('.payable_amount') && $('.payable_amount').length && $('.payable_amount')[1].value){
                    transactionRouteParams.amount = parseFloat($('.payable_amount')[1].value)
                    transactionRouteParams.isPartialPayment = true
                }
                if (this.$el.parent().parent().find('.portal_payable_amount') && this.$el.parent().parent().find('.portal_payable_amount').length && this.$el.parent().parent().find('.portal_payable_amount').val()){
                    transactionRouteParams.amount = parseFloat(this.$el.parent().parent().find('.portal_payable_amount').val())
                    transactionRouteParams.isPartialPayment = true
                }
            }
            return {
                ...transactionRouteParams
            };
        },
         _onClickPaymentOption: function (ev) {
            const PaymentOption = this._super(...arguments);
            // Uncheck all radio buttons
            this.$('input[name="o_payment_radio"]').prop('checked', false);
            // Check radio button linked to selected payment option
            var $option_tags = $('.o_payment_option_tags').not('.d-none')
            var $option_icon_list = $('.o_payment_option_icon_list').not('.d-none')
            if($option_tags.length > 0){
                for(let el of $option_tags){
                    $(el).addClass('d-none');
                }
            }
            if($option_icon_list.length > 0){
                for(let el of $option_icon_list){
                    $(el).addClass('d-none');
                }
            }

            const checkedRadio = $(ev.currentTarget).find('input[name="o_payment_radio"]')[0];
            $(checkedRadio).prop('checked', true);

            let $current_o_payment_option_tags = $(ev.currentTarget).find('.o_payment_option_tags.d-none')
            if($current_o_payment_option_tags.length > 0){
                $current_o_payment_option_tags.removeClass('d-none');
            }

            let $current_o_payment_option_icon_list = $(ev.currentTarget).find('.o_payment_option_icon_list.d-none')
            if($current_o_payment_option_icon_list.length > 0){
                $current_o_payment_option_icon_list.removeClass('d-none');
            }

            // Show the inputs in case they had been hidden
            this._showInputs();

            // Disable the submit button while building the content
            this._disableButton(false);

            // Unfold and prepare the inline form of selected payment option
            this._displayInlineForm(checkedRadio);

            // Re-enable the submit button
            this._enableButton();

            const $submitButton = this.$('button[name="o_payment_submit_button"]');
            const custom_provider = $(ev.currentTarget).find('input[data-provider="custom"]');
            if (custom_provider.length){
                $submitButton[0].innerHTML = 'Place Order'
            }
            else{
                $submitButton[0].innerHTML = 'Pay Now'
            }
        },

    };

    checkoutForm.include(CustomPaymentMixin);

});