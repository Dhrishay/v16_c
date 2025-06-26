/** @odoo-module **/

import { _lt } from "@web/core/l10n/translation";
import { sprintf } from "@web/core/utils/strings";
import { QUARTERS, PERIOD_OPTIONS, QUARTER_OPTIONS, getSetParam, getSelectedOptions, sortPeriodOptions} from "@web/search/utils/dates";
import { Domain } from "@web/core/domain";
import { serializeDate, serializeDateTime } from "@web/core/l10n/dates";
import { localization } from "@web/core/l10n/localization";

export const DEFAULT_PERIOD = "this_month";

QUARTERS[1] = { description: _lt("Q1"), coveredMonths: [4, 5, 6] },
QUARTERS[2] = { description: _lt("Q2"), coveredMonths: [7, 8, 9] },
QUARTERS[3] = { description: _lt("Q3"), coveredMonths: [10, 11, 12] },
QUARTERS[4] = { description: _lt("Q4"), coveredMonths: [1, 2, 3] },



QUARTER_OPTIONS['second_quarter'] = {
        id: "second_quarter",
        groupNumber: 1,
        description: QUARTERS[2].description,
        setParam: { quarter: 2 },
        granularity: "quarter",
    },

QUARTER_OPTIONS['third_quarter'] = {
        id: "third_quarter",
        groupNumber: 1,
        description: QUARTERS[3].description,
        setParam: { quarter: 3 },
        granularity: "quarter",
    },

QUARTER_OPTIONS['fourth_quarter'] = {
        id: "fourth_quarter",
        groupNumber: 1,
        description: QUARTERS[4].description,
        setParam: { quarter: 4 },
        granularity: "quarter",
    },

QUARTER_OPTIONS['first_quarter'] = {
        id: "first_quarter",
        groupNumber: 1,
        description: QUARTERS[1].description,
        setParam: { quarter: 1 },
        granularity: "quarter",
    },

PERIOD_OPTIONS['fourth_quarter'] = QUARTER_OPTIONS['fourth_quarter']
PERIOD_OPTIONS['first_quarter'] = QUARTER_OPTIONS['first_quarter']
PERIOD_OPTIONS['third_quarter'] = QUARTER_OPTIONS['third_quarter']
PERIOD_OPTIONS['second_quarter'] = QUARTER_OPTIONS['second_quarter']


export function constructDateDomainCustom(
    referenceMoment,
    fieldName,
    fieldType,
    selectedOptionIds,
    comparisonOptionId
) {
    let plusParam;
    let selectedOptions;
    if (comparisonOptionId) {
        [plusParam, selectedOptions] = getComparisonParams(
            referenceMoment,
            selectedOptionIds,
            comparisonOptionId
        );
    } else {
        selectedOptions = getSelectedOptions(referenceMoment, selectedOptionIds);
    }
    const yearOptions = selectedOptions.year;
    const otherOptions = [...(selectedOptions.quarter || []), ...(selectedOptions.month || [])];
    sortPeriodOptions(yearOptions);
    sortPeriodOptions(otherOptions);
    const ranges = [];
    for (const yearOption of yearOptions) {
        const constructRangeParams = {
            referenceMoment,
            fieldName,
            fieldType,
            plusParam,
        };
        if (otherOptions.length) {
            for (const option of otherOptions) {
                const setParam = Object.assign(
                    {},
                    yearOption.setParam,
                    option ? option.setParam : {}
                );
                const { granularity } = option;
                const range = constructDateRangeCustom(
                    Object.assign({ granularity, setParam }, constructRangeParams)
                );
                ranges.push(range);
            }
        } else {
            const { granularity, setParam } = yearOption;
            const range = constructDateRangeCustom(
                Object.assign({ granularity, setParam }, constructRangeParams)
            );

            ranges.push(range);
        }
    }
    const domain = Domain.combine(
        ranges.map((range) => range.domain),
        "OR"
    );
    const description = ranges.map((range) => range.description).join("/");
    return { domain, description };
}

export function constructDateRangeCustom(params) {
    const { referenceMoment, fieldName, fieldType, granularity, setParam, plusParam } = params;
    var temp_quarter
    if ("quarter" in setParam) {
        // Luxon does not consider quarter key in setParam (like moment did)
        setParam.month = QUARTERS[setParam.quarter].coveredMonths[0];
        if (setParam.quarter == 4){
            var temp_quarter = 4;
            setParam.year = setParam.year + 1
        }
        delete setParam.quarter;
    }
    const date = referenceMoment.set(setParam).plus(plusParam || {});
    // compute domain
    var leftDate = date.startOf(granularity);
    var rightDate = date.endOf(granularity);

    if (granularity == 'year'){
        var leftDate = date.startOf(granularity).plus({month: 3});
        var rightDate = date.endOf(granularity).plus({month: 3});
    }
    let leftBound;
    let rightBound;
    if (fieldType === "date") {
        leftBound = serializeDate(leftDate);
        rightBound = serializeDate(rightDate);
    } else {
        leftBound = serializeDateTime(leftDate);
        rightBound = serializeDateTime(rightDate);
    }
    const domain = new Domain(["&", [fieldName, ">=", leftBound], [fieldName, "<=", rightBound]]);
    // compute description
//    const descriptions = [date.toFormat("yyyy")];
    if (temp_quarter){
        var descriptions = [(parseInt(date.toFormat("yyyy")) -1) + '-' + date.toFormat("yyyy").toString().slice(-2)]
    }
    else {
        var descriptions = [date.toFormat("yyyy") + '-' + (parseInt(date.toFormat("yyyy")) + 1).toString().slice(-2)]
    }
    const method = localization.direction === "rtl" ? "push" : "unshift";
    if (granularity === "month") {
        descriptions[method](date.toFormat("MMMM"));
    } else if (granularity === "quarter") {
        var quarter = date.quarter;
        if (quarter === 1){
            quarter = 4
        }
        else if (quarter === 2){
            quarter = 1
        }
        else if (quarter === 3){
            quarter = 2
        }
        else if (quarter === 4){
            quarter = 3
        }
        descriptions[method](QUARTERS[quarter].description.toString());
    }
    const description = descriptions.join(" ");
    return { domain, description };
}

