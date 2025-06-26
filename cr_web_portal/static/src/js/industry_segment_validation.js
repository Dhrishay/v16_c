odoo.define('cr_web_portal.industry_validation', function (require) {
'use strict';
   var ajax = require('web.ajax');
    $(document).ready(function(){
        $('.industry_segment_btn').on('click',function(){
            ajax.jsonRpc("/industry_segment_validate", 'call', {}).then( function (result) {
                if(!result['address_mandatory']){
                    $('.css_not_available_msg.industry-segmat-warning')[0].innerHTML = "Please update your billing/shipping address in your profile to proceed with placing your order or inquiry. <a href='/my/account' style='text-decoration: underline;color:#717173;'>Click here</a> to update your billing/shipping address.";
                    $('.css_not_available_msg.industry-segmat-warning').css('display','block');
                }
                if(!result['industry_mandatory']){
                    $('.css_not_available_msg.industry-segmat-warning')[0].innerHTML = "Please update your category segmentation in your profile to proceed with placing your order or inquiry.<a href='/my/account' style='text-decoration: underline;color:#717173;'>Click here</a> to update your category segmentation.";
                    $('.css_not_available_msg.industry-segmat-warning').css('display','block');
                }
                else{
                    var textarea_fields = $("form.industry_segment_validation").find('textarea')
                    var input_fields = $("form.industry_segment_validation").find('input')
                    var selection_fields = $("form.industry_segment_validation").find('select')
                    var all_required_fields = []

                    if(textarea_fields.length > 0){
                        for(let i=0; i<textarea_fields.length; i++){
                            if(textarea_fields[i].getAttribute('required') == 'required'){
                                 all_required_fields.push(textarea_fields[i])
                            }
                        }
                    }
                    if(input_fields.length > 0){
                         for(let i=0; i<input_fields.length; i++){
                            if(input_fields[i].getAttribute('required') == 'required'){
                                 all_required_fields.push(input_fields[i])
                            }
                        }
                    }
                    if(selection_fields.length > 0){
                        for(let i=0; i<selection_fields.length; i++){
                            if(selection_fields[i].getAttribute('required') == 'required'){
                                 all_required_fields.push(selection_fields[i])
                            }
                        }
                    }
                    var require_field_is_empty = true

                    if(all_required_fields.length > 0){
                        for(let i=0; i< all_required_fields.length; i++){
                            if(all_required_fields[i].value == ""){
                                require_field_is_empty = false
                            }

                        }
                    }
                    var per_f = false
                    var quantity = 0
                    if ($('input[type="number"]')[0] != undefined){
                        per_f = true
                        var quantity = $('input[type="number"]')[0].value
                     }
                    if (per_f == true && quantity == 0){
                       $(".check-digit-message").removeClass('d-none')
                       $(".check-digit-message")[0].childNodes[1].innerText = 'Should be enter greator than 0';
                    }
                    else if(require_field_is_empty == true){
                        if($('.css_not_available_msg.industry-segmat-warning').length > 0){
                            $('.css_not_available_msg.industry-segmat-warning').css('display','none');
                        }
                        if($('.css_not_available_msg.form-fields-warning').length > 0){
                             $('.css_not_available_msg.form-fields-warning').css('display','none');
                        }
                         $("form.industry_segment_validation").submit();
                         $.blockUI({
                            'message': '<h4 class="text-white"><img src="/web/static/img/spin.png" class="fa-pulse"/>' +
                                '    <br />' + 'Please Wait....' +
                                '</h4>'
                        });
                    }
                    else{
                            $('.css_not_available_msg.form-fields-warning').css('display','block');
                    }
                }
            });
        });
    });
});




