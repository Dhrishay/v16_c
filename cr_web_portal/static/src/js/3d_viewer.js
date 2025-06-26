odoo.define('cr_web_portal.3d_viewer', function (require) {
'use strict';

    var core = require('web.core');
    var config = require('web.config');
    var publicWidget = require('web.public.widget');

    publicWidget.registry.websiteSaleCarousel3dProduct = publicWidget.Widget.extend({
        selector: '.oe_website_sale',
        disabledInEditableMode: false,
        events: {
            'click .open_glb_viewer': '_onClickGLBBox',
//            'click .btn-left': '_onClickLeftBtn',
//            'click .btn-right': '_onClickRightBtn',
//            'click .btn-up': '_onClickTopBtn',
//            'click .btn-down': '_onClickBottomBtn',
//            'click .btn-reset': '_onClickResetBtn',
//            'click .btn-zoom-in': '_onClickZoomInBtn',
//            'click .btn-zoom-out': '_onClickZoomOutBtn',
        },

        async start() {
            await this._super(...arguments);
        },

        _onClickGLBBox: function (ev) {
            ev.preventDefault();
            $('#open_glb_viewer_box').modal('show');
        },
//        _onClickLeftBtn: function (ev) {
//            if($('model-viewer').length){
//                var old_val = $('model-viewer')[0].getCameraOrbit()
//                // convert into value radian into degree
//                var x_axis = (old_val['theta'] * (180/Math.PI) - 22.5).toString() + 'deg'
//                var y_axis = (old_val['phi'] * (180/Math.PI)).toString() + 'deg'
//                var zoom = (old_val['radius']).toString() + 'm'
//                $('model-viewer')[0].setAttribute('camera-orbit',x_axis+' '+y_axis+' '+zoom)
//            }
//
//        },
//        _onClickRightBtn: function (ev) {
//            if($('model-viewer').length){
//                var old_val = $('model-viewer')[0].getCameraOrbit()
//                // convert into value radian into degree
//                var x_axis = (old_val['theta'] * (180/Math.PI) + 22.5).toString() + 'deg'
//                var y_axis = (old_val['phi'] * (180/Math.PI)).toString() + 'deg'
//                var zoom = (old_val['radius']).toString() + 'm'
//                $('model-viewer')[0].setAttribute('camera-orbit',x_axis+' '+y_axis+' '+zoom)
//            }
//        },
//        _onClickTopBtn: function (ev) {
//            if($('model-viewer').length){
//                var old_val = $('model-viewer')[0].getCameraOrbit()
//                // convert into value radian into degree
//                var x_axis = (old_val['theta'] * (180/Math.PI)).toString() + 'deg'
//                var y_axis = (old_val['phi'] * (180/Math.PI) - 22.5).toString() + 'deg'
//                var zoom = (old_val['radius']).toString() + 'm'
//                $('model-viewer')[0].setAttribute('camera-orbit',x_axis+' '+y_axis+' '+zoom)
//            }
//        },
//        _onClickBottomBtn: function (ev) {
//            if($('model-viewer').length){
//                var old_val = $('model-viewer')[0].getCameraOrbit()
//                // convert into value radian into degree
//                var x_axis = (old_val['theta'] * (180/Math.PI)).toString() + 'deg'
//                var y_axis = (old_val['phi'] * (180/Math.PI) + 22.5).toString() + 'deg'
//                var zoom = (old_val['radius']).toString() + 'm'
//                $('model-viewer')[0].setAttribute('camera-orbit',x_axis+' '+y_axis+' '+zoom)
//            }
//        },
//        _onClickZoomInBtn: function (ev) {
//            if($('model-viewer').length){
//                $('model-viewer')[0].zoom(2.0)
//            }
//        },
//        _onClickZoomOutBtn: function (ev) {
//            if($('model-viewer').length){
//                $('model-viewer')[0].zoom(-2.0)
//            }
//        },
//        _onClickResetBtn: function (ev) {
//            if($('model-viewer').length){
//                $('model-viewer')[0].cameraOrbit = '0deg 60deg 105%'
//            }
//        },
    });

});


