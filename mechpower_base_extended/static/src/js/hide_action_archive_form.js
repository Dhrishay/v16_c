/** @odoo-module **/

import {patch} from "@web/core/utils/patch";
import {FormController} from "@web/views/form/form_controller";
import {useService} from "@web/core/utils/hooks";

patch(FormController.prototype, "form_controller_extend",{
    async setup() {
        this._super();
        this.orm = useService("orm");
        const currentUser = await this.orm.call(
            "res.users",
            "get_is_hide_archive_and_applied_models",
            [],
            {'model':this.props.resModel}
        );
        this.archiveEnabled = false
        this.archInfo.activeActions['delete'] = false
        if (currentUser && currentUser.show_archive_delete_option){
            if (currentUser.archive_available){
                this.archiveEnabled = true
            }
            this.archInfo.activeActions['delete'] = true
        }
    },
});
