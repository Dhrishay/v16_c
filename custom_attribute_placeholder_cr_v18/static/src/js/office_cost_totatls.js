/* @odoo-module */

import { patch } from "@web/core/utils/patch";
import { TaxTotalsComponent } from "@account/components/tax_totals/tax_totals";
import { formatMonetary } from "@web/views/fields/formatters";

patch(TaxTotalsComponent.prototype, {
     office_cost() {
        var office_cost = formatMonetary(this?.totals?.office_cost, {currencyId: this.totals.currency_id});
        return office_cost;
     }
})