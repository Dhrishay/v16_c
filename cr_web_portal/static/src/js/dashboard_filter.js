/** @odoo-module */

import { RELATIVE_DATE_RANGE_TYPES } from "@spreadsheet/helpers/constants";
import { _lt } from "@web/core/l10n/translation";
import { serializeDate, serializeDateTime } from "@web/core/l10n/dates";
import GlobalFiltersUIPlugin from "@spreadsheet/global_filters/plugins/global_filters_ui_plugin";
import { patch } from "@web/core/utils/patch";
const { DateTime } = luxon;
import { Domain } from "@web/core/domain";
import { constructDateRange, getPeriodOptions, QUARTER_OPTIONS } from "@web/search/utils/dates";


RELATIVE_DATE_RANGE_TYPES.push({ type: "previous_month", description: _lt("Last Month") })
RELATIVE_DATE_RANGE_TYPES.push({ type: "previous_year", description: _lt("Last Year") })
RELATIVE_DATE_RANGE_TYPES.push({ type: "current_month", description: _lt("Current Month") })
RELATIVE_DATE_RANGE_TYPES.push({ type: "current_year", description: _lt("Current Year") })

const MONTHS = {
    january: { value: 1, granularity: "month" },
    february: { value: 2, granularity: "month" },
    march: { value: 3, granularity: "month" },
    april: { value: 4, granularity: "month" },
    may: { value: 5, granularity: "month" },
    june: { value: 6, granularity: "month" },
    july: { value: 7, granularity: "month" },
    august: { value: 8, granularity: "month" },
    september: { value: 9, granularity: "month" },
    october: { value: 10, granularity: "month" },
    november: { value: 11, granularity: "month" },
    december: { value: 12, granularity: "month" },
};

export function getRelativeDateDomainCustom(now, offset, rangeType, fieldName, fieldType) {
    let endDate = now.minus({ day: 1 }).endOf("day");
    let startDate = endDate;
    console.log(typeof(now))
    switch (rangeType) {
        case "last_week": {
            const offsetParam = { day: 7 * offset };
            endDate = endDate.plus(offsetParam);
            startDate = now.minus({ day: 7 }).plus(offsetParam);
            break;
        }
        case "last_month": {
            const offsetParam = { day: 30 * offset };
            endDate = endDate.plus(offsetParam);
            startDate = now.minus({ day: 30 }).plus(offsetParam);
            break;
        }
        case "last_three_months": {
            const offsetParam = { day: 90 * offset };
            endDate = endDate.plus(offsetParam);
            startDate = now.minus({ day: 90 }).plus(offsetParam);
            break;
        }
        case "last_six_months": {
            const offsetParam = { day: 180 * offset };
            endDate = endDate.plus(offsetParam);
            startDate = now.minus({ day: 180 }).plus(offsetParam);
            break;
        }
        case "last_year": {
            const offsetParam = { day: 365 * offset };
            endDate = endDate.plus(offsetParam);
            startDate = now.minus({ day: 365 }).plus(offsetParam);
            break;
        }
        case "last_three_years": {
            const offsetParam = { day: 3 * 365 * offset };
            endDate = endDate.plus(offsetParam);
            startDate = now.minus({ day: 3 * 365 }).plus(offsetParam);
            break;
        }
        case "previous_month": {
            endDate = now.minus({ months: 1 }).endOf('month');
            startDate = now.minus({ months: 1 }).startOf('month');
            break;
        }
        case "previous_year": {
            let endDate1 = now.minus({ years: 1 }).endOf('year');
            let startDate1 = now.minus({ years: 1 }).startOf('year');

            endDate = endDate1.plus({month: 3})
            startDate = startDate1.plus({month: 3})
            break;
        }
        case "current_month": {
            endDate = now.endOf('month');
            startDate = now.startOf('month');
            break;
        }
        case "current_year": {
            let endDate1 = now.endOf('year');
            let startDate1 = now.startOf('year');

            endDate = endDate1.plus({month: 3});
            startDate = startDate1.plus({month: 3});
            break;
        }
        default:
            return undefined;
    }
    startDate = startDate.startOf("day");

    let leftBound, rightBound;
    if (fieldType === "date") {
        leftBound = serializeDate(startDate);
        rightBound = serializeDate(endDate);
    } else {
        leftBound = serializeDateTime(startDate);
        rightBound = serializeDateTime(endDate);
    }

    return new Domain(["&", [fieldName, ">=", leftBound], [fieldName, "<=", rightBound]]);
}


patch(GlobalFiltersUIPlugin.prototype, 'CustomGlobalFilter', {
    _getDateDomain(filter, fieldMatching) {
        let granularity;
        const value = this.getGlobalFilterValue(filter.id);
        if (!value || !fieldMatching.chain) {
            return new Domain();
        }
        const field = fieldMatching.chain;
        const type = fieldMatching.type;
        const offset = fieldMatching.offset || 0;
        const now = DateTime.local();
        if (filter.rangeType === "relative") {
            return getRelativeDateDomainCustom(now, offset, value, field, type);
        }
        if (value.yearOffset === undefined) {
            return new Domain();
        }

        const setParam = { year: now.year };
        const yearOffset = value.yearOffset || 0;
        const plusParam = {
            years: filter.rangeType === "year" ? yearOffset + offset : yearOffset,
        };
        if (!value.period || value.period === "empty") {
            granularity = "year";
        } else {
            switch (filter.rangeType) {
                case "month":
                    granularity = "month";
                    setParam.month = MONTHS[value.period].value;
                    plusParam.month = offset;
                    break;
                case "quarter":
                    granularity = "quarter";
                    setParam.quarter = QUARTER_OPTIONS[value.period].setParam.quarter;
                    plusParam.quarter = offset;
                    break;
            }
        }
        return constructDateRange({
            referenceMoment: now,
            fieldName: field,
            fieldType: type,
            granularity,
            setParam,
            plusParam,
        }).domain;
    }

})