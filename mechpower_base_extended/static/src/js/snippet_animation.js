/** @odoo-module */

import publicWidget from 'web.public.widget';
import { _t } from 'web.core';
import 'website.s_website_form';
import 'website.content.snippets.animation';
import dom from 'web.dom';
import ajax from "web.ajax";
import concurrency from 'web.concurrency';

publicWidget.registry.backgroundVideo.include({
     _triggerAutoplay: function (iframeEl) {
         if (this.isMobileEnv && this.isYoutubeVideo) {
             if (window.YT && window.YT.Player){
                 new window.YT.Player(iframeEl, {
                     events: {
                        onReady: ev => ev.target.playVideo(),
                     }
                 });
             }
         }
    }
});