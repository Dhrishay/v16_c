/** @odoo-module **/
import {
    session
} from "@web/session";
import ajax from 'web.ajax';
$(document).ready(function() {

    //  File Upload & Create Attachment and Set the Powerviz Url
    function fileUploadForPowerviz(e) {
        if (e.type == 'change') {
            var files = e.target.files
            if (files.length > 0) {
                var filename = files[0]['name']
                var parts = filename.split('.');
                var fileExtension = parts.length > 1 ? '.' + parts.pop() : '';
                var fileInput = $(e.currentTarget)
                var allowedExtension = $(fileInput).attr('accept').split(',').map(ext => ext.trim()).filter(ext => ext);
                if (allowedExtension.length) {
                    if ($('.loader-modal').length){
                        $('.loader-modal').removeClass('d-none')
                    ;}
                    var form = e.currentTarget.parentElement.parentElement.parentElement.parentElement
                    if (fileExtension.toLowerCase() == '.zip') {
                        if (form.hasAttribute('data-success-page')) {
                            form.setAttribute('data-success-page', '/');
                        }
                        if ($(form.parentElement.parentElement.nextElementSibling).find('.projectionSubmitBtn').length > 0) {
                            var btn = $(form.parentElement.parentElement.nextElementSibling).find('.projectionSubmitBtn')
                            btn[0].innerHTML = 'Submit Inquiry';
                            if (btn.hasClass('disabled')) {
                                btn.removeClass('disabled')
                            }
                            $('.projection-calculate-quote').addClass('disabled')
                        }
                        if ($(form.parentElement.parentElement.nextElementSibling).find('.fdmSubmitBtn').length > 0) {
                            var btn = $(form.parentElement.parentElement.nextElementSibling).find('.fdmSubmitBtn')
                            btn[0].innerHTML = 'Submit Inquiry';
                            if (btn.hasClass('disabled')) {
                                btn.removeClass('disabled')
                            }
                            $('.fdm-calculate-quote').addClass('disabled')
                        }
                    } else {
                        if (form.hasAttribute('data-success-page')) {
                            form.setAttribute('data-success-page', '/redirect-to-cart');
                        }
                        if ($(form.parentElement.parentElement.nextElementSibling).find('.fdmSubmitBtn').length > 0) {
                            var btn = $(form.parentElement.parentElement.nextElementSibling).find('.fdmSubmitBtn')
                            btn[0].innerHTML = 'Add to Cart';
                            if (!btn.hasClass('disabled')) {
                                btn.addClass('disabled')
                            }
                        }
                        if ($(form.parentElement.parentElement.nextElementSibling).find('.projectionSubmitBtn').length > 0) {
                            var btn = $(form.parentElement.parentElement.nextElementSibling).find('.projectionSubmitBtn')
                            btn[0].innerHTML = 'Add to Cart';
                            if (!btn.hasClass('disabled')) {
                                btn.addClass('disabled')
                            }
                        }
                    }
                    if (allowedExtension.includes(fileExtension.toLowerCase())) {
                        var filesizeInByte = files[0]['size']
                        var filesizedict = formatFileSize(filesizeInByte)
                        var fileSizeFormate = filesizedict.fileSizeFormate
                        var fileSize = filesizedict.fileSize
                        var dropEvent = e;
                        var fileUploading = e.currentTarget.parentElement.parentElement.nextElementSibling
                        var file_percentage;
                        var file_name;
                        var file_size_uploading;
                        if ($(fileUploading).find('.uploading-file-name')) {
                            file_name = $(fileUploading).find('.uploading-file-name')[0]
                            file_name.innerText = filename
                        }
                        if ($(fileUploading).find('.total-file-size')) {
                            $(fileUploading).find('.total-file-size')[0].innerText = " / " + fileSize
                        }
                        if ($(fileUploading).find('.file-size')) {
                            $(fileUploading).find('.file-size').each(function(i) {
                                $(fileUploading).find('.file-size')[i].innerText = " " + fileSizeFormate
                            });
                        }
                        if ($(fileUploading).find('.file-percentage')) {
                            file_percentage = $(fileUploading).find('.file-percentage')[0]
                        }
                        if ($(fileUploading).find('.file-size-uploading')) {
                            file_size_uploading = $(fileUploading).find('.file-size-uploading')[0]
                        }
                        if ($(fileUploading).find('.js-progress-bar')) {
                            $(fileUploading).find('.js-progress-bar').css('stroke-dashoffset', 99);
                        }
                        $(fileUploading).find('.file-uploading-completed-icon-box').addClass('d-none');
                        $(fileUploading).find('.file-uploading-progress-icon-box').removeClass('d-none');
                        $(fileUploading).find('.total-file-size').removeClass('d-none');
                        $(fileUploading).find('.file-uploaded-container-btn.mp-btn-light-border-green').addClass('d-none');
                        $(fileUploading.parentElement.parentElement).find('#form-bottom-powerviz').addClass('d-none').attr({
                            'href': ''
                        });
                        $(fileUploading).find('.mobile-file-uploaded-container-btn.mp-btn-light-border-green').attr({
                            'href': ''
                        });
                        $(fileUploading).find('.uploading-cancel-icon-box').css('margin-left', 'auto');
                        $(fileUploading).css('border-color', 'var(--mp-color-7)');
                        $(fileUploading).css('background-color', 'var(--mp-color-10)');
                        var reader = new FileReader();
                        reader.onprogress = function(event) {
                            $(fileUploading).removeClass('d-none');
                            $(dropEvent.currentTarget.parentElement.parentElement).addClass('d-none');
                            if (event.lengthComputable) {
                                var percentLoaded = (event.loaded / event.total) * 100;
                                file_percentage.innerText = Math.round(percentLoaded);
                                file_size_uploading.innerText = ((fileSize * percentLoaded) / 100).toFixed(2);
                                if ($(fileUploading).find('.js-progress-bar')) {
                                    $(fileUploading).find('.js-progress-bar').css('stroke-dashoffset', (100 - Math.round(percentLoaded.toFixed(2))));
                                }
                            }
                        };
                        reader.onloadend = function() {
                            var fileBase64String = reader.result;
                            if (!reader.result && $('.warning-modal h5')) {
                                $('.warning-modal h5')[0].innerText = 'Please upload a valid file.';
                                $('.warning-modal').removeClass('d-none');
                                return
                            }

                            fileBase64String = fileBase64String.split('base64,')[fileBase64String.split('base64,').length - 1];
                            var file_vals = {
                                'name': filename,
                                'mimetype': files[0].type,
                                'base64Data': fileBase64String,
                            }

                            $.ajax({
                                type: "POST",
                                dataType: 'json',
                                url: '/create/attachment/powerviz',
                                contentType: "application/json; charset=utf-8",
                                data: JSON.stringify({
                                    'jsonrpc': "2.0",
                                    'method': "call",
                                    "params": file_vals
                                }),
                                success: function(action) {
                                    if (action.result) {
                                        $(fileUploading).find('.file-uploading-completed-icon-box').removeClass('d-none');
                                        $(fileUploading).find('.file-uploading-progress-icon-box').addClass('d-none');
                                        $(fileUploading).find('.total-file-size').addClass('d-none');
                                        $(fileUploading).find('.file-size')[0].innerText = ''
                                        $(fileUploading).css('border-color', 'var(--mp-color-dark-6)');
                                        $(fileUploading).css('background-color', '#fff');

                                        if (fileExtension.toLowerCase() != '.zip') {
                                            $(fileUploading).find('.uploading-cancel-icon-box').css('margin-left', '24px');
                                            $(fileUploading).find('.mobile-file-uploaded-container-btn.mp-btn-light-border-green').attr({
                                                'href': action.result,
                                                target: '_blank'
                                            });
                                            $(fileUploading).find('.file-uploaded-container-btn.mp-btn-light-border-green').attr({
                                                'href': action.result,
                                                target: '_blank'
                                            }).removeClass('d-none');
                                            $(fileUploading.parentElement.parentElement).find('#form-bottom-powerviz').attr({
                                                'href': action.result,
                                                target: '_blank'
                                            }).removeClass('d-none');
                                            if ($(fileUploading.parentElement.parentElement).find('.projection-calculate-quote') && $(fileUploading.parentElement.parentElement).find('.projection-calculate-quote').hasClass('disabled')) {
                                                $(fileUploading.parentElement.parentElement).find('.projection-calculate-quote').removeClass('disabled')
                                            }
//                                            else if ($(fileUploading.parentElement.parentElement).find('.projection-calculate-quote') && !$(fileUploading.parentElement.parentElement).find('.projection-calculate-quote').hasClass('disabled')) {
//                                                $(fileUploading.parentElement.parentElement).find('.projection-calculate-quote').addClass('disabled')
//                                            }
                                            if ($(fileUploading.parentElement.parentElement).find('.fdm-calculate-quote') && $(fileUploading.parentElement.parentElement).find('.fdm-calculate-quote').hasClass('disabled')) {
                                                $(fileUploading.parentElement.parentElement).find('.fdm-calculate-quote').removeClass('disabled')
                                            }
//                                            else if ($(fileUploading.parentElement.parentElement).find('.fdm-calculate-quote') && !$(fileUploading.parentElement.parentElement).find('.fdm-calculate-quote').hasClass('disabled')) {
//                                                $(fileUploading.parentElement.parentElement).find('.fdm-calculate-quote').addClass('disabled')
//                                            }
                                            $(fileUploading.parentElement.parentElement).find('.s_website_form_submit .mp-btn-light-green').click()
                                        }
                                    } else {
                                        console.log(action)
                                    }
                                },
                            });
                        };
                        reader.readAsDataURL(files[0]);
                    } else {
                        if ($('.warning-modal h5')) {
                            $('.warning-modal h5')[0].innerText = 'Please upload a valid file.';
                            $('.warning-modal').removeClass('d-none');
                        }
                    }
                }
            }
        } else {
            var files = e.originalEvent.dataTransfer.files
            var filename = files[0]['name']
            var parts = filename.split('.');
            var fileExtension = parts.length > 1 ? '.' + parts.pop() : '';
            var fileInput = $(e.currentTarget).find('input[type="file"]')
            if (!$(fileInput)[0].disabled) {
                var allowedExtension = $(fileInput).attr('accept').split(',').map(ext => ext.trim()).filter(ext => ext);
                if (allowedExtension.length) {
                    var form = e.currentTarget.parentElement.parentElement.parentElement.parentElement
                    if (fileExtension.toLowerCase() == '.zip') {
                        if (form.hasAttribute('data-success-page')) {
                            form.setAttribute('data-success-page', '/');
                        }
                        if ($(form.parentElement.nextElementSibling).find('.projectionSubmitBtn').length > 0) {
                            var btn = $(form.parentElement.nextElementSibling).find('.projectionSubmitBtn')
                            btn[0].innerHTML = 'Submit Inquiry';
                            if (btn.hasClass('disabled')) {
                                btn.removeClass('disabled')
                            }
                            $('.projection-calculate-quote').addClass('disabled')
                        }
                        if ($(form.parentElement.nextElementSibling).find('.fdmSubmitBtn').length > 0) {
                            var btn = $(form.parentElement.nextElementSibling).find('.fdmSubmitBtn')
                            btn[0].innerHTML = 'Submit Inquiry';
                            if (btn.hasClass('disabled')) {
                                btn.removeClass('disabled')
                            }
                            $('.fdm-calculate-quote').addClass('disabled')
                        }
                    } else {
                        if (form.hasAttribute('data-success-page')) {
                            form.setAttribute('data-success-page', '/redirect-to-cart');
                        }
                        if ($(form.parentElement.parentElement.nextElementSibling).find('.fdmSubmitBtn').length > 0) {
                            var btn = $(form.parentElement.parentElement.nextElementSibling).find('.fdmSubmitBtn')
                            btn[0].innerHTML = 'Add to Cart';
                            if (!btn.hasClass('disabled')) {
                                btn.addClass('disabled')
                            }
                        }
                        if ($(form.parentElement.parentElement.nextElementSibling).find('.projectionSubmitBtn').length > 0) {
                            var btn = $(form.parentElement.parentElement.nextElementSibling).find('.projectionSubmitBtn')
                            btn[0].innerHTML = 'Add to Cart';
                            if (!btn.hasClass('disabled')) {
                                btn.addClass('disabled')
                            }
                        }
                    }
                    if (allowedExtension.includes(fileExtension.toLowerCase())) {
                        var filesizeInByte = files[0]['size']
                        var filesizedict = formatFileSize(filesizeInByte)
                        var fileSizeFormate = filesizedict.fileSizeFormate
                        var fileSize = filesizedict.fileSize
                        var dropEvent = e;
                        var fileUploading = dropEvent.currentTarget.nextElementSibling
                        var file_percentage;
                        var file_name;
                        var file_size_uploading;
                        if ($(fileUploading).find('.uploading-file-name')) {
                            file_name = $(fileUploading).find('.uploading-file-name')[0]
                            file_name.innerText = filename
                        }
                        if ($(fileUploading).find('.total-file-size')) {
                            $(fileUploading).find('.total-file-size')[0].innerText = " / " + fileSize
                        }
                        if ($(fileUploading).find('.file-size')) {
                            $(fileUploading).find('.file-size').each(function(i) {
                                $(fileUploading).find('.file-size')[i].innerText = " " + fileSizeFormate
                            });
                        }
                        if ($(fileUploading).find('.file-percentage')) {
                            file_percentage = $(fileUploading).find('.file-percentage')[0]
                        }
                        if ($(fileUploading).find('.file-size-uploading')) {
                            file_size_uploading = $(fileUploading).find('.file-size-uploading')[0]
                        }
                        if ($(fileUploading).find('.js-progress-bar')) {
                            $(fileUploading).find('.js-progress-bar').css('stroke-dashoffset', 99);
                        }
                        $(fileUploading).find('.file-uploading-completed-icon-box').addClass('d-none');
                        $(fileUploading).find('.file-uploading-progress-icon-box').removeClass('d-none');
                        $(fileUploading).find('.total-file-size').removeClass('d-none');
                        $(fileUploading).find('.file-uploaded-container-btn.mp-btn-light-border-green').addClass('d-none').attr({
                            'href': ''
                        });
                        $(fileUploading.parentElement.parentElement).find('#form-bottom-powerviz').addClass('d-none').attr({
                            'href': ''
                        });
                        $(fileUploading).find('.mobile-file-uploaded-container-btn.mp-btn-light-border-green').attr({
                            'href': ''
                        });
                        $(fileUploading).find('.uploading-cancel-icon-box').css('margin-left', 'auto');
                        $(fileUploading).css('border-color', 'var(--mp-color-7)');
                        $(fileUploading).css('background-color', 'var(--mp-color-10)');
                        var reader = new FileReader();
                        reader.onprogress = function(event) {
                            $(fileUploading).removeClass('d-none');
                            $(dropEvent.currentTarget).addClass('d-none');
                            if (event.lengthComputable) {
                                var percentLoaded = (event.loaded / event.total) * 100;
                                file_percentage.innerText = Math.round(percentLoaded);
                                file_size_uploading.innerText = ((fileSize * percentLoaded) / 100).toFixed(2);
                                if ($(fileUploading).find('.js-progress-bar')) {
                                    $(fileUploading).find('.js-progress-bar').css('stroke-dashoffset', (100 - Math.round(percentLoaded.toFixed(2))));
                                }
                            }
                        };
                        reader.onloadend = function() {
                            var fileBase64String = reader.result;
                            fileBase64String = fileBase64String.split('base64,')[fileBase64String.split('base64,').length - 1];
                            if (!reader.result && $('.warning-modal h5')) {
                                $('.warning-modal h5')[0].innerText = 'Please upload a valid file.';
                                $('.warning-modal').removeClass('d-none');
                                return
                            }
                            var file_vals = {
                                'name': filename,
                                'mimetype': files[0].type,
                                'base64Data': fileBase64String,
                            }
                            $.ajax({
                                type: "POST",
                                dataType: 'json',
                                url: '/create/attachment/powerviz',
                                contentType: "application/json; charset=utf-8",
                                data: JSON.stringify({
                                    'jsonrpc': "2.0",
                                    'method': "call",
                                    "params": file_vals
                                }),
                                success: function(action) {
                                    if (action.result) {
                                        $(fileUploading).find('.file-uploading-completed-icon-box').removeClass('d-none');
                                        $(fileUploading).find('.file-uploading-progress-icon-box').addClass('d-none');
                                        $(fileUploading).find('.total-file-size').addClass('d-none');
                                        $(fileUploading).find('.file-size')[0].innerText = ''
                                        $(fileUploading).css('border-color', 'var(--mp-color-dark-6)');
                                        $(fileUploading).css('background-color', '#fff');


                                        fileInput.prop('files', files);
                                        if (fileExtension.toLowerCase() != '.zip') {
                                            $(fileUploading.parentElement.parentElement).find('#form-bottom-powerviz').attr({
                                                'href': action.result,
                                                target: '_blank'
                                            }).removeClass('d-none');

                                            $(fileUploading).find('.uploading-cancel-icon-box').css('margin-left', '24px');
                                            $(fileUploading).find('.file-uploaded-container-btn.mp-btn-light-border-green').attr({
                                                'href': action.result,
                                                target: '_blank'
                                            }).removeClass('d-none');
                                            $(fileUploading).find('.mobile-file-uploaded-container-btn.mp-btn-light-border-green').attr({
                                                'href': action.result,
                                                target: '_blank'
                                            })
                                            if ($(fileUploading.parentElement.parentElement).find('.fdm-calculate-quote') && $(fileUploading.parentElement.parentElement).find('.fdm-calculate-quote').hasClass('disabled')) {
                                                $(fileUploading.parentElement.parentElement).find('.fdm-calculate-quote').removeClass('disabled')
                                            }
//                                            else if ($(fileUploading.parentElement.parentElement).find('.fdm-calculate-quote') && !$(fileUploading.parentElement.parentElement).find('.fdm-calculate-quote').hasClass('disabled')) {
//                                                $(fileUploading.parentElement.parentElement).find('.fdm-calculate-quote').addClass('disabled')
//                                            }
                                            if ($(fileUploading.parentElement.parentElement).find('.projection-calculate-quote') && $(fileUploading.parentElement.parentElement).find('.projection-calculate-quote').hasClass('disabled')) {
                                                $(fileUploading.parentElement.parentElement).find('.projection-calculate-quote').removeClass('disabled')
                                            }
//                                            else if ($(fileUploading.parentElement.parentElement).find('.projection-calculate-quote') && !$(fileUploading.parentElement.parentElement).find('.projection-calculate-quote').hasClass('disabled')) {
//                                                $(fileUploading.parentElement.parentElement).find('.projection-calculate-quote').addClass('disabled')
//                                            }
                                        }
                                    } else {
                                        console.log(action)
                                    }
                                },
                            });
                        };
                        reader.readAsDataURL(files[0]);
                    } else {
                        if ($('.warning-modal h5')) {
                            $('.warning-modal h5')[0].innerText = 'Please upload a valid file.';
                            $('.warning-modal').removeClass('d-none');
                        }
                    }
                }
            } else {
                if ($('.warning-modal h5')) {
                    $('.warning-modal h5')[0].innerText = 'You can not upload file here.';
                    $('.warning-modal').removeClass('d-none');
                }
            }
        }
    }

    // Upload File Function
    function fileUpload(e) {
        if (e.type == 'change') {
            var AllowNext = true;
            var files = e.target.files
            if (e.target.id === 'input_technical_drawing' || e.target.id === 'input_uv_printing') {
                if (files[0]['size'] > 10000000) {
                    $('.warning-modal h5')[0].innerText = 'Please upload a valid file.';
                    $('.warning-modal').removeClass('d-none');
                    var AllowNext = false;
                }
            }
            if (files.length > 0 && AllowNext == true) {
                var filename = files[0]['name']
                var parts = filename.split('.');
                var fileExtension = parts.length > 1 ? '.' + parts.pop() : '';
                var fileInput = $(e.currentTarget)
                var allowedExtension = $(fileInput).attr('accept').split(',').map(ext => ext.trim()).filter(ext => ext);
                if (allowedExtension.length) {
                    if (allowedExtension.includes(fileExtension.toLowerCase())) {
                        var filesizeInByte = files[0]['size']
                        var filesizedict = formatFileSize(filesizeInByte)
                        var fileSizeFormate = filesizedict.fileSizeFormate
                        var fileSize = filesizedict.fileSize
                        var dropEvent = e;
                        var fileUploading = e.currentTarget.parentElement.parentElement.nextElementSibling
                        var file_percentage;
                        var file_name;
                        var file_size_uploading;
                        if ($(fileUploading).find('.uploading-file-name')) {
                            file_name = $(fileUploading).find('.uploading-file-name')[0]
                            file_name.innerText = filename
                        }
                        if ($(fileUploading).find('.total-file-size')) {
                            $(fileUploading).find('.total-file-size')[0].innerText = " / " + fileSize
                        }
                        if ($(fileUploading).find('.file-size')) {
                            $(fileUploading).find('.file-size').each(function(i) {
                                $(fileUploading).find('.file-size')[i].innerText = " " + fileSizeFormate
                            });
                        }
                        if ($(fileUploading).find('.file-percentage')) {
                            file_percentage = $(fileUploading).find('.file-percentage')[0]
                        }
                        if ($(fileUploading).find('.file-size-uploading')) {
                            file_size_uploading = $(fileUploading).find('.file-size-uploading')[0]
                        }
                        if ($(fileUploading).find('.js-progress-bar')) {
                            $(fileUploading).find('.js-progress-bar').css('stroke-dashoffset', 99);
                        }
                        $(fileUploading).find('.file-uploading-completed-icon-box').addClass('d-none');
                        $(fileUploading).find('.file-uploading-progress-icon-box').removeClass('d-none');
                        $(fileUploading).find('.total-file-size').removeClass('d-none');
                        $(fileUploading).css('border-color', 'var(--mp-color-7)');
                        $(fileUploading).css('background-color', 'var(--mp-color-10)');
                        var reader = new FileReader();
                        reader.onprogress = function(event) {
                            $(fileUploading).removeClass('d-none');
                            $(dropEvent.currentTarget.parentElement.parentElement).addClass('d-none');
                            if (event.lengthComputable) {
                                var percentLoaded = (event.loaded / event.total) * 100;
                                file_percentage.innerText = Math.round(percentLoaded);
                                file_size_uploading.innerText = ((fileSize * percentLoaded) / 100).toFixed(2);
                                if ($(fileUploading).find('.js-progress-bar')) {
                                    $(fileUploading).find('.js-progress-bar').css('stroke-dashoffset', (100 - Math.round(percentLoaded.toFixed(2))));
                                }
                                if (Math.round(percentLoaded) == 100) {
                                    $(fileUploading).find('.file-uploading-completed-icon-box').removeClass('d-none');
                                    $(fileUploading).find('.file-uploading-progress-icon-box').addClass('d-none');
                                    $(fileUploading).find('.total-file-size').addClass('d-none');
                                    $(fileUploading).find('.file-size')[0].innerText = ''
                                    $(fileUploading).css('border-color', 'var(--mp-color-dark-6)');
                                    $(fileUploading).css('background-color', '#fff');
                                }
                            }
                        };
                        reader.onloadend = function() {};
                        reader.readAsDataURL(files[0]);
                    } else {
                        if ($('.warning-modal h5')) {
                            $('.warning-modal h5')[0].innerText = 'Please upload a valid file.';
                            $('.warning-modal').removeClass('d-none');
                        }
                    }
                }
            }
        } else {
            var files = e.originalEvent.dataTransfer.files
            var filename = files[0]['name']
            var parts = filename.split('.');
            var fileExtension = parts.length > 1 ? '.' + parts.pop() : '';
            var fileInput = $(e.currentTarget).find('input[type="file"]')
            if (!$(fileInput)[0].disabled) {
                var allowedExtension = $(fileInput).attr('accept').split(',').map(ext => ext.trim()).filter(ext => ext);
                if (allowedExtension.length) {
                    if (allowedExtension.includes(fileExtension.toLowerCase())) {
                        var filesizeInByte = files[0]['size']
                        var filesizedict = formatFileSize(filesizeInByte)
                        var fileSizeFormate = filesizedict.fileSizeFormate
                        var fileSize = filesizedict.fileSize
                        var dropEvent = e;
                        var fileUploading = dropEvent.currentTarget.nextElementSibling
                        var file_percentage;
                        var file_name;
                        var file_size_uploading;
                        if ($(fileUploading).find('.uploading-file-name')) {
                            file_name = $(fileUploading).find('.uploading-file-name')[0]
                            file_name.innerText = filename
                        }
                        if ($(fileUploading).find('.total-file-size')) {
                            $(fileUploading).find('.total-file-size')[0].innerText = " / " + fileSize
                        }
                        if ($(fileUploading).find('.file-size')) {
                            $(fileUploading).find('.file-size').each(function(i) {
                                $(fileUploading).find('.file-size')[i].innerText = " " + fileSizeFormate
                            });
                        }
                        if ($(fileUploading).find('.file-percentage')) {
                            file_percentage = $(fileUploading).find('.file-percentage')[0]
                        }
                        if ($(fileUploading).find('.file-size-uploading')) {
                            file_size_uploading = $(fileUploading).find('.file-size-uploading')[0]
                        }
                        if ($(fileUploading).find('.js-progress-bar')) {
                            $(fileUploading).find('.js-progress-bar').css('stroke-dashoffset', 99);
                        }
                        $(fileUploading).find('.file-uploading-completed-icon-box').addClass('d-none');
                        $(fileUploading).find('.file-uploading-progress-icon-box').removeClass('d-none');
                        $(fileUploading).find('.total-file-size').removeClass('d-none');
                        $(fileUploading).css('border-color', 'var(--mp-color-7)');
                        $(fileUploading).css('background-color', 'var(--mp-color-10)');
                        var reader = new FileReader();
                        reader.onprogress = function(event) {
                            $(fileUploading).removeClass('d-none');
                            $(dropEvent.currentTarget).addClass('d-none');
                            if (event.lengthComputable) {
                                var percentLoaded = (event.loaded / event.total) * 100;
                                file_percentage.innerText = Math.round(percentLoaded);
                                file_size_uploading.innerText = ((fileSize * percentLoaded) / 100).toFixed(2);
                                if ($(fileUploading).find('.js-progress-bar')) {
                                    $(fileUploading).find('.js-progress-bar').css('stroke-dashoffset', (100 - Math.round(percentLoaded.toFixed(2))));
                                }
                                if (Math.round(percentLoaded) == 100) {
                                    $(fileUploading).find('.file-uploading-completed-icon-box').removeClass('d-none');
                                    $(fileUploading).find('.file-uploading-progress-icon-box').addClass('d-none');
                                    $(fileUploading).find('.total-file-size').addClass('d-none');
                                    $(fileUploading).find('.file-size')[0].innerText = ''
                                    $(fileUploading).css('border-color', 'var(--mp-color-dark-6)');
                                    $(fileUploading).css('background-color', '#fff');
                                }
                            }
                        };
                        reader.onloadend = function() {
                            fileInput.prop('files', files);
                        };
                        reader.readAsDataURL(files[0]);
                    } else {
                        if ($('.warning-modal h5')) {
                            $('.warning-modal h5')[0].innerText = 'Please upload a valid file.';
                            $('.warning-modal').removeClass('d-none');
                        }
                    }
                }
            } else {
                if ($('.warning-modal h5')) {
                    $('.warning-modal h5')[0].innerText = 'You can not upload file here.';
                    $('.warning-modal').removeClass('d-none');
                }
            }
        }
    }

    //  Get the File Formate
    function formatFileSize(bytes) {
        if (bytes === 0) return {
            'fileSize': 0,
            'fileSizeFormate': 'Bytes'
        };
        const k = 1024;
        const sizes = ['Bytes', 'KB', 'MB', 'GB', 'TB'];
        const i = Math.floor(Math.log(bytes) / Math.log(k));
        var size = {
            'fileSize': parseFloat((bytes / Math.pow(k, i)).toFixed(2)),
            'fileSizeFormate': sizes[i]
        }
        return size;
    }

    //  Check Required Fields are Properly Filled.
    function checkFields(forms) {
        var forms = forms
        var textarea_fields = $(forms).find('textarea.s_website_form_input')
        var input_fields = $(forms).find('input.s_website_form_input')
        var selection_fields = $(forms).find('select.s_website_form_input')
        var all_required_fields = []
        var all_required_fields_name = []
        if (textarea_fields.length > 0) {
            for (let i = 0; i < textarea_fields.length; i++) {
                if (textarea_fields[i].getAttribute('required') == 'required') {
                    all_required_fields.push(textarea_fields[i])
                }
            }
        }
        if (input_fields.length > 0) {
            for (let i = 0; i < input_fields.length; i++) {
                if (input_fields[i].getAttribute('required') == 'required') {
                    all_required_fields.push(input_fields[i])
                }
            }
        }
        if (selection_fields.length > 0) {
            for (let i = 0; i < selection_fields.length; i++) {
                if (selection_fields[i].getAttribute('required') == 'required') {
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
        all_required_fields.forEach(function (field) {
            var $field = $(field);
            var fieldValue = $field.val().trim();

            if (!fieldValue) {
                $field.css('border', '1px solid #F23C2F');
                all_required_fields_name.push($field[0].name)
            } else {
                $field.css('border', '');
            }
        });
        return {'is_required': require_field_is_empty, 'fields_name': all_required_fields_name};
    }

    $(document).on('input change', function (e) {
        if (e.target.value) {
            if($(e.target).hasClass('is-invalid')){
                $(e.target).removeClass('is-invalid')
            }
            else{
                $(e.target).css('border', ''); // Remove red border if input has a value
                if ($(e.target).attr('id') === 'phone') {
                    // Reset the border of the parent div for the phone input
                    $(e.target).closest('div').css('border', '');
                    $(e.target).closest('div').removeClass('is-invalid');
                } else {
                    // Reset the border of the input itself
                    $(e.target).css('border', '');
                }
            }
        }
    });

    $('.login-form-submit').on('click', function (e) {
        var isValid = true;
        var $form = $(this).closest('form');  // Find the closest form to the submit button

        // Check all input[required] elements inside the closest form
        $form.find('input[required]').each(function () {
            if (!$(this).val().trim()) {  // Check if input is empty
                $(this).css('border', '1px solid #F23C2F');  // Apply red border
                isValid = false;
            } else {
                $(this).css('border', '');  // Reset border if valid
            }
        });

        // If the form is invalid, prevent form submission
        if (!isValid) {
            e.preventDefault();  // Prevent form submission if any required field is empty
        }
    });


    // Remove red border when the user starts typing
    $('input[required]').on('input', function () {
        $(this).css('border', '');
    });

    // Check Cart Current Sale order is Customisable or not
    async function checkCart(service) {
        var check_cartline = await ajax.jsonRpc('/check/cartline', 'call', {
            'service': service
        })
        return check_cartline;
    }
    //  instant quote model close
    $('.warning-retry').on('click', function(event) {
        $(event.currentTarget.parentElement.parentElement).addClass('d-none')
        if ($('.warning-modal p')) {
            if ($('.warning-modal p').hasClass('d-none')) {
                $('.warning-modal p').removeClass('d-none');
            }
        }
        if ($('.warning-modal h5')) {
            $('.warning-modal h5')[0].style = '';
        }
    });

    //  submit FDM service
    $('.fdmSubmitBtn').on('click', async function(event) {
        var $form = $('.fdm_service_form')
        if (!session.user_id) {
            window.location.href = 'web/login?login-required';
        } else {
            if (await checkCart('fdm_modeling')) {
                var w_msg = 'It seems you already have a customizable product in your cart. Please empty the cart before submit request.';
                if ($('.warning-modal p')) {
                    $('.warning-modal p').addClass('d-none');
                }
                if ($('.warning-modal h5')) {
                    $('.warning-modal h5')[0].innerText = w_msg;
                    $('.warning-modal h5')[0].style = 'margin-bottom:15px;';
                    $('.warning-modal').removeClass('d-none');
                }
            } else {
                var required = checkFields($('#fdmSubmitBtn')[0].parentElement.parentElement)
                if (required.is_required) {
                    $($('#fdmSubmitBtn')[0].parentElement.parentElement).submit();
                } else {
                    if (required && required.fields_name && required.fields_name.length == 1 && required.fields_name[0] == "fdm_uv_printing_file"){
                        if ($('.warning-modal h5')) {
                            $('.warning-modal h5')[0].innerText = 'UV Printing File Missing';
                            $('.warning-modal p')[0].innerText = 'You have selected UV printing, please upload the required UV printing file to proceed.';
                            $('.warning-modal').removeClass('d-none');
                        }
                    }
                    else if ($('.warning-modal h5')) {
                        $('.warning-modal h5')[0].innerText = 'Please fill in all the mandatory fields to proceed.';
                        $('.warning-modal').removeClass('d-none');
                    }
                }
            }
        }
    });

    //  submit Projection service
    $('.projectionSubmitBtn').on('click', async function(event) {
        var $form = $('.projection_service_form')
        if (!session.user_id) {
            window.location.href = 'web/login?login-required';
        } else {
            if (await checkCart('projection_printing')) {
                var w_msg = 'It seems you already have a customizable product in your cart. Please empty the cart before submit request.';
                if ($('.warning-modal p')) {
                    $('.warning-modal p').addClass('d-none');
                }
                if ($('.warning-modal h5')) {
                    $('.warning-modal h5')[0].innerText = w_msg;
                    $('.warning-modal h5')[0].style = 'margin-bottom:15px;';
                    $('.warning-modal').removeClass('d-none');
                }
            } else {
                var required = checkFields($('#projectionSubmitBtn')[0].parentElement.parentElement)
                if (required.is_required) {
                    $($('#projectionSubmitBtn')[0].parentElement.parentElement).submit();
                } else {
                    if (required && required.fields_name && required.fields_name.length == 1 && required.fields_name[0] == "projection_uv_printing_file"){
                        if ($('.warning-modal h5')) {
                            $('.warning-modal h5')[0].innerText = 'UV Printing File Missing';
                            $('.warning-modal p')[0].innerText = 'You have selected UV printing, please upload the required UV printing file to proceed.';
                            $('.warning-modal').removeClass('d-none');
                        }
                    }
                    else if ($('.warning-modal h5')) {
                        $('.warning-modal h5')[0].innerText = 'Please fill in all the mandatory fields to proceed.';
                        $('.warning-modal').removeClass('d-none');
                    }
                }

            }
        }
    });

    //  Calculate Quote For FDM Service
    $('.fdm-calculate-quote').on('click', function(event) {
        if ($(event.currentTarget.parentElement.parentElement).length && $(event.currentTarget.parentElement.parentElement).find('.file-uploaded-container-btn.mp-btn-light-border-green')) {
            var aTag = $(event.currentTarget.parentElement.parentElement).find('.file-uploaded-container-btn.mp-btn-light-border-green')[0];
            var uv_printing_side;
            var $fdm_uv_printing_side = $(event.currentTarget.parentElement.parentElement).find('select.fdm_uv_printing_side');
            var $fdm_is_uv_printing_mp = $(event.currentTarget.parentElement.parentElement).find('#fdm_is_uv_printing_mp');
            var $fdm_quantity_input = $(event.currentTarget.parentElement.parentElement).find('#fdm_quantity');

            if ($fdm_is_uv_printing_mp[0].checked) {
                uv_printing_side = parseInt($fdm_uv_printing_side.val())
            } else {
                uv_printing_side = false
            }
            if ($fdm_is_uv_printing_mp[0].checked && $fdm_uv_printing_side.val().length == 0) {
                if ($('.warning-modal h5')) {
                    $('.warning-modal h5')[0].innerText = 'Please Select UV Printing Side for Instant Quote Calculation.';
                    $('.warning-modal').removeClass('d-none');
                    $('.loader-modal').addClass('d-none');
                }
            } else {
                if (!aTag.href) {
                    if ($('.warning-modal h5')) {
                        $('.warning-modal h5')[0].innerText = 'Please Upload Technical File for Instant Quote Calculation.';
                        $('.warning-modal').removeClass('d-none');
                    }
                } else if ($fdm_quantity_input.length != 0 && $fdm_quantity_input.val().length == 0) {
                    if ($('.warning-modal h5')) {
                        $('.warning-modal h5')[0].innerText = 'Please Update Quantity for Instant Quote Calculation.';
                        $('.warning-modal').removeClass('d-none');
                    }
                } else if (parseInt($fdm_quantity_input.val()) <= 0) {
                    if ($('.warning-modal h5')) {
                        $('.warning-modal h5')[0].innerText = 'Please Update Quantity for Instant Quote Calculation.';
                        $('.warning-modal').removeClass('d-none');
                    }
                } else {
                    var vals = {
                        'fdm_material': parseInt($(event.currentTarget.parentElement.parentElement).find('#fdm_material_for_calculate').val()),
                        'fdm_print_quality': parseInt($(event.currentTarget.parentElement.parentElement).find('#fdm_print_quality').val()),
                        'fdm_infill': parseInt($(event.currentTarget.parentElement.parentElement).find('#fdm_infill').val()),
                        'uv_printing_side': uv_printing_side,
                        'fdm_quantity': parseInt($fdm_quantity_input.val()),
                        'fdm_step_file_url': aTag.href
                    }
                    if ($('.loader-modal h5')) {
                        $('.loader-modal h5')[0].innerText = 'Processing Your Request...';
                        $('.loader-modal').removeClass('d-none');
                    }
                    var leadTimeValue = $(this).data('lead-time');
                    if (leadTimeValue) {
                        vals.lead_time = parseInt(leadTimeValue); // Add lead_time only if it's found
                    }
                    $.ajax({
                        type: "POST",
                        dataType: 'json',
                        url: '/calculate/fdm/price',
                        contentType: "application/json; charset=utf-8",
                        data: JSON.stringify({
                            'jsonrpc': "2.0",
                            'method': "call",
                            "params": vals
                        }),
                        success: function(action) {
                            if (action.result) {
                                if ('error' in action.result) {
                                    var err_msg = action.result.error
                                    if ($('.warning-modal h5')) {
                                        $('.warning-modal h5')[0].innerText = err_msg;
                                        $('.loader-modal').addClass('d-none');
                                        $('.warning-modal').removeClass('d-none');
                                    } else {
                                        console.log(err_msg)
                                    }
                                } else {
                                    var total_price = action.result.success['total_price']
                                    var fdm_product_price = action.result.success['fdm_product_price']
                                    var uv_printing_side_price = action.result.success['uv_printing_side_price']
                                    var fdm_price = action.result.success['fdm_price']
                                    var lead_time = action.result.success['lead_time'];
                                    var lead_times = action.result.success['customer_lead_time'];

                                    $('.fdm-quote').find('.fdm-total-price')[0].innerText = total_price;
                                    if (uv_printing_side_price) {
                                        $('.fdm-quote').find('.uv-printing-price')[0].innerText = uv_printing_side_price;
                                    }
                                    $('.fdm-quote').find('.fdm_price')[0].innerText = fdm_price;
                                    if ($("#fdm_product_name")[0].value.length > 0) {
                                        $('.written-fdm-price')[0].innerText = $("#fdm_product_name")[0].value
                                    }
                                    if ($(".fdm_product_price").length) {
                                        $(".fdm_product_price")[0].value = fdm_product_price;
                                    }
                                    if ($('.fdmSubmitBtn').hasClass('disabled')) {
                                        $('.fdmSubmitBtn').removeClass('disabled')
                                    }
                                    if (lead_times.length == 0) {
                                        $('.fdm-quote').find('.fdm-total-price')[0].innerText = ''
                                        $('.fdm-quote').find('.fdm_price')[0].innerText = '';
                                        $('.fdmSubmitBtn')[0].innerHTML = 'Submit Inquiry';
                                        if ($('.warning-modal h5')) {
                                            $('.warning-modal h5')[0].innerText = 'The print time is longer than our standard lead time options. Please place an inquiry, and our sales team will get back to you.';
                                            $('.warning-modal').removeClass('d-none');
                                        }
                                        var nearestForm = $('.fdmSubmitBtn').closest('#fdm_3d').find('form');
                                        if (nearestForm.length) {
                                            nearestForm.attr('data-success-page', '/');
                                        }
                                        $("#lead_time").removeAttr("required");
                                        $('.fdm-calculate-quote').addClass('disabled')
                                    }
                                    // Update lead time dropdown dynamically
                                    var hasSelected = false;
                                    var optionsHtml = '';
                                    var selectedLeadTime = vals.lead_time || '';
                                    lead_times.forEach(function(lead_time) {
                                        var isSelected = selectedLeadTime == lead_time.id ? 'selected' : '';
                                        if (isSelected) {
                                            hasSelected = true; // Mark that a selection exists
                                        }
                                        optionsHtml += `<option ${isSelected} value="${lead_time.id}">${lead_time.x_name}</option>`;
                                    });

                                    // If no lead time is selected, set lead_time.x_name == 5 as selected
                                    if (!hasSelected) {
                                        optionsHtml = ''; // Reset optionsHtml to reassign selections
                                        lead_times.forEach(function(lead_time) {
                                            var isSelected = lead_time.x_name == 5 ? 'selected' : '';
                                            optionsHtml += `<option ${isSelected} value="${lead_time.id}">${lead_time.x_name}</option>`;
                                        });
                                    }
                                    $("#lead_time").html(optionsHtml);
                                    if ($("#lead_time").parent().hasClass('d-none') && lead_times.length != 0) {
                                        $("#lead_time").parent().removeClass('d-none');
                                    }
                                    $('.loader-modal').addClass('d-none');
                                    if ($fdm_is_uv_printing_mp[0].checked) {
                                        if ($('.fdm_uv_printing_price_section').hasClass('d-none')) {
                                            $('.fdm_uv_printing_price_section').removeClass('d-none');
                                        }
                                    } else {
                                        if (!$('.fdm_uv_printing_price_section').hasClass('d-none')) {
                                            $('.fdm_uv_printing_price_section').addClass('d-none');
                                        }
                                    }
                                    $('#scrollUpFDM')[0].click();
                                }
                            } else {
                                console.log(action)
                            }
                        },
                    });
                }
            }
        } else {
            if ($('.warning-modal h5')) {
                $('.warning-modal h5')[0].innerText = 'Please fill in all the mandatory fields to proceed.';
                $('.warning-modal').removeClass('d-none');
            }
        }
    });

    $('.fdm_service_form #lead_time').on('change', function(ev){
        var leadTimeValue = $(this).val(); // Get selected value
        $('.fdm-calculate-quote').data('lead-time', leadTimeValue).click();
    })

    $('.projection_service_form #lead_time').on('change', function() {
        $('.projection-calculate-quote')
            .data('lead-time', this.value)
            .trigger('click');
    });

    $('#fdm_quantity').on('change', function(ev){
        $(ev.currentTarget.parentNode.parentNode.parentNode.parentNode.parentNode).find('.fdm-calculate-quote').click();
    })

    $('#fdm_material_for_calculate').on('change', function(ev){
        $(ev.currentTarget.parentNode.parentNode.parentNode.parentNode.parentNode).find('.fdm-calculate-quote').click();
    })

    $('#fdm_print_quality').on('change', function(ev){
        $(ev.currentTarget.parentNode.parentNode.parentNode.parentNode.parentNode).find('.fdm-calculate-quote').click();
    })

    $('#fdm_infill').on('change', function(ev){
        $(ev.currentTarget.parentNode.parentNode.parentNode.parentNode.parentNode).find('.fdm-calculate-quote').click();
    })

    $('#fdm_color').on('change', function(ev){
        $(ev.currentTarget.parentNode.parentNode.parentNode.parentNode.parentNode).find('.fdm-calculate-quote').click();
    })

    $('.fdm_service_form #uv_printing_side').on('change', function(ev){
        $(ev.currentTarget.parentNode.parentNode.parentNode.parentNode.parentNode).find('.fdm-calculate-quote').click();
    })


    $('#projection_quantity').on('change', function(ev){
        $(ev.currentTarget.parentNode.parentNode.parentNode.parentNode.parentNode).find('.projection-calculate-quote').click();
    })

    $('#projection_material').on('change', function(ev){
        $(ev.currentTarget.parentNode.parentNode.parentNode.parentNode.parentNode).find('.projection-calculate-quote').click();
    })

    $('#projection_print_quality').on('change', function(ev){
        $(ev.currentTarget.parentNode.parentNode.parentNode.parentNode.parentNode).find('.projection-calculate-quote').click();
    })

    $('.projection_service_form #uv_printing_side').on('change', function(ev){
        $(ev.currentTarget.parentNode.parentNode.parentNode.parentNode.parentNode).find('.projection-calculate-quote').click();
    })

    //  Calculate Quote For Projection Service
    $('.projection-calculate-quote').on('click', function(event) {
        if ($(event.currentTarget.parentElement.parentElement).length && $(event.currentTarget.parentElement.parentElement).find('.file-uploaded-container-btn.mp-btn-light-border-green')) {
            var aTag = $(event.currentTarget.parentElement.parentElement).find('.file-uploaded-container-btn.mp-btn-light-border-green')[0]
            var uv_printing_side;
            var $projection_uv_printing_side = $(event.currentTarget.parentElement.parentElement).find('select.projection_uv_printing_side');
            var $projection_is_uv_printing_mp = $(event.currentTarget.parentElement.parentElement).find('#projection_is_uv_printing_mp');
            var $projection_quantity_input = $(event.currentTarget.parentElement.parentElement).find('#projection_quantity');

            if ($projection_is_uv_printing_mp[0].checked) {
                uv_printing_side = parseInt($projection_uv_printing_side.val())
            } else {
                uv_printing_side = false
            }
            if ($projection_is_uv_printing_mp[0].checked && $projection_uv_printing_side.val().length == 0) {
                if ($('.warning-modal h5')) {
                    $('.warning-modal h5')[0].innerText = 'Please Select UV Printing Side for Instant Quote Calculation.';
                    $('.warning-modal').removeClass('d-none');
                    $('.loader-modal').addClass('d-none');
                }
            } else {
                if (!aTag.href) {
                    if ($('.warning-modal h5')) {
                        $('.warning-modal h5')[0].innerText = 'Please Upload Technical File for Instant Quote Calculation.';
                        $('.warning-modal').removeClass('d-none');
                    }
                } else if ($projection_quantity_input.length != 0 && $projection_quantity_input.val().length == 0) {
                    if ($('.warning-modal h5')) {
                        $('.warning-modal h5')[0].innerText = 'Please Update Quantity for Instant Quote Calculation.';
                        $('.warning-modal').removeClass('d-none');
                    }
                } else if (parseInt($projection_quantity_input.val()) <= 0) {
                    if ($('.warning-modal h5')) {
                        $('.warning-modal h5')[0].innerText = 'Please Update Quantity for Instant Quote Calculation.';
                        $('.warning-modal').removeClass('d-none');
                    }
                } else {
                    var vals = {
                        'projection_material': parseInt($(event.currentTarget.parentElement.parentElement).find('#projection_material').val()),
                        'projection_print_quality': parseInt($(event.currentTarget.parentElement.parentElement).find('#projection_print_quality').val()),
                        'uv_printing_side': uv_printing_side,
                        'projection_step_file_url': aTag.href,
                        'projection_quantity': parseInt($projection_quantity_input.val()),
                    }
                    if ($('.loader-modal h5')) {
                        $('.loader-modal h5')[0].innerText = 'Processing Your Request...';
                        $('.loader-modal').removeClass('d-none');
                    }
                    var leadTimeValue = $(this).data('lead-time');
                    if (leadTimeValue) {
                        vals.lead_time = parseInt(leadTimeValue); // Add lead_time only if it's found
                    }
                    $.ajax({
                        type: "POST",
                        dataType: 'json',
                        url: '/calculate/projection/price',
                        contentType: "application/json; charset=utf-8",
                        data: JSON.stringify({
                            'jsonrpc': "2.0",
                            'method': "call",
                            "params": vals
                        }),
                        success: function(action) {
                            if (action.result) {
                                if ('error' in action.result) {
                                    var err_msg = action.result.error
                                    if ($('.warning-modal h5')) {
                                        $('.warning-modal h5')[0].innerText = err_msg;
                                        $('.loader-modal').addClass('d-none');
                                        $('.warning-modal').removeClass('d-none');
                                    } else {
                                        console.log(err_msg)
                                    }
                                } else {
                                    var total_price = action.result.success['total_price']
                                    var projection_product_price = action.result.success['projection_product_price']
                                    var uv_printing_side_price = action.result.success['uv_printing_side_price']
                                    var projection_price = action.result.success['projection_price']
                                    var lead_time = action.result.success['lead_time'];
                                    var lead_times = action.result.success['customer_lead_time'];

                                    $('.projection-quote').find('.projection-total-price')[0].innerText = total_price;
                                    if (uv_printing_side_price) {
                                        $('.projection-quote').find('.uv-printing-price')[0].innerText = uv_printing_side_price;
                                    }
                                    $('.projection-quote').find('.projection_price')[0].innerText = projection_price;
                                    if ($("#projection_product_name")[0].value.length > 0) {
                                        $('.written-projection-price')[0].innerText = $("#projection_product_name")[0].value
                                    }
                                    if ($(".projection_product_price").length) {
                                        $(".projection_product_price")[0].value = projection_product_price;
                                    }
                                    if ($('.projectionSubmitBtn').hasClass('disabled')) {
                                        $('.projectionSubmitBtn').removeClass('disabled')
                                    }
                                    if (lead_times.length == 0) {
                                        $('.projection-quote').find('.projection-total-price')[0].innerText = ''
                                        $('.projection-quote').find('.projection_price')[0].innerText = '';
                                        $('.projectionSubmitBtn')[0].innerHTML = 'Submit Inquiry';
                                        if ($('.warning-modal h5')) {
                                            $('.warning-modal h5')[0].innerText = 'The print time is longer than our standard lead time options. Please place an inquiry, and our sales team will get back to you.';
                                            $('.warning-modal').removeClass('d-none');
                                        }
                                        var nearestForm = $('.projectionSubmitBtn').closest('#projection_3d').find('form');
                                        if (nearestForm.length) {
                                            nearestForm.attr('data-success-page', '/');
                                        }
                                        $('.projection_service_form').find('#lead_time').removeAttr("required");
                                        $('.projection-calculate-quote').addClass('disabled')
                                    }
                                    // Update lead time dropdown dynamically
                                    var hasSelected = false;
                                    var optionsHtml = '';
                                    var selectedLeadTime = vals.lead_time || '';
                                    lead_times.forEach(function(lead_time) {
                                        var isSelected = selectedLeadTime == lead_time.id ? 'selected' : '';
                                        if (isSelected) {
                                            hasSelected = true; // Mark that a selection exists
                                        }
                                        optionsHtml += `<option ${isSelected} value="${lead_time.id}">${lead_time.x_name}</option>`;
                                    });

                                    // If no lead time is selected, set lead_time.x_name == 5 as selected
                                    if (!hasSelected) {
                                        optionsHtml = ''; // Reset optionsHtml to reassign selections
                                        lead_times.forEach(function(lead_time) {
                                            var isSelected = lead_time.x_name == 4 ? 'selected' : '';
                                            optionsHtml += `<option ${isSelected} value="${lead_time.id}">${lead_time.x_name}</option>`;
                                        });
                                    }
                                    $('.projection_service_form').find('#lead_time').html(optionsHtml);
                                    if ($('.projection_service_form').find('#lead_time').parent().hasClass('d-none') && lead_times.length != 0) {
                                        $('.projection_service_form').find('#lead_time').parent().removeClass('d-none');
                                    }
                                    $('.loader-modal').addClass('d-none');
                                    if ($projection_is_uv_printing_mp[0].checked) {
                                        if ($('.projection_uv_printing_price_section').hasClass('d-none')) {
                                            $('.projection_uv_printing_price_section').removeClass('d-none');
                                        }
                                    } else {
                                        if (!$('.projection_uv_printing_price_section').hasClass('d-none')) {
                                            $('.projection_uv_printing_price_section').addClass('d-none');
                                        }
                                    }
                                    $('#scrollUpProjection')[0].click();
                                }
                            } else {
                                console.log(action)
                            }
                        },
                    });
                }
            }
        } else {
            if ($('.warning-modal h5')) {
                $('.warning-modal h5')[0].innerText = 'Please fill in all the mandatory fields to proceed.';
                $('.warning-modal').removeClass('d-none');
            }
        }
    });

    //  Check Required Fields are filled than Submit Service Form
    $('.check_fields').on('click', function(event) {
        if (!session.user_id) {
            window.location.href = '/web/login?login-required';
        } else {
            var required = checkFields(event.currentTarget.parentElement.parentElement)
            if (required.is_required) {
                $(event.currentTarget.parentElement.parentElement).submit();
            } else {
                if (required && required.fields_name && required.fields_name.length == 1){
                    if(required.fields_name[0] == "metal_feb_uv_printing_file" || required.fields_name[0] == "injection_uv_printing_file" || required.fields_name[0] == "cnc_uv_printing_file"){
                        if ($('.warning-modal h5')) {
                            $('.warning-modal h5')[0].innerText = 'UV Printing File Missing';
                            $('.warning-modal p')[0].innerText = 'You have selected UV printing, please upload the required UV printing file to proceed.';
                            $('.warning-modal').removeClass('d-none');
                        }
                    }
                }
                else if ($('.warning-modal h5')) {
                    $('.warning-modal h5')[0].innerText = 'Please fill in all the mandatory fields to proceed.';
                    $('.warning-modal').removeClass('d-none');
                }
            }
        }
    });

    //  Switch On-Off
    $('.mp_o_switch').on('click', function(event) {
        if (event.currentTarget.firstElementChild.checked) {
            event.currentTarget.firstElementChild.checked = false;
        } else {
            event.currentTarget.firstElementChild.checked = true;
        }
    });

    //  File Upload Click Event (Required *)
    $('.highlighted-green').on('click', function(e) {
        e.preventDefault();
        e.stopPropagation();
        e.currentTarget.parentNode.previousElementSibling.click();
    });

    $('.upload-icon').on('click', function(e) {
        e.preventDefault();
        e.stopPropagation();
        $(e.currentTarget.parentNode).find('input').click()
    });

    //  File Upload Click Event (Required *)
        $('.hidden-file-input').on('change', function(e) {
            e.preventDefault();
            e.stopPropagation();
            const file = e.target.files[0]; // Get the selected file
            const acceptedTypes = $(e.target).attr('accept'); // Get the accept attribute
            const allowedExtensions = acceptedTypes ? acceptedTypes.split(',').map(type => type.trim()) : []; // Convert to array
            const fileExtension = file.name.split('.').pop().toLowerCase(); // Get file extension

            // Check if .zip is allowed explicitly from DB
            const isZipAllowed = allowedExtensions.includes('.zip');
            if (e.currentTarget.classList.contains('file-uploading-powerviz')) {
                fileUploadForPowerviz(e);
                // if ($('.loader-modal').length){
                //         $('.loader-modal').removeClass('d-none')
                // ;}
                // if (fileExtension !== 'zip') {
                //     setTimeout(function () {
                //          if ($('.loader-modal').length){
                //             $('.loader-modal').addClass('d-none')
                //         }
                //         $(e.currentTarget.parentNode.parentNode.parentNode.parentNode).find('.s_website_form_submit .mp-btn-light-green').click()
                //     }, 7000);
                // }
                // else{
                //     if ($('.loader-modal').length){
                //         $('.loader-modal').addClass('d-none')
                //     }
                // }
            } else {
                fileUpload(e);
            }
        });

    //  File Upload Drag & Drop Event
    $('.file-upload').on('drag dragstart dragend dragover dragenter dragleave drop', function(e) {
        e.preventDefault();
        e.stopPropagation();
    }).on('dragover dragenter', function(e) {
        $(e.currentTarget).addClass('file-upload-background');
    }).on('dragleave dragend drop', function(e) {
        $(e.currentTarget).removeClass('file-upload-background');
    }).on('drop', function(e) {
        if (e.currentTarget.classList.contains('file-uploading-powerviz')) {
            fileUploadForPowerviz(e);
        } else {
            fileUpload(e);
        }
    });

    //  Function for Clean/Remove File
    $('.uploading-cancel-icon-box').on('click', function(e) {
        e.preventDefault();
        e.stopPropagation();
        if ($(e.currentTarget.parentElement.parentElement.parentElement.parentElement).find('#form-bottom-powerviz')) {
            $(e.currentTarget.parentElement.parentElement.parentElement.parentElement).find('#form-bottom-powerviz').attr({
                'href': '',
                target: '_blank'
            }).addClass('d-none');
        }
        if ($(e.currentTarget.parentElement.parentElement.parentElement.parentElement).find('.file-uploaded-container-btn.mp-btn-light-border-green')) {
            $(e.currentTarget.parentElement.parentElement.parentElement.parentElement).find('.file-uploaded-container-btn.mp-btn-light-border-green').attr('target', '_blank').addClass('d-none').removeAttr("href");
        }
        if ($(e.currentTarget.parentElement.parentElement.previousElementSibling).find('input[type="file"]')) {
            $(e.currentTarget.parentElement.parentElement.previousElementSibling).find('input[type="file"]').val('')
        }
        $(e.currentTarget.parentElement.parentElement).addClass('d-none');
        $(e.currentTarget.parentElement.parentElement.previousElementSibling).removeClass('d-none');
    })

    //  Switch On/Off For Required Fields
    $('#metal_feb_is_uv_printing_mp').change(function(e) {
        if (this.checked) {
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
    $('#fdm_is_uv_printing_mp').change(function() {
        if (this.checked) {
            $('#fdm_uv_printing_file').attr("required", "true");
            $('.fdm_uv_printing_file_div_p').addClass('o_input_required');
            if ($('#fdm_uv_printing_file').attr("disabled") == 'disabled') {
                $('#fdm_uv_printing_file').removeAttr("disabled");
            }
            if ($('.fdm_uv_printing_side_section').length) {
                if ($('.fdm_uv_printing_side_section').hasClass('disabled')) {
                    $('.fdm_uv_printing_side_section').removeClass("disabled");
                }
            }
            $('#uv_printing_side.fdm_uv_printing_side').attr("required", "required");
            $("label[for='uv_printing_side'].fdm_uv_printing_side").addClass('o_input_required');
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
            if ($('.fdm_uv_printing_side_section').length) {
                if (!$('.fdm_uv_printing_side_section').hasClass('disabled')) {
                    $('.fdm_uv_printing_side_section').addClass("disabled");
                }
            }
            $('#uv_printing_side.fdm_uv_printing_side')[0].required = false;
            $("label[for='uv_printing_side'].fdm_uv_printing_side").removeClass('o_input_required');
            $('.fdm_uv_printing_side')[0].selectedIndex = 0;
            $('.fdm-calculate-quote')[0].click();
            $('#uv_printing_side.fdm_uv_printing_side').css('border', '1px solid #dbdbdb');

        }
    });
    $('#projection_is_uv_printing_mp').change(function() {
        if (this.checked) {
            $('#projection_uv_printing_file').attr("required", "true");
            $('.projection_uv_printing_file_div_p').addClass('o_input_required');
            if ($('#projection_uv_printing_file').attr("disabled") == 'disabled') {
                $('#projection_uv_printing_file').removeAttr("disabled");
            }
            if ($('.projection_uv_printing_side_section').length) {
                if ($('.projection_uv_printing_side_section').hasClass('disabled')) {
                    $('.projection_uv_printing_side_section').removeClass("disabled");
                }
            }
            $('#uv_printing_side.projection_uv_printing_side').attr("required", "required");
            $("label[for='uv_printing_side'].projection_uv_printing_side").addClass('o_input_required');
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
            if ($('.projection_uv_printing_side_section').length) {
                if (!$('.projection_uv_printing_side_section').hasClass('disabled')) {
                    $('.projection_uv_printing_side_section').addClass("disabled");
                }
            }
            $('#uv_printing_side.projection_uv_printing_side')[0].required = false;
            $("label[for='uv_printing_side'].projection_uv_printing_side").removeClass('o_input_required');
            $('.projection_uv_printing_side')[0].selectedIndex = 0;
            $('.projection-calculate-quote')[0].click()
            $('#uv_printing_side.projection_uv_printing_side').css('border', '1px solid #dbdbdb');
        }
    });
    $('#injection_is_uv_printing_mp').change(function() {
        if (this.checked) {
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
    $('#cnc_is_uv_printing_mp').change(function() {
        if (this.checked) {
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


    const $slides = $('.user-review-card');
    const $carouselContainer = $('.user-review-section');
    let currentIndex = 0;

    function changeSlide() {
        const $currentSlide = $slides.eq(currentIndex);
        const nextIndex = (currentIndex + 1) % $slides.length;
        const $nextSlide = $slides.eq(nextIndex);

        // Set a lighter background fade effect
        $carouselContainer.css('background', `linear-gradient(0deg, rgba(0, 0, 0, 0.3) 0%, rgba(0, 0, 0, 0.3) 100%), ${$nextSlide.data('bg')} lightgray 50%/cover no-repeat`);

        // Animate slides
        $currentSlide.removeClass('active').addClass('exiting');
        $nextSlide.addClass('active');

        setTimeout(() => {
            $currentSlide.removeClass('exiting');
            currentIndex = nextIndex;
        }, 1000); // Match transition duration
    }

    // Initialize first slide
    $slides.eq(currentIndex).addClass('active');
    $carouselContainer.css('background',`linear-gradient(0deg, rgba(0, 0, 0, 0.6) 0%, rgba(0, 0, 0, 0.6) 100%), ${$slides.eq(currentIndex).data('bg')}  lightgray 50%/cover no-repeat`);
    // Auto-slide every 3 seconds
    setInterval(changeSlide, 3000);

    $('.websiteblog_filter_btn').on('click', function(e) {
        if($('.blog-left-col').length){
            $('.blog-left-col').addClass('scrolled_up');
        }
    });
    $('.blog_section_cancel_btn').on('click', function(e) {
        if($('.blog-left-col').length && $('.blog-left-col').hasClass('scrolled_up')){
            $('.blog-left-col').removeClass('scrolled_up');
        }
    });
    $('.table_of_content_link').on('click', function(e){
        var $currentLink = $(e.currentTarget);

        // Remove 'active' class from all siblings
        $currentLink.parent().children().removeClass('active');

        // Add 'active' class to clicked element
        $currentLink.addClass('active');
    });

    $('.sort_drop_click').on('click', function(e){
        var $currentLink = $(e.currentTarget);
        if($currentLink.length > 0){
            var option_id = $currentLink[0].id
            for(var sort_option of $('.sort_selection option')){
                if(sort_option.hasAttribute('selected')){
                    sort_option.removeAttribute('selected')
                }
            }
            var $sort_element = $('.sort_selection #'+option_id)
            if($sort_element.length > 0){
                $sort_element[0].selected = true;
            }
            var $js_attributes_form = $('form.js_attributes');
            if($js_attributes_form.length > 0){
                $js_attributes_form[0].submit();
            }
        }

    });

    $('.shop_activate_filters').on('click', function(e) {
        if($('.sort_by_mobile_device_section').length > 0 && $('.sort_by_mobile_device_section').hasClass('scrolled_up')){
            $('.sort_by_mobile_device_section').removeClass('scrolled_up');
        }
        if($('#products_grid_before').length > 0 && !$('#products_grid_before').hasClass('scrolled_up')){
            $('#products_grid_before').addClass('scrolled_up');
        }
    });
    $('.shop_activate_sortby').on('click', function(e) {
        if($('#products_grid_before').length > 0 && $('#products_grid_before').hasClass('scrolled_up')){
            $('#products_grid_before').removeClass('scrolled_up');
        }
        if($('.sort_by_mobile_device_section').length > 0 && !$('.sort_by_mobile_device_section').hasClass('scrolled_up')){
            $('.sort_by_mobile_device_section').addClass('scrolled_up');
        }
    });
    $('.shop_section_cancel_btn').on('click', function(e) {
        if($('#products_grid_before').length > 0 && $('#products_grid_before').hasClass('scrolled_up')){
            $('#products_grid_before').removeClass('scrolled_up');
        }
    });
    $('.shop_sortby_section_cancel_btn').on('click', function(e) {
        if($('.sort_by_mobile_device_section').length > 0 && $('.sort_by_mobile_device_section').hasClass('scrolled_up')){
            $('.sort_by_mobile_device_section').removeClass('scrolled_up');
        }
    });
    $('.shop_filter_apply_btn').on('click', function(e) {


        if($('.js_attributes').length > 0){
            $($('.js_attributes')[0]).submit();
        }

    });
    $('.onchange_sortby_mobile_input').on('click', function(e) {
        if($('.onchange_sortby_mobile_input').length > 0){
            for(var sort_by of $('.onchange_sortby_mobile_input')){
                sort_by.checked = false;
            }
            e.currentTarget.checked = true;
        }
    });
    $('.shop_sortby_filter_apply_btn').on('click', function(e) {
        if($('.sort_by_mobile_device_box input').length > 0){
            for(var sort_by of $('.sort_by_mobile_device_box input')){
                if(sort_by.checked){

                    var option_id = sort_by.id
                    for(var sort_option of $('.sort_selection option')){
                        if(sort_option.hasAttribute('selected')){
                            sort_option.removeAttribute('selected')
                        }
                    }
                    var $sort_element = $('.sort_selection #'+option_id)
                    if($sort_element.length > 0){
                        $sort_element[0].selected = true;
                    }
                    var $js_attributes_form = $('form.js_attributes');
                    if($js_attributes_form.length > 0){
                        $js_attributes_form[0].submit();
                    }
                }
            }
        }
    });
});

//$(document).ready(function() {
//    var currentIndex = 0;
//    var rotationInterval = 12000;
//
//    var $largeBox = $('.team-member.large');
//    var $smallBoxes = $('.team-member.small');
//    var totalMembers = $smallBoxes.length + 1;
//    var originalMembers = [];
//    originalMembers.push({
//        image: $largeBox.find('img').attr('src'),
//        name: $largeBox.find('h3').text(),
//        role: $largeBox.find('.role').text(),
//        description: $largeBox.find('.description').text(),
//        linkedin: $largeBox.find('.fa-linkedin').parent().attr('href')
//    });
//
//    $smallBoxes.each(function() {
//        originalMembers.push({
//            image: $(this).find('img').attr('src'),
//            name: $(this).find('h3').text(),
//            role: $(this).find('.role').text(),
//            description: $(this).find('.description').text(),
//            linkedin: $(this).find('.fa-linkedin').parent().attr('href')
//        });
//    });
//
//    function updateMember($element, data) {
//        $element.find('img').attr('src', data.image);
//        $element.find('h3').text(data.name);
//        $element.find('.role').text(data.role);
//        $element.find('.description').text(data.description);
//        $element.find('.fa-linkedin').parent().attr('href', data.linkedin);
//    }
//
//    function rotateMember() {
//        currentIndex = (currentIndex + 1) % totalMembers;
//        $largeBox.fadeOut(500, function() {
//            updateMember($largeBox, originalMembers[currentIndex]);
//            for(var i = 0; i < $smallBoxes.length; i++) {
//                var boxIndex = (i + currentIndex + 1) % totalMembers;
//                updateMember($($smallBoxes[i]), originalMembers[boxIndex]);
//            }
//            $largeBox.fadeIn(500);
//        });
//    }
//
//    var rotationTimer = setInterval(rotateMember, rotationInterval);
//
//    $('.team-member.large').hover(
//        function() {
//            clearInterval(rotationTimer);
//        },
//        function() {
//            rotationTimer = setInterval(rotateMember, rotationInterval);
//        }
//    );
//
//    $('.team-member.small').click(function() {
//        clearInterval(rotationTimer);
//        var clickedIndex = $('.team-member.small').index(this) + 1;
//        var rotationsNeeded = (clickedIndex - currentIndex + totalMembers) % totalMembers;
//        currentIndex = clickedIndex - 1;
//        rotateMember();
//        rotationTimer = setInterval(rotateMember, rotationInterval);
//    });
//
//    function resetPositions() {
//        clearInterval(rotationTimer);
//        currentIndex = 0;
//
//        $largeBox.fadeOut(500, function() {
//            updateMember($largeBox, originalMembers[0]);
//            for(var i = 0; i < $smallBoxes.length; i++) {
//                updateMember($($smallBoxes[i]), originalMembers[i + 1]);
//            }
//            $largeBox.fadeIn(500);
//        });
//        rotationTimer = setInterval(rotateMember, rotationInterval);
//    }
//});