/** @odoo-module **/

import { registerPatch } from '@mail/model/model_core';
import { clear } from '@mail/model/model_field_command';

registerPatch({
    name: 'MessageView',
    fields: {
        dateFromNow: ({
            compute() {
                if (!this.message) {
                    return clear();
                }
                if (!this.message.date) {
                    return clear();
                }
                if (!this.clockWatcher.clock.date) {
                    return clear();
                }
                const now = moment(this.clockWatcher.clock.date.getTime());
                if (now.diff(this.message.date, 'seconds') < 45) {
                    return this.env._t("now");
                }
                return  this.message.date.toString().slice(0, 24);
            },
        }),

    },
});
