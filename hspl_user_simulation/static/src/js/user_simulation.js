/** @odoo-module **/
/*
"JS modified as per OWL JS structure instead of old js structure (gk)"
*/

import { Component, onMounted, useRef } from "@odoo/owl";
import { useService } from "@web/core/utils/hooks";
import { registry } from "@web/core/registry";
import { _t } from 'web.core';
import session from 'web.session';

export class UserSimulation extends Component {
    setup() {
        super.setup();
        this.action = useService("action");
        this.button_ref = useRef("UserSimulationRef");
        this.orm = useService("orm");

        onMounted(async () => {
            var result = await this.orm.call(
                'res.users',
                'check_for_user_simulation',
                [],
                { 'user_id': session.uid },
            );
            if (!result) {
                this.button_ref.el.classList.add('d-none');
            };
        });
    };

    _onclickUserSimulation() {
        this.action.doAction({
            res_model: 'user.simulation.wizard',
            name: _t('User Simulation'),
            views: [[false, 'form']],
            type: 'ir.actions.act_window',
            target: 'new',
        });
    };
};

UserSimulation.template = "hspl_user_simulation.UserSimulation";

export const systrayItem = {
    Component: UserSimulation,
};

registry.category("systray").add("UserSimulation", systrayItem, { sequence: 1 });



/*
"Old Javascript Structure"
*/

//odoo.define('web.UserSimulation', function (require) {
//"use strict";
//
//var SystrayMenu = require('web.SystrayMenu');
//var session = require('web.session');
//var Widget = require('web.Widget');
//var core = require('web.core');
//var _t = core._t;
//
//var UserSimulation = Widget.extend({
//    template: "WebClient.UserSimulation",
//    events: {
//        "click a": "open_simulation_wizard"
//    },
//    open_simulation_wizard: function(ev){
//        ev.preventDefault();
//        this.do_action({
//            res_model: 'user.simulation.wizard',
//            name: _t('User Simulation'),
//            views: [[false, 'form']],
//            type: 'ir.actions.act_window',
//            target: 'new',
//        });
//    },
//    start: function () {
//        return $.when(
//            this._rpc({
//                    model: 'res.users',
//                    method: 'check_for_user_simulation',
//                    kwargs: {'user_id':session.uid},
//                }),
//            this._super()
//        ).then(function(result){
//            if(!result){
//                this.hide_simulation();
//            }
//        }.bind(this));
//    },
//    hide_simulation: function(){
//        this.$el.html('');
//    },
//
//});
//
//SystrayMenu.Items.push(UserSimulation);
//
//});