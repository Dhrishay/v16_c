odoo.define('cr_web_portal.website_sale_stock_variantMixin', function (require) {
'use strict';

const {Markup} = require('web.utils');
var VariantMixin = require('sale.VariantMixin');
var publicWidget = require('web.public.widget');
var core = require('web.core');
var QWeb = core.qweb;

require('website_sale.website_sale');
VariantMixin.showToast = function (type, message) {
    const toastContainer = $("#toast-container");
    // Define icons based on type
    const iconSrc = type === "success" ? "/cr_web_portal/static/src/images/new_design_resource/email_success_img.svg" : "/cr_web_portal/static/src/images/new_design_resource/email_error_img.svg";
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
        VariantMixin.removeToast(toast);
    }, 5000);

    // Close button functionality
    toast.find(".close-btn").on("click", function() {
        VariantMixin.removeToast(toast);
    });
}

VariantMixin.removeToast = function (toast) {
    toast.removeClass("show");
    toast.on("transitionend", function() {
        toast.remove();
    });
}

VariantMixin._onChangeCombinationStock = async function (ev, $parent, combination) {
    const palce_inquiry_btn = $parent.find('#palce_inquiry_btn');
    if (combination.prevent_zero_price_sale) {
        palce_inquiry_btn.removeClass('d-none').addClass('d-flex')
    }
    else{
        palce_inquiry_btn.removeClass('d-flex').addClass('d-none')
    }
    let product_id = 0;
    // needed for list view of variants
    if ($parent.find('input.product_id:checked').length) {
        product_id = $parent.find('input.product_id:checked').val();
    } else {
        product_id = $parent.find('.product_id').val();
    }
    const isMainProduct = combination.product_id &&
        ($parent.is('.js_main_product') || $parent.is('.main_product')) &&
        combination.product_id === parseInt(product_id);

    if (!this.isWebsite || !isMainProduct) {
        return;
    }

    const $addQtyInput = $parent.find('input[name="add_qty"]');
    let qty = $addQtyInput.val();
    let ctaWrapper = $parent[0].querySelector('#o_wsale_cta_wrapper');
    ctaWrapper.classList.replace('d-none', 'd-flex');
    ctaWrapper.classList.remove('out_of_stock');
    var available_qty = await this._rpc({
        route: "/get_product_quantity",
        params: {
            product_id: combination.product_id,
        },
    })
    let product_qty_available = available_qty - (combination.cart_qty + parseInt(qty))
    if (combination.product_type === 'product' && !combination.allow_out_of_stock_order) {
        combination.free_qty -= parseInt(combination.cart_qty);
        if (product_qty_available < 0) {
            ctaWrapper.classList.add('out_of_stock');
        }
    }

    $('.oe_website_sale').find('.availability_message_' + combination.product_template).remove();
    combination.has_out_of_stock_message = $(combination.out_of_stock_message).text() !== '';
    combination.out_of_stock_message = Markup(combination.out_of_stock_message);
    combination['product_qty_available'] = product_qty_available
    if( combination.product_type == 'product' && !combination.prevent_zero_price_sale && product_qty_available < 0){
//        if (!$('.toast').length) {
//            VariantMixin.showToast('error', "The product you're interested in is currently unavailable in the desired quantity. Expect a lead time of "+combination.sale_delay+" days for delivery.")
//        }
        return
    }

//    const $message = $(QWeb.render('cr_web_portal.product_availability',combination));
    if($('div#o_wsale_cta_wrapper.out_of_stock').length > 0){
        if (product_qty_available < 0) {
            if(document.querySelectorAll('#out_of_stock_message').length > 0){
            var divs = document.querySelectorAll('#out_of_stock_message')
                for(let i=0;i<divs.length; i++ ){
                    divs[i].classList.add('d-none');
                }
            }
//            $('div#o_wsale_cta_wrapper.out_of_stock').before($message);
            VariantMixin.showToast('error', "<span class='error-msg-word'>Stock alert!</span> The quantity you selected is not available. Please choose up to "+combination.qty_available+" Qty.")
        }
        else{
             if(document.querySelectorAll('#out_of_stock_message').length > 0){
                var divs = document.querySelectorAll('#out_of_stock_message')
                for(let i=0;i<divs.length; i++){
                    divs[i].classList.add('d-none');
                }
            }
        }
    }else{
        if(document.querySelectorAll('#out_of_stock_message').length > 0){
            var divs = document.querySelectorAll('#out_of_stock_message')
            for(let i=0;i<divs.length; i++){
                divs[i].classList.add('d-none');
            }
        }
    }
};


});
