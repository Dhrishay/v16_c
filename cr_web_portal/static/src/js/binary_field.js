/** @odoo-module **/

import { registry } from "@web/core/registry";
import { useService } from "@web/core/utils/hooks";
import { BinaryField } from "@web/views/fields/binary/binary_field";

import { patch } from "@web/core/utils/patch";

patch(BinaryField.prototype, "cr_web_portal.BinaryFieldExt", {

    openTreeView(name){
        if(this.props.record.model.env.searchModel.resModel == 'product.product'){
            this.props.record.model.actionService.doAction({
                type: "ir.actions.act_window",
                name: 'Doument History ',
                views: [
                    [false, "list"],
                ],
                domain:[['file_type','=',name],['product_id','=',this.props.record.data.id]],
                res_model: 'document.history',
            });
        }
        else{
            this.props.record.model.actionService.doAction({
                type: "ir.actions.act_window",
                name: 'Doument History ',
                views: [
                    [false, "list"],
                ],
                domain:[['file_type','=',name],['product_template_id','=',this.props.record.data.id]],
                res_model: 'document.history',
            });
        }
    }
});
