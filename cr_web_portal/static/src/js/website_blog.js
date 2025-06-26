odoo.define('cr_web_portal.website_blog', function (require) {
'use strict';

    var core = require('web.core');
    var config = require('web.config');
    var publicWidget = require('web.public.widget');

    publicWidget.registry.websiteBlog = publicWidget.Widget.extend({
        selector: '.website_blog',
        events: {
            'click #o_wblog_post_content_jump': '_onContentAnchorClick',
        },
        async start() {
            await this._super(...arguments);
        },
        _onContentAnchorClick: function (ev) {
            // do nothing only need this function for stop base '_onContentAnchorClick' function.
        },
    });
});