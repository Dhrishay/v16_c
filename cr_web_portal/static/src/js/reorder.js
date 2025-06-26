odoo.define('cr_web_portal.reorder', function (require) {
'use strict';
    var ajax = require('web.ajax');

    $(document).ready(function(){
        function updatePriceSummary() {
            let subtotal = 0;

            // Loop through each order line
            $('.reorder_qty').each(function() {
                const lineId = $(this).attr('id'); // Get the line ID from the input
                const quantity = parseInt($(this).val()) || 1; // Get the quantity
                const priceUnit = parseFloat($(`#price_unit_${lineId}`).text()) || 0; // Get the unit price
                const lineSubtotal = priceUnit * quantity; // Calculate subtotal for this line
                subtotal += lineSubtotal; // Add to the total subtotal
            });

            // Update the UI
            $('.reorder_subtotal_amount').text(subtotal.toFixed(2));
            $('.reorder_total_amount').text(subtotal.toFixed(2)); // For now, total = subtotal (add taxes, fees, etc. if needed)
        }

        // Quantity Update Function
        function updateQuantity(button, change) {
            const inputElement = $(button).parent().find('.reorder_qty');
            let quantity = parseInt(inputElement.val()) || 1; // Parse the input value, default to 1 if invalid
            quantity = Math.max(1, quantity + change); // Prevent quantity from going below 1
            inputElement.val(quantity); // Update the input value
            inputElement.trigger('change'); // Trigger the change event to update the price
        }

        // Trigger price update on quantity change
        $('.reorder_qty').on('change', function() {
            updatePriceSummary();
        });


        $(".jsOnchangeQty").change(function(event) {
            var currentElement = event.target
            if(currentElement){
                var unitPriceEle = $('#price_unit_'+currentElement.id)
                var PriceSubTotalEle = $('#price_subtotal_'+currentElement.id)
                var priceSubTotal = 0.0
                var qty = 0.0
                var unitPrice = 0.0
                if(parseFloat(unitPriceEle.text().trim()) > 0.00 && parseInt(currentElement.value) < 1 && PriceSubTotalEle.length){
                    unitPrice = parseFloat(unitPriceEle.text().trim())
                    qty =  1.00
                    currentElement.value = 1
                    priceSubTotal = unitPrice * qty
                    if(PriceSubTotalEle.find('.oe_currency_value').length){
                        PriceSubTotalEle.find('.oe_currency_value')[0].textContent = priceSubTotal.toFixed(2)
                    }
                }
                else if(parseFloat(unitPriceEle.text().trim()) > 0.00 && parseInt(currentElement.value) > 0 && PriceSubTotalEle.length){
                    unitPrice = parseFloat(unitPriceEle.text().trim())
                    qty =  parseFloat(currentElement.value)
                    priceSubTotal = unitPrice * qty
                    if(PriceSubTotalEle.find('.oe_currency_value').length){
                        PriceSubTotalEle.find('.oe_currency_value')[0].textContent = priceSubTotal.toFixed(2)
                    }
                }
            }
        });

        $(".js_delete_product_from_reorder").click(function(event) {
            if($('#line_'+event.target.id).length){
                $('#line_'+event.target.id)[0].remove()
                updatePriceSummary();
            }
        });

        $(".popupSubmitBtn").click(async function(event){
            if( $(event.target).parent().parent().find('.sale_tbody')[0].childElementCount > 0){
                var place_inq = await ajax.jsonRpc('/check/order/non-customisable/inquiry', 'call', {'is_p_inquiry':false})
                var check_customisable = await ajax.jsonRpc('/check/order/customisable', 'call', {})
                if(place_inq || check_customisable){
                    return alert('It seems you already have a customizable product in your cart. You cannot add a non-customizable product at this time. Select either customizable or non-customizable product to process checkout.');
                }
                else if(!place_inq && !check_customisable){
                    var formOrderId = $(event.target)[0].id.split('submitBtn')[1]
                    if($("form[id='"+formOrderId+"']").length){
                        $("form[id='"+formOrderId+"']").submit()
                    }
                }
            }else{
                return;
            }
        });
        if($(".js_delete_product_from_reorder").length){
            updatePriceSummary();
        }
    });
});