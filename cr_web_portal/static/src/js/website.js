odoo.define('cr_web_portal.website', function(require) {
    "use strict";

    require('website_sale.website_sale');
    var core = require('web.core');
    var _t = core._t;
    var ajax = require('web.ajax');
    const utils = require('web.utils');
    var publicWidget = require('web.public.widget');

    $(document).ready(function() {
        if (window.location && window.location.search == "?login-required" && $('.signup_confirmation-modal')){
            $('.signup_confirmation-modal').removeClass('d-none');
        };
        if (window.location && window.location.search == "?enclosure"){
            setTimeout(() => {
                $('a#enc_des').click()
            });
        };
        if (window.location && window.location.search == "?fused-deposition-modeling"){
            setTimeout(() => {
                $('a#fdm_3d').click()
            });
        };
        if (window.location && window.location.search == "?projection-printing-figure"){
            setTimeout(() => {
                $('a#projection_3d').click()
            });
        };
        if (window.location && window.location.search == "?sheet-metal-fabrication"){
            setTimeout(() => {
                $('a#sheet_metal_feb').click()
            });
        };
        if (window.location && window.location.search == "?injection-molding"){
            setTimeout(() => {
                $('a#injection_molding').click()
            });
        };
        if (window.location && window.location.search == "?cnc-machining"){
            setTimeout(() => {
                $('a#cnc_machining').click()
            });
        };

        $('.signup_confirmation-close').on('click', function() {
            $('.signup_confirmation-modal').addClass('d-none'); // Hide modal
        });

        $('.login_signup_confirmation-close').on('click', function() {
            $('.signup_confirmation-modal').addClass('d-none'); // Hide modal
        });

        setTimeout(() => {
            $('.o_web_sign_load_button').each(function(index, element) {
                 element.text = 'Upload' // Logs each button
            });
        }, 2000);

        $('.send_inquiry_button').on('click', function (e) {
            // Prevent the default action
            e.preventDefault();

            // Find the target button using the data-trigger attribute
            var targetClass = $(this).data('trigger');
            var $targetButton = $('.' + targetClass);

            // Trigger a click on the target button
            if ($targetButton.length) {
                $targetButton.trigger('click');
            }
        });

        async function showToast(type, message) {
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
            }, 500000000);

            // Close button functionality
            toast.find(".close-btn").on("click", function() {
                toast.removeClass("show");
                toast.on("transitionend", function() {
                    toast.remove();
                });
            });
        }

        if ($('.js_country_code_field').length) {
            (async function() {
                try {
                    var resp = await fetch('https://ipapi.co/json/');
                    var data = await resp.json();
                    if (data.country_code) {
                        var country_code = data.country_code.toUpperCase();
                        for (var rec of $('.js_country_code_field')) {
                            try {
                                var $input = $(rec);
                                var $countryDropdown = $input.closest('div').find("#" + country_code);
                                var nearest_number = $input[0].parentElement.parentElement.nextElementSibling.value;
                                if ($countryDropdown.length && !nearest_number) {
                                    $countryDropdown.trigger('click');
                                }
                                if (!$input.val()){
                                    $countryDropdown.trigger('click');
                                }
                            } catch (innerError) {
                                console.error("Error processing individual record:", innerError);
                            }
                        }
                    }
                } catch (error) {
                    console.error("Error fetching IP-based location data or processing records:", error);
                }
            })();
        }

        if ($('#selection_is_uv_printing') && $('#selection_is_uv_printing').length) {
            if ($('#selection_is_uv_printing').val() == 'Yes') {
                $('#uv_print_div').removeClass('d-none');
            }
        }
        //   styling from js for white space in all pages which has url '/my' , /my/purchase, /my/account
        if (window.location.href.indexOf("/my") > -1) {
            $("#wrapwrap").addClass("mp-overflow-auto");
        }
        else if(window.location.href.indexOf("/blog") > -1 ){
            if($("#wrap").length){
                $("#wrap").css("overflow", "hidden");
            }
        }
        else {
            $("#wrapwrap").css("overflow", "visible");
        }
        if (window.location && window.location.pathname == '/shop' && window.location.search.startsWith('?search') && $('.oe_website_sale').length){
            $('.oe_website_sale')[0].scrollIntoView()
        }
        if (window.location && window.location.search == "?have"){
            $('.mp-contactus-section')[0].scrollIntoView();
        }
        if($('.table_of_content_link').length){
            $($('.table_of_content_link')[0]).addClass('active');
        }

        $('#is_custimizable').click(function(ev) {
            if (ev.target.checked) {
                $('.product-price-discount').addClass('d-none');
                $('.dynamic_content').addClass('d-none');
                $('.js_check_product')[0].innerText = 'Submit Inquiry';
            } else {
                $('.product-price-discount').removeClass('d-none');
                $('.dynamic_content').removeClass('d-none');
                $('.js_check_product')[0].innerText = 'Add to cart';


            }
        });

        var files = $('.file-class');
        if (files != null) {
            for (let i = 0; i < files.length; i++) {
                $(files[i]).change(async function() {
                    var parent = files[i].parentNode;
                    var product_attachment = files[i]
                    var file = product_attachment.files[0];
                    var attachment_data = await utils.getDataURLFromFile(file);
                    var attachment_name = product_attachment.files[0].name;
                    var attachment_type = product_attachment.files[0].type;

                    parent.childNodes[3].value = attachment_name;
                    parent.childNodes[5].value = attachment_type;
                    parent.childNodes[7].value = attachment_data.split(",")[1];
                });
            }
        }

        var filerButtons = $('.outer-filter');
        if (filerButtons != null) {
            for (let i = 0; i < filerButtons.length; i++) {
                $(filerButtons[i]).click(async function() {
                    if ($(filerButtons[i]).hasClass('collapsed')) {
                        $(filerButtons[i]).removeClass('collapsed');
                        $(filerButtons[i].parentNode.nextElementSibling).addClass('show');
                    } else {
                        $(filerButtons[i]).addClass('collapsed');
                        $(filerButtons[i].parentNode.nextElementSibling).removeClass('show');
                    }
                });
            }
        }
        $('#industry_id').change(function() {
            ajax.jsonRpc("/filter_industry", 'call', {
                'main_category': this.value,
            }).then(function(data) {
                var selectstate = $('#sub_category_id');
                selectstate.empty();
                if (data.states.length) {
                    selectstate.append("<option value=''>Select Industry Affiliation Sub-category</option>")
                    _.each(data.states, function(x) {
                        var opt = $('<option>').text(x[1])
                            .attr('value', x[0]);
                        selectstate.append(opt);
                    });
                }
            });
        });

        $('#metal_feb_is_uv_printing').change(function() {
            if (this.value == 'Yes') {
                $('#metal_feb_uv_printing_file').attr("required", "true");
                $('.metal_feb_uv_printing_file_div_p').addClass('o_input_required');
                if ($('#metal_feb_uv_printing_file').attr("disabled") == 'disabled') {
                    $('#metal_feb_uv_printing_file').removeAttr("disabled");
                }
            } else {
                if ($('.metal_feb_uv_printing_file_div_p').hasClass('o_input_required')) {
                    $('.metal_feb_uv_printing_file_div_p').removeClass('o_input_required');
                }
                if ($('#metal_feb_uv_printing_file').attr("required") == 'required') {
                    $('#metal_feb_uv_printing_file').removeAttr("required");
                }
                if ($('#metal_feb_uv_printing_file').attr("disabled") != 'true') {
                    $('#metal_feb_uv_printing_file').attr("disabled", "true");
                }
            }
        });

        $('#projection_is_uv_printing').change(function() {
            if (this.value == 'Yes') {
                $('#projection_uv_printing_file').attr("required", "true");
                $('.projection_uv_printing_file_div_p').addClass('o_input_required');
                if ($('#projection_uv_printing_file').attr("disabled") == 'disabled') {
                    $('#projection_uv_printing_file').removeAttr("disabled");
                }
            } else {
                if ($('.projection_uv_printing_file_div_p').hasClass('o_input_required')) {
                    $('.projection_uv_printing_file_div_p').removeClass('o_input_required');
                }
                if ($('#projection_uv_printing_file').attr("required") == 'required') {
                    $('#projection_uv_printing_file').removeAttr("required");
                }
                if ($('#projection_uv_printing_file').attr("disabled") != 'true') {
                    $('#projection_uv_printing_file').attr("disabled", "true");
                }
            }
        });

        $('#fdm_is_uv_printing').change(function() {
            if (this.value == 'Yes') {
                $('#fdm_uv_printing_file').attr("required", "true");
                $('.fdm_uv_printing_file_div_p').addClass('o_input_required');
                if ($('#fdm_uv_printing_file').attr("disabled") == 'disabled') {
                    $('#fdm_uv_printing_file').removeAttr("disabled");
                }
            } else {
                if ($('.fdm_uv_printing_file_div_p').hasClass('o_input_required')) {
                    $('.fdm_uv_printing_file_div_p').removeClass('o_input_required');
                }
                if ($('#fdm_uv_printing_file').attr("required") == 'required') {
                    $('#fdm_uv_printing_file').removeAttr("required");
                }
                if ($('#fdm_uv_printing_file').attr("disabled") != 'true') {
                    $('#fdm_uv_printing_file').attr("disabled", "true");
                }
            }
        });

        $('#metal_feb_material').change(function() {
            if (this.value == 'Other') {
                $('#metal_feb_material_div_other').removeClass('d-none');
                $('.metal_feb_material_div_other_p').addClass('o_input_required');
                $('.metal_feb_material_div_other_input').attr("required", "true");
            } else {

                if (!$('#metal_feb_material_div_other').hasClass('d-none')) {
                    $('#metal_feb_material_div_other').addClass('d-none');
                }
                if ($('.metal_feb_material_div_other_p').hasClass('o_input_required')) {
                    $('.metal_feb_material_div_other_p').removeClass('o_input_required');
                }
                if ($('.metal_feb_material_div_other_input').attr("required") == 'required') {
                    $('.metal_feb_material_div_other_input').removeAttr("required");
                }

            }
        });

        $('#injection_mold_material').change(function() {
            if (this.value == 'Other') {
                $('#injection_mold_material_other_div_other').removeClass('d-none');
                $('.injection_mold_material_other_p').addClass('o_input_required');
                $('.injection_mold_material_other_input').attr("required", "true");
            } else {

                if (!$('#injection_mold_material_other_div_other').hasClass('d-none')) {
                    $('#injection_mold_material_other_div_other').addClass('d-none');
                }
                if ($('.injection_mold_material_other_p').hasClass('o_input_required')) {
                    $('.injection_mold_material_other_p').removeClass('o_input_required');
                }
                if ($('.injection_mold_material_other_input').attr("required") == 'required') {
                    $('.injection_mold_material_other_input').removeAttr("required");
                }

            }
        });

        $('#injection_mold_colour').change(function() {
            if (this.value == 'Other') {
                $('#injection_mold_colour_other_div_other').removeClass('d-none');
                $('.injection_mold_colour_other_p').addClass('o_input_required');
                $('.injection_mold_colour_other_input').attr("required", "true");
            } else {

                if (!$('#injection_mold_colour_other_div_other').hasClass('d-none')) {
                    $('#injection_mold_colour_other_div_other').addClass('d-none');
                }
                if ($('.injection_mold_colour_other_p').hasClass('o_input_required')) {
                    $('.injection_mold_colour_other_p').removeClass('o_input_required');
                }
                if ($('.injection_mold_colour_other_input').attr("required") == 'required') {
                    $('.injection_mold_colour_other_input').removeAttr("required");
                }

            }
        });


        $('#metal_feb_thickness').change(function() {
            if (this.value == 'Other') {
                $('#metal_feb_thickness_div_other').removeClass('d-none');
                $('.metal_feb_thickness_div_other_p').addClass('o_input_required');
                $('.metal_feb_thickness_div_other_input').attr("required", "true");
            } else {
                if (!$('#metal_feb_thickness_div_other').hasClass('d-none')) {
                    $('#metal_feb_thickness_div_other').addClass('d-none');
                }
                if ($('.metal_feb_thickness_div_other_p').hasClass('o_input_required')) {
                    $('.metal_feb_thickness_div_other_p').removeClass('o_input_required');
                }
                if ($('.metal_feb_thickness_div_other_input').attr("required") == 'required') {
                    $('.metal_feb_thickness_div_other_input').removeAttr("required");
                }

            }
        });

        $('#metal_feb_surface_finish').change(function() {
            if (this.value == 'Other') {
                $('#metal_feb_surface_finish_div_other').removeClass('d-none');
                $('.metal_feb_surface_finish_div_other_p').addClass('o_input_required');
                $('.metal_feb_surface_finish_div_other_input').attr("required", "true");
            } else {
                if (!$('#metal_feb_surface_finish_div_other').hasClass('d-none')) {
                    $('#metal_feb_surface_finish_div_other').addClass('d-none');
                }
                if ($('.metal_feb_surface_finish_div_other_p').hasClass('o_input_required')) {
                    $('.metal_feb_surface_finish_div_other_p').removeClass('o_input_required');
                }
                if ($('.metal_feb_surface_finish_div_other_input').attr("required") == 'required') {
                    $('.metal_feb_surface_finish_div_other_input').removeAttr("required");
                }

            }
        });

        $('#metal_feb_color').change(function() {
            if (this.value == 'Other') {
                $('#metal_feb_color_div_other').removeClass('d-none');
                $('.metal_feb_color_div_other_p').addClass('o_input_required');
                $('.metal_feb_color_div_other_input').attr("required", "true");
            } else {
                if (!$('#metal_feb_color_div_other').hasClass('d-none')) {
                    $('#metal_feb_color_div_other').addClass('d-none');
                }
                if ($('.metal_feb_color_div_other_p').hasClass('o_input_required')) {
                    $('.metal_feb_color_div_other_p').removeClass('o_input_required');
                }
                if ($('.metal_feb_color_div_other_input').attr("required") == 'required') {
                    $('.metal_feb_color_div_other_input').removeAttr("required");
                }

            }
        });

        $('#selection_is_uv_printing').change(function() {
            if (this.value == 'Yes') {
                $('#input_uv_printing').attr("required", "true");
                $('#uv_print_div').removeClass('d-none');
                $('.s_website_form_label_content').addClass('o_input_required');
                $('.addition_note').removeClass('o_input_required');
                if ($('#input_uv_printing').attr("disabled") == 'disabled') {
                    $('#input_uv_printing').removeAttr("disabled");
                }
            } else {
                if ($('.s_website_form_label_content').hasClass('o_input_required')) {
                    $('.s_website_form_label_content').removeClass('o_input_required');
                }
                if ($('#input_uv_printing').attr("required") == 'required') {
                    $('#input_uv_printing').removeAttr("required");
                }
                if ($('#input_uv_printing').attr("disabled") != 'true') {
                    $('#input_uv_printing').attr("disabled", "true");
                }
                if (!$('#uv_print_div').hasClass('d-none')) {
                    $('#uv_print_div').addClass('d-none')
                }
            }
        });

        $('#cnc_is_uv_printing').change(function() {
            if (this.value == 'Yes') {
                if ($('#cnc_uv_printing_file').attr("disabled") == 'disabled') {
                    $('#cnc_uv_printing_file').removeAttr("disabled");
                }
                $('#cnc_uv_printing_file').attr("required", "true");
                $('.cnc_uv_printing_file_div_p').addClass('o_input_required');

            } else {
                if ($('.cnc_uv_printing_file_div_p').hasClass('o_input_required')) {
                    $('.cnc_uv_printing_file_div_p').removeClass('o_input_required');
                }
                if ($('#cnc_uv_printing_file').attr("required") == 'required') {
                    $('#cnc_uv_printing_file').removeAttr("required");
                }
                if ($('#cnc_uv_printing_file').attr("disabled") != 'true') {
                    $('#cnc_uv_printing_file').attr("disabled", "true");
                }
            }
        });

        $('#injection_is_uv_printing').change(function() {
            if (this.value == 'Yes') {
                if ($('#injection_uv_printing_file').attr("disabled") == 'disabled') {
                    $('#injection_uv_printing_file').removeAttr("disabled");
                }
                $('#injection_uv_printing_file').attr("required", "true");
                $('.injection_uv_printing_file_div_p').addClass('o_input_required');

            } else {
                if ($('.injection_uv_printing_file_div_p').hasClass('o_input_required')) {
                    $('.injection_uv_printing_file_div_p').removeClass('o_input_required');
                }
                if ($('#injection_uv_printing_file').attr("required") == 'required') {
                    $('#injection_uv_printing_file').removeAttr("required");
                }
                if ($('#injection_uv_printing_file').attr("disabled") != 'true') {
                    $('#injection_uv_printing_file').attr("disabled", "true");
                }
            }
        });

        // for Filter Searchbar
        $('.search_filter_input').keyup(function(ev) {
            ev.preventDefault();
            ev.stopPropagation();
            if (ev.key == 'Enter') {
                ev.preventDefault();
                return false;
            }
            var input = $(ev.target)[0];
            var filter = input.value.toUpperCase();

            var div_inner_size = $(ev.target).parent().siblings('#inner-size')
            var a;
            if (div_inner_size.find('div.form-check').length == 0) {
                a = div_inner_size.find('label.form-check').hide();
            } else {
                a = div_inner_size.find('div.form-check').hide();

            }


            if (filter.trim() === '') {
                if (div_inner_size.find('div.form-check').length == 0) {
                    $(ev.target).parent().siblings('#inner-size').find('label.form-check').show();
                    return;
                } else {
                    $(ev.target).parent().siblings('#inner-size').find('div.form-check').show();
                    return;
                }
            }

            a.each(function() {
                var self_a = this;

                var txtValue = $(this).find('.form-check-label').text().toUpperCase();

                if (txtValue.includes(filter)) {
                    if ($(self_a).hasClass('show') != true) {
                        $(self_a).show();
                    }
                }
            });

        });

        $('#fdm_material').change(function() {
            var current_material = $('#fdm_material').val()
            $('#fdm_color').empty();
            if (current_material == 'ABS') {
                $('#fdm_color').append("<option value='white'>White</option>")
                $('#fdm_color').append("<option value='black'>Black</option>")
                $('#fdm_color').append("<option value='blue'>Blue</option>")
                $('#fdm_color').append("<option value='orange'>Orange</option>")
                $('#fdm_color').append("<option value='green'>Green</option>")
                $('#fdm_color').append("<option value='grey'>Grey</option>")
                $('#fdm_color').append("<option value='red'>Red</option>")
                $('#fdm_color').append("<option value='natural'>Natural</option>")

            }
            if (current_material == 'PLA') {
                $('#fdm_color').append("<option value='white'>White</option>")
                $('#fdm_color').append("<option value='black'>Black</option>")
                $('#fdm_color').append("<option value='blue'>Blue</option>")
                $('#fdm_color').append("<option value='orange'>Orange</option>")
                $('#fdm_color').append("<option value='green'>Green</option>")
                $('#fdm_color').append("<option value='grey'>Grey</option>")
                $('#fdm_color').append("<option value='red'>Red</option>")

            }
            if (current_material == 'PETG') {
                $('#fdm_color').append("<option value='white'>White</option>")
                $('#fdm_color').append("<option value='black'>Black</option>")
                $('#fdm_color').append("<option value='blue'>Blue</option>")
                $('#fdm_color').append("<option value='yellow'>Yellow</option>")
                $('#fdm_color').append("<option value='natural'>Natural</option>")

            }
            if (current_material == 'ASA') {
                $('#fdm_color').append("<option value='white'>White</option>")
                $('#fdm_color').append("<option value='black'>Black</option>")
                $('#fdm_color').append("<option value='orange'>Orange</option>")
                $('#fdm_color').append("<option value='green'>Green</option>")

            }
            if (current_material == 'TPU') {
                $('#fdm_color').append("<option value='black'>Black</option>")
                $('#fdm_color').append("<option value='natural'>Natural</option>")
            }
            if (current_material == 'TPE') {
                $('#fdm_color').append("<option value='natural'>Natural</option>")
            }
            //        $('#fdm_color').empty();
            //         selectOption.append(
            //                    $('<option></option>').val(val).html(text)
            //                );
        });



        $('#inquiry_request_select').change(function() {
            if (this.value == '') {
                if ($('#submit_inquiry_request').attr("disabled") != 'true') {
                    $('#submit_inquiry_request').attr("disabled", "true");
                }
            } else {
                if ($('#submit_inquiry_request').attr("disabled") == 'disabled') {
                    $('#submit_inquiry_request').removeAttr("disabled");
                }
            }
        });

        //   Homepage tab functionality

        $('.tab-btn-funcation').on("click", function(ev) {
            if (ev.currentTarget) {
                var tab_id = ev.currentTarget.id
                var buttons = $('.tab-btn-funcation')

                // loop for tab underline color add
                buttons.each(function(i) {
                    if (buttons[i].id == tab_id) {
                        buttons[i].classList.add('underline-border-green');
                    } else {
                        buttons[i].classList.remove('underline-border-green');
                    }
                })

                //  div appear on tab menu click
                if ($('.tab-funcation-form')) {
                    var tab_function_div = $('.tab-funcation-form')
                    tab_function_div.each(function(index) {
                        $(tab_function_div[index]).find('form')[0].reset();
                        if (tab_function_div[index].id == tab_id) {
                            tab_function_div[index].classList.remove('d-none');
                        } else {
                            tab_function_div[index].classList.add('d-none');
                        }
                    });
                }

            }

        });


        $('.place_inquiry').on("click", async function(ev) {
            var product_id = $('.product_id')[0].value
            var qty = $('input[name="add_qty"]')[0].value
            $('.is_custimizable_enquiry')[0].checked = true
            var temp = false
            var msg = ''
            if ($('.is_custimizable_enquiry')[0].checked) {
                var temp = await ajax.jsonRpc('/create/product/variant/inquiry', 'call', {})
            }
            if ($('.is_custimizable_enquiry')[0].checked) {
                var temp = await ajax.jsonRpc('/check/order/non-customisable/inquiry', 'call', {
                    'is_p_inquiry': true
                })
                var msg = 'It appears you already have a non-customizable product in your cart. You cannot add a customizable product at this time. Select either customisable or non-customisable product to process checkout. '
            }
            if (temp) {
                await showToast('warning',"<div class='error-msg-word'>Customization error!</div>" + msg)
                return
            }
            if (product_id && qty) {
                var order = await ajax.jsonRpc('/create_cart_inquiry', 'call', {
                    'product_id': product_id,
                    'qty': qty
                })
                if (order) {
                    window.location.href = '/shop/cart';
                }
            }

        });

        // it will help to redirect portal user to add to cart after sign in
        if (window.location.href.indexOf("/shop/checkout") > -1) {
            if ($('.redirect_to_add_to_cart') && $('.redirect_to_add_to_cart').length) {
                $('.redirect_to_add_to_cart')[0].value = 'True';
            }
        }


        if ($('.article-clicked')) {
            if ($('.article-clicked').length > 0) {
                for (let i = 0; i < $('.article-clicked').length; i++) {
                    $($('.article-clicked')[i]).click(async function() {
                        let url = this.getAttribute('href')
                        window.location.href = url;
                    });
                }
            }
        }

        // for country selection

        $('.js_select_country_code').on("click", async function(ev) {
            var phone_code = ev.currentTarget.getAttribute('data-phone_code')
            var country_id = ev.currentTarget.getAttribute('data-country_id')
            var button = $(ev.currentTarget.parentElement.parentElement).siblings()[0]
            var country_code_input_field = $(ev.currentTarget.parentElement.parentElement).siblings()[1]

            button.innerHTML = "<div id='img_code_vat' class='js_img_country_code country_img'> +" + phone_code + " <i class='fa fa-chevron-down'></i></div>"
            country_code_input_field.value = country_id
        });

        $('.search_country').keyup(function(ev) {
            ev.preventDefault();
            ev.stopPropagation();
            if (ev.key == 'Enter') {
                ev.preventDefault();
                return false;
            }
            var input = $(ev.target)[0];
            var searchInput = input.value.toUpperCase();



            var div_inner_size = $($(ev.currentTarget).parent().siblings()[0])
            var a = div_inner_size.find('a.js_select_country_code').hide();

            if (searchInput.trim() === '') {
                $('#country_id_list').find('a.js_select_country_code').show();
                return;
            }

            a.each(function() {
                var self_a = this;
                var txtValue = $(this).find('.form-country-name').text().toUpperCase();
                if (txtValue.includes(searchInput)) {
                    if ($(self_a).hasClass('show') != true) {
                        $(self_a).show();
                    }
                }
            });

        });

        // Loading On CREATE ACCOUNT
        $('#createAccountBtn').click(function(ev) {
            var input_fields = $('form.oe_sign_up_form').find('input');
            var selection_fields = $('form.oe_sign_up_form').find('select');
            var all_required_fields = []

            if (input_fields.length > 0) {
                for (let i = 0; i < input_fields.length; i++) {
                    if (input_fields[i].required == true) {
                        all_required_fields.push(input_fields[i])
                    }
                }
            }

            if (selection_fields.length > 0) {
                for (let i = 0; i < selection_fields.length; i++) {
                    if (selection_fields[i].required == true) {
                        all_required_fields.push(selection_fields[i])
                    }
                }
            }

            var require_field_is_empty = true

            if (all_required_fields.length > 0) {
                for (let i = 0; i < all_required_fields.length; i++) {
                    if (all_required_fields[i].value == "") {
                        require_field_is_empty = false
                    }

                }
            }
            if (require_field_is_empty == true) {
                $.blockUI({
                    'message': '<h4 class="text-white"><img src="/web/static/img/spin.png" class="fa-pulse"/>' +
                        '    <br />' + 'Please Wait....' +
                        '</h4>'
                });
            }
        });
        // Loading On SUBMIT SERVICE
        $('#submitServiceBtn').click(function(ev) {
            var textarea_fields = $("form.o_mark_required.mp_service_form").find('textarea')
            var input_fields = $("form.o_mark_required.mp_service_form").find('input')
            var all_required_fields = []

            if (textarea_fields.length > 0) {
                for (let i = 0; i < textarea_fields.length; i++) {
                    if (textarea_fields[i].required == true) {
                        all_required_fields.push(textarea_fields[i])
                    }
                }
            }
            if (input_fields.length > 0) {
                for (let i = 0; i < input_fields.length; i++) {
                    if (input_fields[i].required == true) {
                        all_required_fields.push(input_fields[i])
                    }
                }
            }
            var require_field_is_empty = true

            if (all_required_fields.length > 0) {
                for (let i = 0; i < all_required_fields.length; i++) {
                    if (all_required_fields[i].value == "") {
                        require_field_is_empty = false
                    }

                }
            }
            if (require_field_is_empty == true) {
                $.blockUI({
                    'message': '<h4 class="text-white"><img src="/web/static/img/spin.png" class="fa-pulse"/>' +
                        '    <br />' + 'Please Wait....' +
                        '</h4>'
                });
            }
        });
        // Loading On SUBMIT CONTACT US FORM
        $('#contactUsSubmitBtn').click(function(ev) {
            var textarea_fields = $("form#contactus_form.o_mark_required").find('textarea')
            var input_fields = $("form#contactus_form.o_mark_required").find('input')
            var textarea_fields = $("form#contactus_form.o_mark_required").find('textarea')
            var all_required_fields = []

            if (textarea_fields.length > 0) {
                for (let i = 0; i < textarea_fields.length; i++) {
                    if (textarea_fields[i].required == true) {
                        all_required_fields.push(textarea_fields[i])
                    }
                }
            }
            if (input_fields.length > 0) {
                for (let i = 0; i < input_fields.length; i++) {
                    if (input_fields[i].required == true) {
                        all_required_fields.push(input_fields[i])
                    }
                }
            }
            if (textarea_fields.length > 0) {
                for (let i = 0; i < textarea_fields.length; i++) {
                    if (textarea_fields[i].required == true) {
                        all_required_fields.push(textarea_fields[i])
                    }
                }
            }
            var require_field_is_empty = true

            if (all_required_fields.length > 0) {
                for (let i = 0; i < all_required_fields.length; i++) {
                    if (all_required_fields[i].value == "") {
                        require_field_is_empty = false
                    }

                }
            }
        });

        $("input.restrict_numbers").keydown(function(event) {
            var alphabetRegex = /[a-zA-Z]/;
            return alphabetRegex.test(event.key);
        });

        $("input.restrict_alphabets").keydown(function(event) {
            var numericRegex = /[0-9]/;
            if (event.ctrlKey) {
                if (event.keyCode === 65 || event.keyCode === 97) { // 'A' or 'a'
                    return true;
                }
                return true;
            } else if (event.key === "Backspace" || event.key === "Delete" || event.key === "Control" || event.key === "ArrowLeft" || event.key === "ArrowUp" || event.key === "ArrowRight" || event.key === "ArrowDown" || event.key === "Tab") {
                return true;
            } else {
                return numericRegex.test(event.key);
            }
        });

        $('.upload_file_1').click(function() {
            $('.s_website_form_input_1').trigger('click');
        });

        $('.s_website_form_input_1').change(function(event) {
            var input_values = $('.check-file-type-extra').val()
            var input_val = input_values.toLowerCase()
            var ext = input_val.split(".");
            var arrayExtensions = ["zip", "stl", "step", "stp", "stp", "obj", "3MF", "pdf", "zip", "dxf", "dwg", "iges", "sldprt"];
            var ext_1 = ext[ext.length - 1]
            var new_filename = "";
            if(input_values){
                new_filename = input_values.split('\\').pop();
            }
            if (!arrayExtensions.includes(ext_1)) {
                $(".check-file-type-extra").val("");
            }
            if ($('.check-file-type-extra').val()) {
                // $('.already_uploaded_drawing_file_1').addClass('d-none')
                // $('.upload_file_1').addClass('d-none')
                // $('.s_website_form_input_1').removeClass('d-none')
                if(new_filename){
                    var sections = $(event.currentTarget.parentElement.parentElement.parentElement).find('.uploading-file-section')
                    for(var sec of sections){
                        sec.innerText = new_filename;
                    }
                }
            }
        });

        $('.upload_file_2').click(function() {
            $('.s_website_form_input_2').trigger('click');
        });

        $('.s_website_form_input_2').change(function() {
            var input_values = $('.check-file-type_uv').val()
            var input_val = input_values.toLowerCase()
            var ext = input_val.split(".");
            var arrayExtensions = ["tiff", "png", "jpeg", "jpg", "pdf"];
            var ext_1 = ext[ext.length - 1]
            var new_filename = "";
            if(input_values){
                new_filename = input_values.split('\\').pop();
            }
            if (!arrayExtensions.includes(ext_1)) {
                $('.check-file-type_uv').val("");
            }
            if ($('.check-file-type_uv').val()) {
                if(new_filename){
                    var sections = $(event.currentTarget.parentElement.parentElement.parentElement).find('.uploading-file-section')
                    for(var sec of sections){
                        sec.innerText = new_filename;
                    }
                }
            }
        });

        $('.country_onchange').change(function() {
            if (!$("#country_id").val()) {
                return;
            }
            ajax.jsonRpc("/filter_state", 'call', {
                'country_id': $("#country_id").val(),
            }).then(function(data) {
                var selectstate = $('#state_id');
                selectstate.empty();
                if (data.length) {
                    selectstate.append("<option value=''>Select State...</option>")
                    _.each(data, function(x) {
                        var opt = $('<option>').text(x['state_name'])
                            .attr('value', x['id']);
                        selectstate.append(opt);
                    });
                }
            });
        });

        $('#state_id, #country_id').change(function() {
            var country_id = $('#country_id').val()
            var state_id = $('#state_id').val()
            var city_id
            if ($('#selected_city').length && $('#selected_city').val()) {
                var city_id = $('#selected_city').val()
            }
            if (country_id && state_id) {
                ajax.jsonRpc("/get_cities", 'call', {
                    'country_id': country_id,
                    'state_id': state_id,
                }).then(function(data) {
                    var selectcity = $('#city_id');
                    selectcity.empty();
                    if (data.length) {
                        selectcity.append("<option value=''>Select City...</option>")
                        _.each(data, function(x) {
                            if (city_id == x['id']) {
                                var opt = $('<option>').text(x['city_name'])
                                    .attr({
                                        'value': x['id'],
                                        'selected': true
                                    });
                                selectcity.append(opt);
                            } else {
                                var opt = $('<option>').text(x['city_name'])
                                    .attr('value', x['id']);
                                selectcity.append(opt);
                            }
                        });
                    }
                });
            }
            if ($('#state_id').parent()[0]) {
                setTimeout(function() {
                    var temp = $('#state_id').parent()[0]
                    $(temp).css('display', 'block')
                }, 500);
            }
        });

        if ($('#state_id').length || $('#country_id').length) {
            var country_id = $('#country_id').val()
            var state_id = $('#state_id').val()
            var city_id
            if ($('#selected_city').length && $('#selected_city').val()) {
                var city_id = $('#selected_city').val()
            }
            if (country_id && state_id) {
                ajax.jsonRpc("/get_cities", 'call', {
                    'country_id': country_id,
                    'state_id': state_id,
                }).then(function(data) {
                    var selectcity = $('#city_id');
                    selectcity.empty();
                    if (data.length) {
                        selectcity.append("<option value=''>Select City...</option>")
                        _.each(data, function(x) {

                            if (city_id == x['id']) {
                                var opt = $('<option>').text(x['city_name'])
                                    .attr({
                                        'value': x['id'],
                                        'selected': true
                                    });
                                selectcity.append(opt);
                            } else {
                                var opt = $('<option>').text(x['city_name'])
                                    .attr('value', x['id']);
                                selectcity.append(opt);
                            }
                        });
                    }
                });
            }
        }
        if ($('#state_id').parent()[0]) {
            setTimeout(function() {
                var temp = $('#state_id').parent()[0]
                $(temp).css('display', 'block')
            }, 500);
        }

        $('.payable_amount').change(function(ev) {
            if (parseFloat(ev.target.value) > parseFloat(ev.target.max)) {
               ev.target.value = ev.target.max
            } else if (parseFloat(ev.target.value) < parseFloat(ev.target.min)) {
               ev.target.value = ev.target.min
            }
             var total_amount = $('.order_total_value')[0].value
             if ($('.remaining_amount').length) {
                 for (var rec of $('.remaining_amount')) {
                    var remaining = '₹ ' + ((total_amount - ev.target.value).toFixed(2) || "0.00");
                    rec.innerText = remaining;
                 }
            }
        });

        if (window.location.pathname == '/shop/payment' && $('.amount_of_payable').length > 0) {
            for(var rec of $('.amount_of_payable')){
                $(rec).removeClass('d-none')
            }
            for(var rec of $('.remaining_of_payable')){
                $(rec).removeClass('d-none')
            }
        }

        let recentFileUrl = null; // To store the blob URL of the updated file

        // Trigger the file input when Edit is clicked
        $('.gst_edit').on("click", function (ev) {
            $('.new_gst_file').trigger('click');
        });

        // Handle file selection and validation
        $('.new_gst_file').on('change', function () {
            const fileInput = $('.new_gst_file')[0]; // Access the actual file input element
            const fileName = fileInput.value.toLowerCase();
            const allowedExtensions = ['pdf'];
            const fileExtension = fileName.split('.').pop();

            // Validate file extension
            if (!allowedExtensions.includes(fileExtension)) {
                alert('Only PDF files are allowed.');
                $(fileInput).val(''); // Clear the file input
                return;
            }

            // Update the UI to show Save/Cancel buttons and "Edit" status
            $('.custom-uploaded').addClass('d-none');
            $('.custom-edit').removeClass('d-none');
            $('.gst-actions').show(); // Show Save and Cancel buttons
            $('.custom-save-icon').removeClass('d-none'); // Show Save icon
            $('.custom-delete-icon').removeClass('d-none'); // Show Delete icon
            $('.custom-inactive-gst').addClass('d-none');
    //        $('.custom-view-btn').addClass('d-none'); // Hide View button
            $('.gst_edit').addClass('d-none'); // Hide View button
            $('.gst-view').addClass('d-none'); // Hide View button

            // Create a blob URL for the selected file
            const file = fileInput.files[0];
            if (file) {
                if (recentFileUrl) {
                    URL.revokeObjectURL(recentFileUrl); // Revoke the previous blob URL
                }
                recentFileUrl = URL.createObjectURL(file); // Create a new blob URL
            }
        });

        // Save button functionality
        $('.gst-save').on("click", function (ev) {
            ev.preventDefault(); // Prevent default button behavior

            // Show a loading spinner and submit the form
            $.blockUI({
                'message': '<h4 class="text-white"><img src="/web/static/img/spin.png" class="fa-pulse"/>' +
                    '    <br />' + 'Please Wait....' +
                    '</h4>'
            });
            $('#upload_gst_certificate').submit(); // Submit the form
        });

        // Cancel button functionality
        $('.gst-cancel').on("click", function (ev) {
            ev.preventDefault(); // Prevent default button behavior

            // Reset the file input and hide Save/Cancel buttons
            $('.new_gst_file').val(''); // Clear the selected file
            $('.gst-actions').hide(); // Hide Save and Cancel buttons
            $('.custom-uploaded').addClass('d-none');
            $('.custom-edit').removeClass('d-none');
            $('.gst-actions').hide(); // Hide Save and Cancel buttons
            $('.custom-save-icon').addClass('d-none'); // Hide Save icon
            $('.custom-delete-icon').addClass('d-none'); // Hide Delete icon
            $('.custom-view-btn').removeClass('d-none'); // Show View button
            $('.custom-uploaded').removeClass('d-none');
            $('.custom-edit').addClass('d-none');

            // Revoke the recent file URL if it exists
            if (recentFileUrl) {
                URL.revokeObjectURL(recentFileUrl);
                recentFileUrl = null;
            }
        });


        // Save icon functionality (Download the recent file)
        $('.custom-delete-icon').on('click', function () {
            $('.gst-cancel').click();
        })
        $('.custom-save-icon').on('click', function () {
            if (recentFileUrl) {
                const downloadLink = document.createElement('a');
                downloadLink.href = recentFileUrl; // Use the recent file URL
                downloadLink.target = '_blank';
                downloadLink.download = $('.new_gst_file')[0].files[0]?.name || 'download.pdf'; // Use the file's name or default to 'download.pdf'
                document.body.appendChild(downloadLink);
                downloadLink.click();
                document.body.removeChild(downloadLink);
            } else {
                alert('No recent file available for download.');
            }
        });
        $('.portal_payable_amount').on('change', function (ev) {
            let value_payable = parseFloat($(this).val());
            const min = parseFloat($(this).attr('min'));
            const max = parseFloat($(this).attr('max'));
            if (value_payable < min) {
                value_payable = min;
                $(this).val(min);
            }
            if (value_payable > max) {
                value_payable = max;
                $(this).val(max);
            }
        });

    });
});