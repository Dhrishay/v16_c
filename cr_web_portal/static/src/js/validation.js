odoo.define('cr_web_portal.input_validation', function (require) {
'use strict';

    $(document).ready(function(){

        $(".read-description-more").on('click',function(event){
            var target = $(event.currentTarget.previousElementSibling)
            if(target.hasClass('description-more')){
                target.removeClass('description-more')
                event.currentTarget.innerText = 'Read more...'

            }else{
                target.addClass('description-more')
                event.currentTarget.innerText = 'Read less...'
    
            }
        });
        function is_service_product_checked(){
            var is_service_product_checked = false;
            var check_boxes = $('.is_service_product_checked');
            for(var i=0; i<check_boxes.length; i++){
                if(check_boxes[i].checked){
                    is_service_product_checked = true;
                }
            }
            return is_service_product_checked;
        }
         function check_email(){
            var email = $("#contact_us_emai_checking")[0].value;
            var emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

            if (!emailRegex.test(email) && email.length >= 1) {
               return false;
            }
            else{
                if($('.pbmit-btn').attr("disabled") != 'false' && is_service_product_checked() && emailRegex.test(email)){
                      return true;
                }
            }

        }

     $(".check_email").blur(function() {
        var email = event.target.value;
        var emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        var len_email = $(".check_email")[0].value.length
        if (!emailRegex.test(email) && len_email >= 1) {
           $(".pbmit-btn").attr('disabled', true);
           $(".email-validate-message").removeClass('d-none')
           $(".email-validate-message")[0].childNodes[1].innerText = 'Please enter a valid email address (e.g.sales@mechpowertech.com).';
           if($("form.industry_segment_validation").length > 0){
                if($("form.industry_segment_validation").find('.pbmit-btn').length > 0){
                    $("form.industry_segment_validation").find('.pbmit-btn')[0].classList.remove('industry_segment_btn');
                }
             }
        }
        else{
             $(".pbmit-btn").attr('disabled', false);
             $(".email-validate-message").addClass('d-none')
             $(".email-validate-message")[0].childNodes[1].innerText = '';
             if($("form.industry_segment_validation").length > 0){
                if($("form.industry_segment_validation").find('.pbmit-btn').length > 0){
                    $("form.industry_segment_validation").find('.pbmit-btn')[0].classList.add('industry_segment_btn');
                }
             }
        }
    });

     $(".contact_us_check_email").blur(function() {
        var email = event.target.value;
        var emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

        if (!emailRegex.test(email) && email.length >= 1) {
            if($('#contactUsSubmitBtn').attr("disabled") != 'true'){
                $('#pbmit-btn').attr("disabled",true);
            }
           $(".email-validate-message").removeClass('d-none')
           $(".email-validate-message")[0].childNodes[1].innerText = 'Please enter a valid email address (e.g. sales@mechpowertech.com).';
        }
        else{
            if($('#contactUsSubmitBtn').attr("disabled") != 'false' && is_service_product_checked()){
                $('#contactUsSubmitBtn').attr('disabled', false);
            }else{
                $('#contactUsSubmitBtn').attr("disabled",true);
            }
             $(".email-validate-message").addClass('d-none')
             $(".email-validate-message")[0].childNodes[1].innerText = '';

        }
    });

    $(".is_service_product_checked").change(function() {
        if($('#contactUsSubmitBtn').attr("disabled") != 'false' && is_service_product_checked() && check_email()){
            $('#contactUsSubmitBtn').attr('disabled', false);
        }else{
           $('#contactUsSubmitBtn').attr('disabled', true);
        }
    });

//    $(".mp_input_field_web .form_label").on('click',function(e){
//        e.currentTarget.previousElementSibling.focus();
//    });

    $(".change_input").change(function() {
        var input_val = $('.change_input').val()
        if (input_val == 'Company' ||input_val == 'Educational_Institution' ||input_val == 'Government_Organisation' ){
            $('.company-name').attr("required", true);
            $('.partner-name').attr("required", false);
        }
        else{
            $('.company-name').attr("required", false);
            $('.partner-name').attr("required", true);
        }
    });

    $(".check-file-type_one").change(function(){
        var input_values = $('.check-file-type_one').val()
        var input_val = input_values.toLowerCase()
        var ext = input_val.split(".");
        var arrayExtensions = ["stl","step", "stp", "zip"];
        var ext_1 = ext[ext.length - 1]

        if (! arrayExtensions.includes(ext_1)) {
            if($(".add-dyn-text").length > 0){
                $('.warning-modal h5')[0].innerText = 'Please upload a valid file.';
                    $('.warning-modal').removeClass('d-none');
            }
            $(".check-file-type_one").val("");
            if($("form.industry_segment_validation").length > 0){
                if($("form.industry_segment_validation").find('.pbmit-btn').length > 0){
                    $("form.industry_segment_validation").find('.pbmit-btn')[0].classList.remove('industry_segment_btn');
                }
            }
        }
        else{
            if($(".add-dyn-text").length > 0){
                $(".add-dyn-text")[0].childNodes[1].innerText = '';
            }
            if($("form.industry_segment_validation").length > 0){
                if($("form.industry_segment_validation").find('.pbmit-btn').length > 0){
                    $("form.industry_segment_validation").find('.pbmit-btn')[0].classList.add('industry_segment_btn');
                }
             }
        }

    });

    $(".check-file-type_uv").change(function(){
        var input_values = $('.check-file-type_uv').val()
        var input_val = input_values.toLowerCase()
        var ext = input_val.split(".");
        var arrayExtensions = ["tiff","png", "jpeg", "jpg","pdf"];
        var ext_1 = ext[ext.length - 1]
        if (! arrayExtensions.includes(ext_1)) {
            if($(".add-dyn-text-uv").length > 0){
                $('.warning-modal h5')[0].innerText = 'Please upload a valid file.';
                $('.warning-modal').removeClass('d-none');
            }
            $(".check-file-type_uv").val("");
            if($("form.industry_segment_validation").length > 0){
                if($("form.industry_segment_validation").find('.pbmit-btn').length > 0){
                    $("form.industry_segment_validation").find('.pbmit-btn')[0].classList.remove('industry_segment_btn');
                }
             }
        }
        else{
            if($(".add-dyn-text-uv").length > 0){
                $(".add-dyn-text-uv")[0].childNodes[1].innerText = '';
            }
            if($("form.industry_segment_validation").length > 0){
                if($("form.industry_segment_validation").find('.pbmit-btn').length > 0){
                    $("form.industry_segment_validation").find('.pbmit-btn')[0].classList.add('industry_segment_btn');
                }
             }
        }

    });
    $(".o_password_show_div").click(function(e){
        var target = $(this).siblings()[0]
        if (target.type == 'password'){
            target.type = 'text';
            $(this)[0].innerHTML = `<i class="fa fa-eye o_password_show_div_i"/>`
        }
        else{
            target.type = 'password';
            $(this)[0].innerHTML = `<i class="fa fa-eye-slash o_password_show_div_i"/>`
        }

    });
    $(".check-file-type_two").change(function(){
        var input_values = $('.check-file-type_two').val()
        var input_val = input_values.toLowerCase()
        var ext = input_val.split(".");
        var arrayExtensions = ["zip","dxf", "dwg", "step","stp","iges","sldprt","pdf"];
        var ext_1 = ext[ext.length - 1]

        if (! arrayExtensions.includes(ext_1)) {
            $(".email-validate-message").removeClass('d-none')
            if($(".add-dyn-text").length > 0){
                $(".add-dyn-text")[0].childNodes[1].innerText = 'Please upload a valid file.';
            }
            $(".check-file-type_two").val("");
            if($("form.industry_segment_validation").length > 0){
                if($("form.industry_segment_validation").find('.pbmit-btn').length > 0){
                    $("form.industry_segment_validation").find('.pbmit-btn')[0].classList.remove('industry_segment_btn');
                }
             }
        }
        else{
            if($(".add-dyn-text").length > 0){
                $(".add-dyn-text")[0].childNodes[1].innerText = '';
            }
            if($("form.industry_segment_validation").length > 0){
                if($("form.industry_segment_validation").find('.pbmit-btn').length > 0){
                    $("form.industry_segment_validation").find('.pbmit-btn')[0].classList.add('industry_segment_btn');
                }
             }
        }
    });

     $(".check-file-type-extra").change(function(){
        var input_values = $('.check-file-type-extra').val()
        var input_val = input_values.toLowerCase()
        var ext = input_val.split(".");
        var arrayExtensions = ["zip","stl", "step", "stp","stp","obj","3MF","pdf","zip","dxf","dwg","iges","sldprt"];
        var ext_1 = ext[ext.length - 1]

        if (! arrayExtensions.includes(ext_1)) {
            if($(".add-dyn-text").length > 0){
                $('.warning-modal h5')[0].innerText = 'Please upload a valid file.';
                $('.warning-modal').removeClass('d-none');
            }
            $(".check-file-type-extra").val("");
            if($("form.industry_segment_validation").length > 0){
                if($("form.industry_segment_validation").find('.pbmit-btn').length > 0){
                    $("form.industry_segment_validation").find('.pbmit-btn')[0].classList.remove('industry_segment_btn');
                }
             }
        }
        else{
            if($(".add-dyn-text").length > 0){
                $(".add-dyn-text")[0].childNodes[1].innerText = '';
            }
            if($("form.industry_segment_validation").length > 0){
                if($("form.industry_segment_validation").find('.pbmit-btn').length > 0){
                    $("form.industry_segment_validation").find('.pbmit-btn')[0].classList.add('industry_segment_btn');
                }
             }
        }
    });

    $(".registration_type_option").on('click',function() {
        if($(".registration_type_option").hasClass('active')){
            $(".registration_type_option").removeClass('active');
        }
        $(this).addClass('active');
        $('.onchange-registration-type').val($(this)[0].getAttribute('value'));

        if($(this)[0].getAttribute('value') == 'person'){
            $('#cname').attr("required", false);
            $('#name').attr("disabled",false);
            if(!$("label[for='name'").hasClass('o_input_required')){
                $("label[for='name'").addClass('o_input_required')
            }
            if($("label[for='cname'").hasClass('o_input_required')){
                $("label[for='cname'").removeClass('o_input_required')
            }
            $('#name').attr("required", true);
        }
        if($(this)[0].getAttribute('value') == 'company'){
            $('#cname').attr("disabled",false);
            $('#cname').attr("required", true);
            if(!$("label[for='cname'").hasClass('o_input_required')){
                $("label[for='cname'").addClass('o_input_required')
            }
            if($("label[for='name'").hasClass('o_input_required')){
                $("label[for='name'").removeClass('o_input_required')
            }
            $('#name').attr("required", false);
        }
    });

    $("#inquiry_as").change(function(e) {
        if($(this)[0].value == 'Individual'){
            $('#contact4').attr("required", false);
            $('#contact1').attr("disabled",false);
            if(!$("label[for='contact1'").hasClass('o_input_required')){
                $("label[for='contact1'").addClass('o_input_required')
            }
            if($("label[for='contact4'").hasClass('o_input_required')){
                $("label[for='contact4'").removeClass('o_input_required')
            }
            $('#contact1').attr("required", true);
        }
        if($(this)[0].value == 'Company'){
            $('#contact4').attr("disabled",false);
            $('#contact4').attr("required", true);
            if(!$("label[for='contact4'").hasClass('o_input_required')){
                $("label[for='contact4'").addClass('o_input_required')
            }
            if($("label[for='contact1'").hasClass('o_input_required')){
                $("label[for='contact1'").removeClass('o_input_required')
            }
            $('#contact1').attr("required", false);
        }
    });
    $(".lead_source_option").on('click',function() {
        if($(".lead_source_option").hasClass('active')){
            $(".lead_source_option").removeClass('active');
        }
        $(this).addClass('active');
        $('.lead_source_input').val($(this)[0].getAttribute('value'));
    });


    });
    $('.mp_o_switch').on('click', function(event) {
        if (event.currentTarget.firstElementChild.checked) {
            event.currentTarget.firstElementChild.checked = false;
        } else {
            event.currentTarget.firstElementChild.checked = true;
        }
    });

    function blogFilterApply(){
        var redirect_url = location.origin + '/blog';
        var blog_url = '';

        var blog_check_boxes = $('.blog_checkmark_onchange#u_blog_category');
        for(var i=0; i<blog_check_boxes.length; i++){
            if(blog_check_boxes[i].checked){
                if(blog_url.replace(location.origin + '/blog','') == ''){
                    blog_url = blog_url+'/'+blog_check_boxes[i].getAttribute('href')
                }else{
                    blog_url = blog_url+','+blog_check_boxes[i].getAttribute('href')
                }
            }
        }
        if(blog_url.replace(location.origin + '/blog','') != ''){
            redirect_url = redirect_url + blog_url
        }
        var tag_url = '/tag';

        var tag_check_boxes = $('.blog_checkmark_onchange#u_tag_category');
        for(var i=0; i<tag_check_boxes.length; i++){
            if(tag_check_boxes[i].checked){
                if(tag_url.replace('/tag','') == ''){
                    tag_url = tag_url+'/'+tag_check_boxes[i].getAttribute('href')
                }else{
                    tag_url = tag_url+','+tag_check_boxes[i].getAttribute('href')
                }
            }
        }
        if(tag_url.replace('/tag','') != ''){
            redirect_url = redirect_url + tag_url
        }

        window.location.href = redirect_url;
    }

    $('.blog_checkmark_onchange').change(function(e){
        if($('.blog-left-col').length && !$('.blog-left-col')[0].classList.contains('scrolled_up')){
            blogFilterApply();
        }
    });

    $('.blog_filter_apply_btn').on('click', function(e) {
        if($('.blog-left-col').length && $('.blog-left-col')[0].classList.contains('scrolled_up')){
            blogFilterApply();
        }
    });

});