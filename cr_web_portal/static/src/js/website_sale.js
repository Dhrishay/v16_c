odoo.define('cr_web_portal.website_sale', function(require) {
    "use strict";

    require('website_sale.website_sale');
    var core = require('web.core');
    var _t = core._t;
    var ajax = require('web.ajax');
    const utils = require('web.utils');
    var publicWidget = require('web.public.widget');
    var config = require('web.config');
    var VariantMixin = require('website_sale.VariantMixin');
    var wSaleUtils = require('website_sale.utils');
    const cartHandlerMixin = wSaleUtils.cartHandlerMixin;
    const {
        extraMenuUpdateCallbacks
    } = require('website.content.menu');
    const dom = require('web.dom');
    const {
        ComponentWrapper
    } = require('web.OwlCompatibility');
    const {
        ProductImageViewerWrapper
    } = require("@website_sale/js/components/website_sale_image_viewer");

    publicWidget.registry.WebsiteSale.include({

        showToast: async function(type, message) {
            var toastContainer = $("#toast-container");
            if(toastContainer.length == 0){
                toastContainer = await $('<div id="toast-container"></div>').insertBefore(".oe_website_sale");
            }
            // Define icons based on type
            if (type === 'warning'){
                var iconSrc = "/cr_web_portal/static/src/images/new_design_resource/warning.svg"
            }
            else{
                var iconSrc = type === "success" ? "/cr_web_portal/static/src/images/new_design_resource/email_success_img.svg" : "/cr_web_portal/static/src/images/new_design_resource/email_error_img.svg";
            }
            const closeSrc = "/cr_web_portal/static/src/images/new_design_resource/black_cross_btn.svg";
            // Create the toast element
            const toast = $(`
                    <div class="toast ${type}">
                      <div class="message">
                        <img src="${iconSrc}" alt="${type} icon">
                        <span>${message}</span>
                      </div>
                      <button class="close-btn">
                        <img src="${closeSrc}" alt="Close button">
                      </button>
                    </div>
                  `);

            // Append the toast to the container
            toastContainer.append(toast);

            // Show the toast
            setTimeout(() => {
                toast.addClass("show");
            }, 100);

            //           Auto-remove the toast after 5 seconds
            setTimeout(() => {
                toast.removeClass("show");
                toast.on("transitionend", function() {
                    toast.remove();
                });
            }, 5000);

            // Close button functionality
            toast.find(".close-btn").on("click", function() {
                toast.removeClass("show");
                toast.on("transitionend", function() {
                    toast.remove();
                });
            });
        },

        _handleAdd: async function($form) {
            var temp = false
            var msg = ''
            if ($('.is_custimizable').length > 0) {
                if ($('.is_custimizable')[0].checked) {
                    var temp = await ajax.jsonRpc('/create/product/variant', 'call', {})
                }
                var place_inq = await ajax.jsonRpc('/check/order/non-customisable/inquiry', 'call', {
                    'is_p_inquiry': false
                })

                if ($('.is_custimizable')[0].checked) {
                    var temp = await ajax.jsonRpc('/check/order/non-customisable', 'call', {})
                    var msg = 'It appears you already have a non-customizable product in your cart. You cannot add a customizable product at this time. Select either customisable or non-customisable product to process checkout.'
                } else if (place_inq) {
                    var temp = true
                    var msg = 'It seems you already have a customizable product in your cart. You cannot add a non-customizable product at this time. Select either customizable or non-customizable product to process checkout.'
                } else {
                    var temp = await ajax.jsonRpc('/check/order/customisable', 'call', {})
                    var msg = 'It seems you already have a customizable product in your cart. You cannot add a non-customizable product at this time. Select either customizable or non-customizable product to process checkout.'
                }
                if (temp) {
                    await this.showToast('warning',"<div class='error-msg-word'>Customization error!</div>" + msg)
                    return
                }

            }

            var self = this;
            this.$form = $form;

            var productSelector = [
                'input[type="hidden"][name="product_id"]',
                'input[type="radio"][name="product_id"]:checked'
            ];

            var productReady = this.selectOrCreateProduct(
                $form,
                parseInt($form.find(productSelector.join(', ')).first().val(), 10),
                $form.find('.product_template_id').val(),
                false
            );
            var $qty = $('.css_quantity .quantity.quantity-num')
            if ($qty.length > 0) {
                $qty = $qty.val()
                await this.showToast('success', "<span class='success-msg-word'>" + $qty + " Item added to your cart!</span> View Cart or Continue Shopping.")
            }
            return productReady.then(async function(productId) {
                $form.find(productSelector.join(', ')).val(productId);
                self._updateRootProduct($form, productId);
                return self._onProductReady();
            });
        },

        // onchange cart quantity in when shop cart line
        _changeCartQuantity: async function($input, value, $dom_optional, line_id, productIDs) {
            _.each($dom_optional, function(elem) {
                $(elem).find('.js_quantity').text(value);
                productIDs.push($(elem).find('span[data-product-id]').data('product-id'));
            });
            $input.data('update_change', true);
            var self = this;
            await this._rpc({
                route: "/shop/cart/check_stock_and_update_json",
                params: {
                    line_id: line_id,
                    product_id: parseInt($input.data('product-id'), 10),
                    set_qty: value
                },
            }).then(async function(data) {
                var qty_available = 0;
                var stock_unavialable = false;

                if('stock_unavialable' in data){
                    stock_unavialable = data.stock_unavialable
                    if('qty_available' in data){
                        qty_available = data.qty_available
                    }
                }
                $input.data('update_change', false);
                var check_value = parseInt($input.val() || 0, 10);
                if (isNaN(check_value)) {
                    check_value = 1;
                }
                if (value !== check_value) {
                    $input.trigger('change');
                    return;
                }
                sessionStorage.setItem('website_sale_cart_quantity', data.cart_quantity);
                if (!data.cart_quantity) {
                    return window.location = '/shop/cart';
                }
                $input.val(data.quantity);
                $('.js_quantity[data-line-id=' + line_id + ']').val(data.quantity).text(data.quantity);

                if(stock_unavialable){
                    await self.showToast('error', "<span class='error-msg-word'>Stock alert!</span> The quantity you selected is not available. Please choose up to "+qty_available+" Qty.");
                }
                wSaleUtils.updateCartNavBar(data);
                wSaleUtils.showWarning(data.warning);
                // Propagating the change to the express checkout forms
                core.bus.trigger('cart_amount_changed', data.amount, data.minor_amount);
            });
        },
    })

});