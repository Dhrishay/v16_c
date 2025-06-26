odoo.define('cr_web_portal.script', function (require) {
"use strict";

  /*-------------------------------------
      Animation on scroll: Number rotator
  -------------------------------------*/
  $("[data-appear-animation]").each(function() {
      var self      = $(this);
      var animation = self.data("appear-animation");
      var delay     = (self.data("appear-animation-delay") ? self.data("appear-animation-delay") : 0);
        self.html('0');
        self.waypoint(function(direction) {
            if( !self.hasClass('completed') ){
                var from     = self.data('from');
                var to       = self.data('to');
                var interval = self.data('interval');
                self.numinate({
                    format: '%counter%',
                    from: from,
                    to: to,
                    runningInterval: 2000,
                    stepUnit: interval,
                    onComplete: function(elem) {
                        self.addClass('completed');
                    }
                });
            }
        }, { offset:'85%' });
  });

  /*-------------------------------------
  Swiper Slider
  -------------------------------------*/
  var swiperslider = $(".swiper-slider");
  var x = 1;
  swiperslider.each(function () {  
             var carouselElement	= $(this);
             var header_area =  $(this).closest('section').find( '.pbmit-ele-header-area');
              var columns = $(this).data('columns');
              var loop = $(this).data('loop');
              var autoplay2 = $(this).data('autoplay');
              var autoplayspeed1 = $(this).data('autoplayspeed'); 
              var val_nav = $(this).data('arrows');
              var nav_arrow = $(this).data('arrows-class');                
              var val_dots = $(this).data('dots');
              var val_center = $(this).data('center');
              var style = $(this).data('effect');
              var loopSlide = null; 
              var sl_speed = 2000; 
              var c_counter = false;

              jQuery('.pbmit-element-timeline-style-1 .swiper-slide:even').addClass('pbmit-slide-even');

              carouselElement.addClass( 'pbmit-element-viewtype-carousel-' + x );


              if( columns === 1 ){ 
                var responsive_items = [ /* 1199 : */ '1', /* 991 : */ '1', /* 767 : */ '1', /* 575 : */ '1', /* 0 : */ '1' ];
              } else if( columns === 2 ||  columns === 2.3 ){ 
                var responsive_items = [ /* 1199 : */ columns, /* 991 : */ '2', /* 767 : */ '2', /* 575 : */ '1', /* 0 : */ '1' ];
              } else if( columns === 3 ||  columns === 3.5 ){
                var responsive_items = [ /* 1199 : */ columns, /* 991 : */ '2', /* 767 : */ '2', /* 575 : */ '1', /* 0 : */ '1' ];
              } else if( columns === 4 ||  columns === 4.5 ){
                var responsive_items = [ /* 1199 : */ columns, /* 991 : */ '4', /* 767 : */ '3', /* 575 : */ '1', /* 0 : */ '1' ];
              } else if( columns === 5 ){
                var responsive_items = [ /* 1199 : */ '5', /* 991 : */ '4', /* 767 : */ '2', /* 575 : */ '1', /* 0 : */ '1' ];
              } else if( columns === 6 ){
                var responsive_items = [ /* 1199 : */ '6', /* 991 : */ '4', /* 767 : */ '3', /* 575 : */ '3', /* 0 : */ '1' ];
              }
              else if( columns === 8 ){
                var responsive_items = [ /* 1199 : */ '8', /* 991 : */ '6', /* 767 : */ '4', /* 575 : */ '3', /* 0 : */ '1' ];
              }
              else if( columns === 9 ){
                var responsive_items = [ /* 1199 : */ '9', /* 991 : */ '6', /* 767 : */ '4', /* 575 : */ '3', /* 0 : */ '1' ];
              } else {
                var responsive_items = [ /* 1199 : */ '3', /* 991 : */ '3', /* 767 : */ '1', /* 575 : */ '1', /* 0 : */ '1' ];
              }

			 
			  if (autoplay2 !== true) {
				 autoplay2 = false;
			   } else{
				autoplay2 =  { delay: 2000 };
			   }


			 
				
              if (val_dots === true) {
                carouselElement.append('<div class="swiper-pagination swiper-pagination"></div>');
              }
              if ( jQuery(carouselElement).hasClass('pbmit-element-testimonial-style-2') ) {
                  c_counter = true;
                  var totalslide = jQuery(carouselElement).find('article:not(".swiper-slide-duplicate")').length;
                  var cal = Math.round((1 * 100) / totalslide); 
                  header_area.append('<div class="pbmit-fld-contents"><div class="pbmit-circle-outer" data-digit="' + cal + '" data-fill="#b8967e" data-emptyfill="#f6f6f6" data-before=""  data-thickness="2" data-size="100"><div class="pbmit-circle"><div class="pbmit-fid-inner"></div></div></div></div>');
                   
                  var elm = jQuery(carouselElement).closest('section').find( '.pbmit-circle');
                  pbmit_circle_progressbar(); 
                  setTimeout(function() { updatecircle(elm, 1, totalslide); }, 100);
              }

              if(val_nav === true){
                 
                if(!nav_arrow){
                  carouselElement.append( '<div class="swiper-buttons"></div>' );
                  carouselElement.find('.swiper-buttons').append( '<div class="swiper-button-next swiper-button-next-' + x + '"></div>' );
                  carouselElement.find('.swiper-buttons').append( '<div class="swiper-button-prev swiper-button-prev-' + x + '"></div>' );
                }
//                else{
//                  $('.' + nav_arrow).append( '<div class="swiper-buttons"></div>' );
//                  $('.' + nav_arrow).append( '<div class="swiper-button-next swiper-button-next-' + x + '"></div>' );
//                  $('.' + nav_arrow).append( '<div class="swiper-button-prev swiper-button-prev-' + x + '"></div>' );
//                }
              }

              var pagination_val = false;
              if (val_dots === true) {
                  pagination_val = {
                      el: '.swiper-pagination',
                      clickable: true,
                  };
              }
              var navigation_val = false;
              if(val_nav === true){
                navigation_val =  {
                  nextEl: '.swiper-button-next-' + x,
                  prevEl: '.swiper-button-prev-' + x,
                };
              }


              if(!style){
                style = "slide";
              }    
              
              var margin_val = 30;
              if( $(carouselElement).data('margin') !== '' || $(carouselElement).data('margin') === '0'){
                margin_val = $(carouselElement).data('margin');  
              } 
            
              if(carouselElement.hasClass('marquee')){ 
                var reverse_direction = $(this).data('reverse');
                if (!reverse_direction) reverse_direction = false;
                 var swiper2 = new Swiper( '.pbmit-element-viewtype-carousel-' + x, { 
                   spaceBetween: 0,
                   centeredSlides: true,
                   speed: 5000,
                   autoplay: {
                       delay: 1,
                       disableOnInteraction: true,
                       reverseDirection: reverse_direction,
                   },
                   loop: true,
                   slidesPerView: 'auto',
                   allowTouchMove: false,
                   disableOnInteraction: true
               }); 

              
             } else{          
              var numOfSlides;         
            var swiper = new Swiper( '.pbmit-element-viewtype-carousel-' + x, { 
                loop: loop,
                navigation: navigation_val,
                pagination: pagination_val,
                slidesPerView: columns,
                spaceBetween: margin_val,
                loopedSlides: loopSlide,
                effect: style,
				autoplay:autoplay2,
                speed: sl_speed,
                grabCursor: false,
                centeredSlides: val_center,
                breakpoints		  : {
                  1199 : {
                    slidesPerView	: responsive_items[0],
                  },
                  991	 : {					
                    slidesPerView	: responsive_items[1],
                  },
                  767	 : {
                    slidesPerView	: responsive_items[2],
                  },
                  575	 : {
                    slidesPerView	: responsive_items[3],
                  },
                  0	 : {
                    slidesPerView	: responsive_items[4],
                  }
                             
              },
              on: {
                slideChange: function(swiper) {
                    if (c_counter) { 
                        var elm = jQuery(carouselElement).closest('section').find( '.pbmit-circle');
                        var current = swiper.realIndex + 1;
                        updatecircle(elm, current, numOfSlides);
                    }
                },
                beforeInit: function(){
                    numOfSlides = jQuery('.pbmit-element-viewtype-carousel-' + x + ' .swiper-slide').length;
                }
              }
            }); 
            if (jQuery('.pbmit-element-viewtype-carousel-' + x).hasClass('pbmit-element-testimonial-style-1') || jQuery('.pbmit-element-viewtype-carousel-' + x).hasClass('pbmit-element-testimonial-style-2') || jQuery('.pbmit-element-viewtype-carousel-' + x).hasClass('pbmit-element-testimonial-style-10')) {
                var pbmit_var = jQuery('.pbmit-element-viewtype-carousel-' + x);                 
                pbmit_var.find('.swiper-button-next').attr('data-cursor-text', '<i class="pbmit-base-icon-right-open"></i>');
                pbmit_var.find('.swiper-button-prev').attr('data-cursor-text', '<i class="pbmit-base-icon-left-open"></i>');
            }

          }
            x = x + 1;             
        });
    function updatecircle(elm, cr, tl) {
        var cal = getpercentage(tl, cr, elm); 
        var short_digit = cal / 100;
        elm.circleProgress('value', short_digit);
    }

  

/* ====================================== */
/* Circle Progress bar
/* ====================================== */
 function pbmit_circle_progressbar() {

  jQuery('.pbmit-circle-outer').each(function() {

      var this_circle = jQuery(this);

      // Circle settings
      var emptyFill_val = "rgba(0, 0, 0, 0)";
      var thickness_val = 10;
      var fill_val = this_circle.data('fill');
      var size_val = 110;

      if (typeof this_circle.data('emptyfill') !== 'undefined' && this_circle.data('emptyfill') != '') {
          emptyFill_val = this_circle.data('emptyfill');
      }
      if (typeof this_circle.data('thickness') !== 'undefined' && this_circle.data('thickness') != '') {
          thickness_val = this_circle.data('thickness');
      }
      if (typeof this_circle.data('size') !== 'undefined' && this_circle.data('size') != '') {
          size_val = this_circle.data('size');
      }
      if (typeof this_circle.data('filltype') !== 'undefined' && this_circle.data('filltype') == 'gradient') {
          fill_val = { gradient: [this_circle.data('gradient1'), this_circle.data('gradient2')], gradientAngle: Math.PI / 4 };
      }

      if (typeof jQuery.fn.circleProgress == "function") {
          var digit = this_circle.data('digit');
          var before = this_circle.data('before');
          var after = this_circle.data('after');
          var digit = Number(digit);
          var short_digit = (digit / 100);

          jQuery('.pbmit-circle', this_circle).circleProgress({
              value: 0,
              size: size_val,
              startAngle: -Math.PI / 4 * 2,
              thickness: thickness_val,
              emptyFill: emptyFill_val,
              fill: fill_val
          }).on('circle-animation-progress', function(event, progress, stepValue) { // Rotate number when animating
              this_circle.find('.pbmit-circle-number').html(before + Math.round(stepValue * 100) + after);
          });
      }

      this_circle.waypoint(function(direction) {
          if (!this_circle.hasClass('completed')) {
              // Re draw when view
              if (typeof jQuery.fn.circleProgress == "function") {
                  jQuery('.pbmit-circle', this_circle).circleProgress({ value: short_digit });
              };
              this_circle.addClass('completed');
          }
      }, { offset: '85%' });

  });
} 

   /*-------------------------------------
    Contact form validator
    -------------------------------------*/
    
    if ( $.isFunction($.fn.validate) ) {
      $("#contact-form").validate();
    }


    /*-------------------------------------
     Send email via Ajax
   Make sure you configure send.php file 
     -------------------------------------*/
//    $("#contact-form").submit(function(){
//
//   if( $("#contact-form .doing-via-ajax").length == 0 ){
//     $("#contact-form").prepend('<input class="doing-via-ajax" type="hidden" name="doing-via-ajax" value="yes" />');;
//   }
//
////   if( $("#contact-form").valid() ){  // check if form is valid
////
////     $(".contact-form .message-status").html('');
////     $('.form-btn-loader').removeClass('d-none');
////     $('.contact-form button.pbmit-btn span').hide();
////     $('.contact-form button.pbmit-btn').attr("disabled", "disabled");
////
////     $.ajax( {
////       type: "POST",
////       url: "send.php",
////       data:$('#contact-form').serialize(),
////       success: function(cevap) {
////         $('.form-btn-loader').addClass('d-none');
////         $('.contact-form button.pbmit-btn span').show();
////         $(".contact-form button.pbmit-btn").removeAttr("disabled");
////         $(".contact-form .message-status").html(cevap);
////       }
////     });
////
////   }
//
//   return false;
//
//   });

  /*-------------------------------------
    Masonry
  -------------------------------------*/
 
	if (jQuery('.pbmit-element-viewtype-masonry').length > 0) {
		jQuery('.pbmit-element-viewtype-masonry').each(function() {

			var main_ele = jQuery(this); 			
			// init Masonry
			let $grid = jQuery('.pbmit-element-posts-wrapper', main_ele).masonry({
				
				itemSelector: '.pbmit-portfolio-style-4, .pbmit-blog-style-1',
				columnWidth: '.pbmit-portfolio-style-4, .pbmit-blog-style-1',
				gutter: 0,
				percentPosition: true,
				stagger: 30,
				// nicer reveal transition
				visibleStyle: { transform: 'translateY(0)', opacity: 1 },
				hiddenStyle: { transform: 'translateY(100px)', opacity: 0 },
				horizontalOrder: true
			});
			 
		}
		)};

  /*-------------------------------------
  ProgressBar
  -------------------------------------*/
  AOS.init({
    once: true,
  });

  /*-------------------------------------
  Scroll To Top
  -------------------------------------*/

//  var pbmit_back_to_top = function() {
//    var progressPath = document.querySelector('.pbmit-progress-wrap path');
//      var pathLength = progressPath.getTotalLength();
//      progressPath.style.transition = progressPath.style.WebkitTransition = 'none';
//      progressPath.style.strokeDasharray = pathLength + ' ' + pathLength;
//      progressPath.style.strokeDashoffset = pathLength;
//      progressPath.getBoundingClientRect();
//      progressPath.style.transition = progressPath.style.WebkitTransition = 'stroke-dashoffset 10ms linear';
//      var updateProgress = function() {
//          var scroll = jQuery(window).scrollTop();
//          var height = jQuery(document).height() - jQuery(window).height();
//          var progress = pathLength - (scroll * pathLength / height);
//          progressPath.style.strokeDashoffset = progress;
//      }
//      updateProgress();
//      jQuery(window).scroll(updateProgress);
//      var offset = 50;
//      var duration = 550;
//      jQuery(window).on('scroll', function() {
//          if (jQuery(this).scrollTop() > offset) {
//              jQuery('.pbmit-progress-wrap').addClass('active-progress');
//          } else {
//              jQuery('.pbmit-progress-wrap').removeClass('active-progress');
//          }
//      });
//      jQuery('.pbmit-progress-wrap').on('click', function(event) {
//          event.preventDefault();
//          jQuery('html, body').animate({ scrollTop: 0 }, duration);
//          return false;
//      })
//  }
//  pbmit_back_to_top();



  /* Static Box Slider */
var pbmit_staticbox_hover_slide = function() {
	if (typeof Swiper !== 'undefined') {
		var pbmit_hover1 = new Swiper(".pbmit-static-image", {
			grabCursor: true,
			effect: "slide",
			allowTouchMove: false,
			slidesPerView:1
		});
		var pbmit_hover2 = new Swiper(".pbmit-hover-short-desc", {
			grabCursor: true,
			effect: "creative",
			creativeEffect: {
				prev: {
					translate: [0, "-170%", 1],
				},
				next: {
					translate: [0, "100%", 0],
				},
			},
			allowTouchMove: false
		});
		jQuery('.pbmit-main-static-slider li').hover(function(e) {
			e.preventDefault();
			var myindex = jQuery(this).index();
			pbmit_hover1.slideTo(myindex, 500, false);
			pbmit_hover2.slideTo(myindex, 500, false);
		});
	}
}
pbmit_staticbox_hover_slide();

var pbmit_hover_slide = function() {
	if (typeof Swiper !== 'undefined') {
		var pbmit_hover1 = new Swiper(".pbmit-hover-image", {
			grabCursor: true,
			effect: "slide",
			allowTouchMove: false
		});
    var pbmit_hover2 = new Swiper(".pbmit-short-description", {
			grabCursor: true,
			effect: "creative",
			creativeEffect: {
				prev: {
					translate: [0, "-170%", 1],
				},
				next: {
					translate: [0, "100%", 0],
				},
			},
			allowTouchMove: false
		});
	}
  
	jQuery('.pbmit-main-hover-slider li').hover(function(e) {
		e.preventDefault();
		var myindex = jQuery(this).index();
		pbmit_hover1.slideTo(myindex, 500, false);
		pbmit_hover2.slideTo(myindex, 500, false);
	});
}
pbmit_hover_slide();
var pbmit_service_bg_hover = function() {
	var pbmit_hover;
	if (typeof Swiper !== 'undefined') {
		pbmit_hover = new Swiper(".pbmit-hover-image-faded", {
			speed: 6000,
			effect: 'fade',
		});
	}
	jQuery('.pbmit-main-hover-faded li').hover(function(e) {
		e.preventDefault();
		var myindex = jQuery(this).index();
		pbmit_hover.slideTo(myindex, 1000, false);
	});
}
pbmit_service_bg_hover();
  /*-------------------------------------
  Header Search Form
  -------------------------------------*/
  $(".pbmit-search-overlay").on('click', function() {
        $(".pbmit-search-close").click()
  });
  $( ".pbmit-header-search-btn a" ).on('click', function() {
    $(".pbmit-search-overlay").addClass('st-show');
    $("body").addClass('st-prevent-scroll');            
    return false;
  });   
  $( ".pbmit-search-close").on('click', function() {
        $(".pbmit-search-overlay").removeClass('st-show');
      $("body").removeClass('st-prevent-scroll');            
      return false;
  }); 
  $('.pbmit-site-searchform').on('click', function(event){
    event.stopPropagation();
  });

  /*-------------------------------------
  Sticky Header
  -------------------------------------*/ 
  $(window).scroll(function(){
    var sticky = $('.sticky-menu'),
    scroll = $(window).scrollTop();
    if (scroll >= 90) sticky.addClass('sticky-header');
    else sticky.removeClass('sticky-header');
  });

  	 /*-------------------------------------
    Stretched Div
    -------------------------------------*/ 	
    var document_width = $(document).width();
      function pbmit_col_stretched(){
        $('.pbmit-col-stretched-yes').each(function() {
          var this_ele = $(this);
          var window_width = jQuery(window).width();
          var main_width = $('.container').width();
          var extra_width = ((window_width - main_width) / 2);  
          if (window_width < 1200){
            extra_width = 0;
          }
          if (this_ele.hasClass('pbmit-col-right')) { 
            $('.pbmit-col-stretched-right', this_ele).css('margin-right', '-' + extra_width + 'px'); 
          } else { 
            $('.pbmit-col-stretched-left', this_ele).css('margin-left', '-' + extra_width + 'px'); 
          }
        });
      }
      $(window).resize(function(){
        pbmit_col_stretched();
      });
      pbmit_col_stretched();
  
  /*-------------------------------------
  Count Down
  -------------------------------------*/ 

  if( $('#clock').length>0 ){
    $('#clock').countdown('2024/10/10', function(event) {
      $(this).html(event.strftime(''
      + '<div class="conut-time"><span class="time_left">86</span><span class="time_description">Day%!d </span></div>'
      + '<div class="conut-time"><span class="time_left">05</span><span class="time_description"> Hours </span></div> '
      + '<div class="conut-time"><span class="time_left">33</span><span class="time_description"> Minutes </span></div>'
      + '<div class="conut-time"><span class="time_left">%S</span><span class="time_description"> Seconds </span></div>'
      ));
    });
  }

  /*-------------------------------------
  Count Down
  -------------------------------------*/ 
  var pbmit_icon_box_hover_effect = function() {
    jQuery(".active-onhover .pbmit-element-posts-wrapper .pbmit-ele-miconheading , .active-onhover .elementor-inner-section .elementor-container .elementor-inner-column:nth-child(2)").eq(0).addClass('pbmit-ihbox-hover-active');
    jQuery(".active-onhover .pbmit-element-posts-wrapper .pbmit-ele-miconheading , .active-onhover .elementor-inner-section .elementor-container .elementor-inner-column").mouseover(function() {
      var main_row = jQuery(this).closest('.active-onhover');
      jQuery('.pbmit-ele-miconheading , .elementor-inner-column', main_row).removeClass('pbmit-ihbox-hover-active');
      jQuery(this).addClass('pbmit-ihbox-hover-active');
    });
  }
  pbmit_icon_box_hover_effect();

  var pbmit_multi_icon_box_hover_effect = function() {
    jQuery(".active-onhover .pbmit-miconheading-style-15:nth-child(2), .pbmit-miconheading-style-3:nth-child(2), .pbmit-miconheading-style-1:nth-child(2)").eq(0).addClass('pbmit-mihbox-hover-active');
    jQuery(".active-onhover .pbmit-miconheading-style-15, .pbmit-miconheading-style-3, .pbmit-miconheading-style-1").mouseover(function() {
      var main_row = jQuery(this).closest('.active-onhover ');
      jQuery('.pbmit-miconheading-style-15, .pbmit-miconheading-style-3, .pbmit-miconheading-style-1', main_row).removeClass('pbmit-mihbox-hover-active');
      jQuery(this).addClass('pbmit-mihbox-hover-active');
    }).mouseout(function() {
      var main_row = jQuery(this).closest('.active-onhover');
      jQuery('.pbmit-miconheading-style-15, .pbmit-miconheading-style-3, .pbmit-miconheading-style-1', main_row).removeClass('pbmit-mihbox-hover-active');
      jQuery(this).addClass('pbmit-mihbox-hover-active');
    });
  }
  pbmit_multi_icon_box_hover_effect();

  /*-------------------------------------
    tooltip
  -------------------------------------*/
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
      var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
      return new bootstrap.Tooltip(tooltipTriggerEl)
    })
    
  /*-------------------------------------
    Mobile Menu
  -------------------------------------*/     
  $('.navbar-toggler,.closepanel').on('click', function () { 
    jQuery("header").toggleClass("active");
  }); 

  /*-------------------------------------
  Magnific Popup
  -------------------------------------*/
  var i_type = 'image';
  $('.pbmit-lightbox-video, .pbmit-lightbox-video a, a.pbmit-lightbox').each(function(){
      if( $(this).hasClass('pbmit-lightbox-video')){ 
        i_type = 'iframe';
      } else {
        i_type = 'image';
      }  
      $(this).magnificPopup({type:i_type});
  });   

     /*-------------------------------------
  Magnific Popup
  -------------------------------------*/
    $('.pbmit-nav-menu-toggle').on('click', function() {
      $(".floting-bar-wrap").toggleClass("active");
    })
    $('.floting-bar-wrap .closepanel').on('click', function() {
      $(".floting-bar-wrap").toggleClass("active");
    });

  /*-------------------------------------
   Accordion
  -------------------------------------*/

  $('.accordion .accordion-item').on('click', function () { 
    var e = $(this);  
    $(this).parent().find('.accordion-item').removeClass('active');        
    if(!$(this).find('.accordion-button').hasClass('collapsed')){
      $(this).addClass('active');
    }  
  }); 

  /*-------------------------------------
  Add Arrow Down icon in menu
  -------------------------------------*/
  if(screen.width > 444){
    if($(".width-hide-show")){
        if($(".width-hide-show").length > 0){
            $(".width-hide-show")[0].classList.add('d-none');
        }
    }
  }
  else{
    if($(".width-hide-show")){
        if($(".width-hide-show").length > 0){
             $(".width-hide-show")[0].classList.remove('d-none');
        }
    }
    $('.hide-card').remove();
  }





  /*-------------------------------------
  Responsive Menu

  -------------------------------------*/



    $('.righticon.for-laptop-view.extra-icon').on('click', function(event) {
        event.preventDefault();
        event.stopPropagation();
         if(!$(this).siblings().hasClass('open')){

//            if(!$(this)[0].previousElementSibling.previousElementSibling.classList.contains('resouces')){
//                 $(this).css("padding-right","20px");
//            }
      }else{

//             if(!$(this)[0].previousElementSibling.previousElementSibling.classList.contains('resouces')){
//                 $(this).css("padding-right","0px");
//            }
      }

         $(this).parent().siblings().toggleClass('open');
         $(this).find('i').toggleClass('ti-angle-up ti-angle-up');
         return false;
    });

    $(".check_digits").keypress(function(){
        var key = event.keyCode;
        if (![48,49,50,51,52,53,54,55,56,57,58].includes(key) || this.value.length + 1 > 10) { // 0-9
            event.preventDefault();
        }
    });
    $(".check_digits_quantity").keypress(function(){
        var key = event.keyCode;
        if (![48,49,50,51,52,53,54,55,56,57,58].includes(key)) { // 0-9
            event.preventDefault();
        }
    });

    $(".check_digits_quantity").blur(function(event){
        var quantity = event.currentTarget.value;
        if (quantity <= 0){
           $(".pbmit-btn").attr('disabled', true);
           $(".check-digit-message").removeClass('d-none')
//           $(".check-digit-message")[0].childNodes[1].innerText = 'Should be enter greator than 0';
           if($("form.industry_segment_validation").length > 0){
                if($("form.industry_segment_validation").find('.pbmit-btn').length > 0){
                    $("form.industry_segment_validation").find('.pbmit-btn')[0].classList.remove('industry_segment_btn');
                }
             }
        }
        else{
           $(".pbmit-btn").attr('disabled', false);
           $(".check-digit-message").addClass('d-none')
           if($("form.industry_segment_validation").length > 0){
                if($("form.industry_segment_validation").find('.pbmit-btn').length > 0){
                    $("form.industry_segment_validation").find('.pbmit-btn')[0].classList.add('industry_segment_btn');
                }
             }
        }
    });

    $('a#dropdown-menus').on('click', function() {
      if(!$(this).siblings().hasClass('open')){

//            if(!$(this)[0].previousElementSibling.previousElementSibling.classList.contains('resouces')){
//                 $(this).css("padding-right","20px");
//            }
      }else{

//             if(!$(this)[0].previousElementSibling.previousElementSibling.classList.contains('resouces')){
//                 $(this).css("padding-right","0px");
//            }
      }
         $(this).siblings().toggleClass('open');
         $(this).find('i').toggleClass('ti-angle-up ti-angle-up');
         return false;
  });



  /*-------------------------------------
  Sortable Div
  -------------------------------------*/

  jQuery('.pbmit-sortable-yes').each(function(){ 
    var boxes = jQuery('.pbmit-element-posts-wrapper', this ); 
    var links = jQuery('.pbmit-sortable-list a', this ); 
    boxes.isotope({ animationEngine : 'best-available'}); 
    links.on('click', function(e){  
      var selector = jQuery(this).data('sortby'); 
      if( selector != '*' ){ 
        var selector = '.' + selector; 
      } 
      boxes.isotope({ filter : selector, itemSelector : '.pbmit-ele', layoutMode : 'fitRows' }); 
      links.removeClass('pbmit-selected');
      jQuery(this).addClass('pbmit-selected');
      e.preventDefault(); 
    });
  }); 

  /*-------------------------------------
  Circle Progressbar
  -------------------------------------*/
  $('.pbmit-circle-outer').each(function() {

    var this_circle = $(this);

    // Circle settings
    var emptyFill_val = "rgba(0, 0, 0, 0)";
    var thickness_val = 10;
    var fill_val = this_circle.data('fill');
    var size_val = 110;

    if (typeof this_circle.data('emptyfill') !== 'undefined' && this_circle.data('emptyfill') !== '') {
        emptyFill_val = this_circle.data('emptyfill');
    }
    if (typeof this_circle.data('thickness') !== 'undefined' && this_circle.data('thickness') !== '') {
        thickness_val = this_circle.data('thickness');
    }
    if (typeof this_circle.data('size') !== 'undefined' && this_circle.data('size') !== '') {
        size_val = this_circle.data('size');
    }
    if (typeof this_circle.data('filltype') !== 'undefined' && this_circle.data('filltype') === 'gradient') {
        fill_val = { gradient: [this_circle.data('gradient1'), this_circle.data('gradient2')], gradientAngle: Math.PI / 4 };
    }

    if (typeof $.fn.circleProgress === "function") {
        var digit = this_circle.data('digit');
        var before = this_circle.data('before');
        var after = this_circle.data('after');
        var digit = Number(digit);
        var short_digit = (digit / 100);

        $('.pbmit-circle', this_circle).circleProgress({
            value: 0,
            size: size_val,
            startAngle: -Math.PI / 4 * 2,
            thickness: thickness_val,
            emptyFill: emptyFill_val,
            fill: fill_val
        }).on('circle-animation-progress', function(event, progress, stepValue) { // Rotate number when animating
            this_circle.find('.pbmit-circle-number').html(before + Math.round(stepValue * 100) + after);
        });
    }
    
    this_circle.waypoint(function(direction) {
        if (!this_circle.hasClass('completed')) {
            // Redraw when view
            if (typeof $.fn.circleProgress === "function") {
                $('.pbmit-circle', this_circle).circleProgress({ value: short_digit });
            };
            this_circle.addClass('completed');
        }
    }, { offset: '85%' });

});

});

var pbmit_burger_menu = function() {
	if (jQuery('.header-style-8,.header-style-9,.header-style-12,.header-style-13').length > 0) {


		jQuery('.header-style-8 .pbmit-header-overlay .pbmit-logo-menuarea,.header-style-9 .pbmit-header-overlay .pbmit-logo-menuarea,.header-style-12 .pbmit-header-overlay .pbmit-logo-menuarea,.header-style-13 .pbmit-header-overlay .pbmit-logo-menuarea').clone().appendTo('.pbmit-burger-headerarea');
		jQuery('.header-style-8 .pbmit-header-overlay .pbmit-search-cart-box,.header-style-9 .pbmit-header-overlay .pbmit-search-cart-box,.header-style-12 .pbmit-header-overlay .pbmit-search-cart-box,.header-style-13 .pbmit-header-overlay .pbmit-search-cart-box').clone().appendTo('.pbmit-burger-headerarea');

		
		jQuery('.header-style-8 .pbmit-header-overlay .main-navigation,.header-style-9 .pbmit-header-overlay .main-navigation,.header-style-12 .pbmit-header-overlay .main-navigation,.header-style-13 .pbmit-header-overlay .main-navigation').clone().appendTo( '.pbmit-burger-menu-area-inner' ).insertBefore(".pbmit-burger-content");
		jQuery('.pbmit-burger-menu-area .main-navigation, .pbmit-burger-menu-area .main-navigation ul, .pbmit-burger-menu-area .main-navigation ul li, .pbmit-burger-menu-area .main-navigation ul li a').removeAttr('id');

		jQuery('.pbmit-burger-menu-area .main-navigation').removeClass('pbmit-navbar');
		jQuery('.pbmit-burger-menu-area .sub-menu-toggle').remove();

		jQuery('.pbmit-burger-menu-area ul.menu li:has(ul) > a').after("<span class='sub-menu-toggle'><i class='pbmit-base-icon-down-open-big'></i></span>");

		jQuery('.pbmit-burger-menu-area .sub-menu-toggle').on('click', function() {

			if (jQuery(this).siblings('.sub-menu, .children').css('display') == 'block'){			
				jQuery(this).siblings('.sub-menu, .children').slideUp();
				jQuery('i', jQuery(this)).removeClass('pbmit-base-icon-up-open-big').addClass('pbmit-base-icon-down-open-big');
			} else {
				jQuery(this).siblings('.sub-menu, .children').slideDown();
				jQuery('i', jQuery(this)).removeClass('pbmit-base-icon-down-open-big').addClass('pbmit-base-icon-up-open-big');
			}
			return false;
		});

		jQuery('.pbmit-burger-menu-link').click(function() {
			jQuery('.pbmit-burger-menu-area').addClass('show');
			jQuery('body').addClass('body-overflow-hidden');
		});

		jQuery('.pbmit-burger-menu-area .pbmit-closepanel').click(function() {
			jQuery('.pbmit-burger-menu-area').removeClass('show');
			jQuery('body').removeClass('body-overflow-hidden');
		});

	}
}
pbmit_burger_menu();



// let card = document.querySelector(".card");
// let displayPicture = document.querySelector(".display-picture"); 

// displayPicture.addEventListener("click", function() { 
// card.classList.toggle("hidden")})







