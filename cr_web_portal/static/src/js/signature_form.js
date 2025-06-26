/** @odoo-module **/

import { patch } from "@web/core/utils/patch";
import { qweb,_t } from 'web.core';
var SignatureForm = require('portal.signature_form').SignatureForm;
var Dialog = require('web.Dialog');
var ajax = require('web.ajax');

patch(SignatureForm.prototype, "Mech_SignatureForm", {
    init: function (parent, options) {
        this._super.apply(this, arguments);
        this.sendLabel = options.sendLabel || _t("Accept & Pay");
    },
//     $("#confirm").on('click', function () {
//                return confirm('Are you sure?');
//     }),

     _onClickSignSubmit: function (ev) {
        var self = this;
        ev.preventDefault();
        if (!this.nameAndSignature.validateSignature()) {
            return;
        }

        const fileInput = document.getElementById('purchase_order');
        var po_file_no = document.getElementById('purchase_order_no');

//        if (po_file_no && !po_file_no.value){
//            alert('Please Add Purchase Order Number')
//            return
//        }
//        if (fileInput && !fileInput.value){
//            alert('Please Upload Purchase Order File')
//            return
//        }
        if(this?.nameAndSignature?.$el?.closest('form.js_website_submit_form')){
            var model_form = this.nameAndSignature.$el.closest('form.js_website_submit_form').attr('data-order-id')
        }
        if (fileInput && fileInput.files[0]) {
          var po_file_no_c = false
          if (po_file_no){
            po_file_no_c = document.getElementById('purchase_order_no').value;
          }
        $.blockUI({
                'message': '<h4 class="text-white"><img src="/web/static/img/spin.png" class="fa-pulse"/>' +
                    '    <br />' + 'Please Wait....' +
                    '</h4>'
            });
          const file = fileInput.files[0];
          const reader = new FileReader();
          var self = this
          var base64String = ''
           reader.onload =  function(event) {
            var base64String = event.target.result;
            var name = self.nameAndSignature.getName();
            var signature = self.nameAndSignature.getSignatureImage()[1];

            return self._rpc({
                route: self.callUrl,
                params: _.extend(self.rpcParams, {
                    'name': name,
                    'signature': signature,
                    'po_url':base64String,
                    'po_file_name':file.name,
                    'po_file_no':po_file_no_c,
                }),
            }).then(function (data) {
                if (data && data.error) {
                    self.$('.o_portal_sign_error_msg').remove();
                    self.$controls.prepend(qweb.render('portal.portal_signature_error', {widget: data}));
                } else if (data && data.success) {
                    var $success = qweb.render('portal.portal_signature_success', {widget: data});
                    self.$el.empty().append($success);
                }
                $.unblockUI();
                if (data.redirect_url) {
                    window.location = data.redirect_url;
                    };

                $('#modalaccept').modal('hide')
                $(`#modalaccept_${model_form}`).modal('hide')
                $('#modalaccept1').modal('show')
                $(`#modalaccept1_${model_form}`).modal('show')
            });
          }
          reader.readAsDataURL(file);
        }else{
            $.blockUI({
                'message': '<h4 class="text-white"><img src="/web/static/img/spin.png" class="fa-pulse"/>' +
                    '    <br />' + 'Please Wait....' +
                    '</h4>'
            });
            var name = this.nameAndSignature.getName();
            var signature = this.nameAndSignature.getSignatureImage()[1];
            return this._rpc({
                route: this.callUrl,
                params: _.extend(this.rpcParams, {
                    'name': name,
                    'signature': signature,
                    'po_url':false,
                    'po_file_name':false,
                }),
            }).then(function (data) {
                if (data.error) {
                    self.$('.o_portal_sign_error_msg').remove();
                    self.$controls.prepend(qweb.render('portal.portal_signature_error', {widget: data}));
                } else if (data.success) {
                    var $success = qweb.render('portal.portal_signature_success', {widget: data});
                    self.$el.empty().append($success);
                }
                if (data.redirect_url) {
                    window.location = data.redirect_url;
                    };
                $('#modalaccept').modal('hide')
                $(`#modalaccept_${model_form}`).modal('hide')
                $.unblockUI();
                $('#modalaccept1').modal('show')
                $(`#modalaccept1_${model_form}`).modal('show')
            });
          }
    },
});