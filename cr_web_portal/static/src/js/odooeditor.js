/** @odoo-module **/

import { OdooEditor } from '@web_editor/js/editor/odoo-editor/src/OdooEditor'
import { patch } from "@web/core/utils/patch";
import { ancestors } from '@web_editor/js/common/wysiwyg_utils';

patch(OdooEditor.prototype, 'OdooEditorCustomer', {
    bindExecCommand(element) {
        for (const buttonEl of element.querySelectorAll('[data-call]')) {
            buttonEl.addEventListener('click', ev => {
                const sel = this.document.getSelection();
                if (sel.anchorNode && ancestors(sel.anchorNode).includes(this.editable)) {
                    this.execCommand(buttonEl.dataset.call, buttonEl.dataset.arg1);

                    ev.preventDefault();
                    this._updateToolbar();
                }
            });
        }
        var self = this;
        var font_size_input = element.querySelector('#fontsizeinput');
        if(font_size_input){
            font_size_input.addEventListener('keydown', function(event){
                if (event.keyCode === 13) { // 'A' or 'a'
                   var customFontSizeVal =  element.querySelector('#customFontSizeVal');
                   customFontSizeVal.setAttribute('data-arg1',this.value+'px');
                   customFontSizeVal.click()
                   return true;
                }
            });
        }
    }
});