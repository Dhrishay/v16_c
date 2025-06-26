
odoo.define('cr_web_portal.price_range_attribute', function (require) {
'use strict';

var ajax = require('web.ajax');
var core = require('web.core');
var publicWidget = require('web.public.widget');
require('website_sale.website_sale');

var _t = core._t;
    publicWidget.registry.WebsiteSale.include({
        _onChangeAttribute: function (ev) {
            if(window.innerWidth <= 425 || window.innerWidth <= 435 && window.innerHeight <= 967 || window.innerWidth <= 434 && window.innerHeight == 847 || window.innerWidth <= 428 && window.innerHeight == 926 || window.innerWidth <= 430 && window.innerHeight == 932 || window.innerWidth <= 540 && window.innerHeight == 720 ){

            }else{
                if (!ev.isDefaultPrevented()) {
                    ev.preventDefault();
                    const productGrid = this.el.querySelector(".o_wsale_products_grid_table_wrapper");
                    if (productGrid) {
                        productGrid.classList.add("opacity-50");
                    }
                    const range = ev.currentTarget;
                    if(!$(range)[0].classList.contains('form-range')){
                        $(ev.currentTarget).closest("form").submit();
                    }
                }
            }
        },
    });
});

odoo.define('cr_web_portal.price_range_option', function (require) {
'use strict';

const publicWidget = require('web.public.widget');

    publicWidget.registry.multirangePriceSelector = publicWidget.Widget.extend({
        selector: '.o_wsale_products_page',
        events: {
            'newRangeValue #o_wsale_price_range_option input[type="range"]': '_onPriceRangeSelected',
        },
        _onPriceRangeSelected(ev) {
            const range = ev.currentTarget;
            const searchParams = new URLSearchParams(window.location.search);
            searchParams.delete("min_price");
            searchParams.delete("max_price");
            if (parseFloat(range.min) !== range.valueLow) {
                searchParams.set("min_price", range.valueLow);
            }
            if (parseFloat(range.max) !== range.valueHigh) {
                searchParams.set("max_price", range.valueHigh);
            }
            let product_list_div = this.el.querySelector('.o_wsale_products_grid_table_wrapper');
            if (product_list_div) {
                product_list_div.classList.add('opacity-50');
            }
            window.location.search = searchParams.toString();
        },
    });
});



