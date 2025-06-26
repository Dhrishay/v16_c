/** @odoo-module **/

import { Domain } from "@web/core/domain";
import { makeContext } from "@web/core/context";
import { SearchModel } from "@web/search/search_model";
import { patch } from "@web/core/utils/patch";
import {constructDateDomainCustom} from '@cr_web_portal/js/dates'


patch(SearchModel.prototype, 'CustomSearchModel', {
    setup() {
        this._super.apply(this, arguments);
        this.optionGenerators.forEach(function(key) {
            if (key.id == 'this_year'){
                var this_year = parseInt(key.description) + 1
                key.description = key.description + '-' + this_year.toString().slice(-2)
            }
            else if (key.id == 'last_year'){
                var last_year = parseInt(key.description) + 1
                key.description = key.description + '-' + last_year.toString().slice(-2)
            }
            else if (key.id == 'antepenultimate_year'){
                var antepenultimate_year = parseInt(key.description) + 1
                key.description = key.description + '-' + antepenultimate_year.toString().slice(-2)
            }
	    });
    },

    getFullComparison() {
        let searchItem = null;
        for (const queryElem of this.query.slice().reverse()) {
            const item = this.searchItems[queryElem.searchItemId];
            if (item.type === "comparison") {
                searchItem = item;
                break;
            } else if (item.type === "favorite" && item.comparison) {
                searchItem = item;
                break;
            }
        }
        if (!searchItem) {
            return null;
        } else if (searchItem.type === "favorite") {
            return searchItem.comparison;
        }
        const { dateFilterId, comparisonOptionId } = searchItem;
        const { fieldName, fieldType, description: dateFilterDescription } = this.searchItems[
            dateFilterId
        ];
        const selectedGeneratorIds = this._getSelectedGeneratorIds(dateFilterId);
        // compute range and range description
        const { domain: range, description: rangeDescription } = constructDateDomainCustom(
            this.referenceMoment,
            fieldName,
            fieldType,
            selectedGeneratorIds
        );
        // compute comparisonRange and comparisonRange description
        const {
            domain: comparisonRange,
            description: comparisonRangeDescription,
        } = constructDateDomainCustom(
            this.referenceMoment,
            fieldName,
            fieldType,
            selectedGeneratorIds,
            comparisonOptionId
        );
        return {
            comparisonId: comparisonOptionId,
            fieldName,
            fieldDescription: dateFilterDescription,
            range: range.toList(),
            rangeDescription,
            comparisonRange: comparisonRange.toList(),
            comparisonRangeDescription,
        };
    },

    _getDateFilterDomain(dateFilter, generatorIds, key = "domain") {
        const { fieldName, fieldType } = dateFilter;
        const dateFilterRange = constructDateDomainCustom(
            this.referenceMoment,
            fieldName,
            fieldType,
            generatorIds
        );
        return dateFilterRange[key];
    }



})
