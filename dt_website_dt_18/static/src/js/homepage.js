/** @odoo-module **/

import publicWidget from "@web/legacy/js/public/public_widget";
import { ConfirmationDialog } from "@web/core/confirmation_dialog/confirmation_dialog";
import { _t } from "@web/core/l10n/translation";
import { rpc } from "@web/core/network/rpc";

publicWidget.registry.DashBoard = publicWidget.Widget.extend({
    selector: '.dashboards-section .collection-list-wrapper, #wrapwrap',
    events: {
        'click label.filter-checkbox': '_onFilterChange',
    },

    init() {
        this._super(...arguments);
        this.dialog = this.bindService("dialog");
    },

    _labelActive(ev) {
        ev.stopPropagation();
        ev.preventDefault();
        var $label = $(ev.currentTarget);
        var flag_active = $label.hasClass('is-active');
        if (flag_active) {
            $label.removeClass('is-active');
            $label.find('.w-checkbox-input').removeClass('w--redirected-checked');
        } else {
            $label.addClass('is-active');
            $label.find('.w-checkbox-input').addClass('w--redirected-checked');
        }
    },

    _onFilterChange: function (ev) {
        this._labelActive(ev);
        var selectedCategories = [];
        $('.w--redirected-checked').each(function (ev) {
            var categoryId = $(this).closest('label').find('input').data('id');
            selectedCategories.push(categoryId);
        });

        this._fetchDashboards(selectedCategories);
    },

    _fetchDashboards: function (category_ids) {
        var self = this;
        console.time('RPC Time');

        rpc("/dashboard/filter", {
            category_ids: category_ids
        }).then(function (result) {
            console.timeEnd('RPC Time');
            $('#dashboard-list').empty();
            if (result.length > 0) {
                result.forEach(function (dashboard) {
                    var card = `<div class="collection-item w-dyn-item w-col">
                        <a href="${dashboard.url}" target="_blank" class="link-block w-inline-block">
                            <img src="data:image/png;base64,${dashboard.image}" class="image-32"/>
                            <div class="solutions-card-top">
                                <h2 class="heading2 is-gradient">${dashboard.name}</h2>
                                <img src="/website_dt/static/src/images/purple-right-arrow.svg"/>
                            </div>
                            <p class="cms-dash-text is-tablet">${dashboard.description}</p>
                            <div class="categories">
                                ${dashboard.categories.map(cat => `<div class="category">${cat}</div>`).join('')}
                            </div>
                        </a>
                    </div>`;
                    $('#dashboard-list').append(card);
                });
            } else {
                $('#dashboard-list').html('<p>No dashboards found</p>');
            }
        });
    },
});

$(document).ready(function () {
    $(".feature-nav a").on("click", function (event) {
        event.preventDefault();
        var target = $(this).attr("href");

        $(".feature-nav a").removeClass("active");

        $(this).addClass("active");

        $("html, body").animate(
            {
                scrollTop: $(target).offset().top - 60,
            },
            800
        );
    });

    $(window).on("scroll", function () {
        let scrollPos = $(window).scrollTop();

        $(".suite-of-feature h2").each(function () {
            var sectionTop = $(this).offset().top - 100;
            var sectionId = $(this).attr("id");

            if (scrollPos >= sectionTop) {
                $(".feature-nav a").removeClass("active");
                $('.feature-nav a[href="#' + sectionId + '"]').addClass("active");
            }
        });
    });

    let normalHeader = $(".header");
    let stickyHeader = $(".header-sticky");
    var featureSection = $("#features");

    function updateHeaderVisibility() {
        var scrollTop = $(window).scrollTop();
        var featureTop = featureSection.offset().top;
        
        if (scrollTop > 350) {
            if (scrollTop >= featureTop - 100) { 
                stickyHeader.fadeOut(100, function () {
                    $(this).addClass("d-none");
                });
            } else {
                if (!stickyHeader.is(":visible")) {
                    normalHeader.fadeOut(100, function () {
                        $(this).addClass("d-none");
                        stickyHeader.removeClass("d-none").hide().fadeIn(100);
                    });
                }
            }
        } else {
            if (!normalHeader.is(":visible")) {
                stickyHeader.fadeOut(100, function () {
                    $(this).addClass("d-none");
                    normalHeader.removeClass("d-none").hide().fadeIn(100);
                });
            }
        }
    }

    if (window.location.pathname === "/") {
        $(window).on("scroll", updateHeaderVisibility);
    }

    $('.feature-tooltip').tooltip({
        title: `<p>
            You'll receive access to the Sandbox with a sample database and three sample dashboards. Please contact us if you need the training or additional functionality.
        </p>`,
        html: true,
        placement: 'top',
        container: '.feature-footer',
    });

    function checkForm() {
        $('form').each(function () { // Loop through each form on the page
            let isValid = true;
            let form = $(this);

            form.find('input, select').each(function () {
                if ($(this).prop('required')) {
                    if ($(this).is(':checkbox, :radio')) {
                        if (!$(this).is(':checked')) {
                            isValid = false;
                        }
                    } else if (!$(this).val()) {
                        isValid = false;
                    }
                }
            });

            if (isValid) {
                form.find('.btn-submit').removeClass('disabled'); // Only affect buttons inside the same form
            } else {
                form.find('.btn-submit').addClass('disabled');
            }
        });
    }


    $(".try-btn, .try-button").on("click", function (e) {
    // Trigger check on input/select change
        $('.access-form input').on('input', checkForm);  // For text input
        $('.access-form select').on('change', checkForm); // For dropdowns
    });
    // Initial check in case fields are pre-filled
    checkForm();

    $(".btn-submit.sandbox").on("click", function (e) {
        e.preventDefault(); // Prevent default form submission

        var form = $(e.currentTarget).closest('form');
        var formData = form.serialize(); // Get form data

        $.ajax({
            type: "POST",
            url: "/create/access", // Call Odoo controller
            data: formData,
            success: function (response) {
                var jsonResponse = JSON.parse(response);
                if (jsonResponse.success) {
                    $("#sandboxAccessModal").modal("hide"); // Close current modal
                    $("#sandboxAccessThankyou").modal("show"); // Show Thank You modal
                } else {
                    alert("Error: " + jsonResponse.message);
                }
            },
            error: function () {
                alert("An error occurred. Please try again.");
            },
        });
    });

    $(".btn-submit.newsletter").on("click", function (e) {
        var form = $(e.currentTarget).closest('form');
        var formData = form.serialize(); // Get form data

        $.ajax({
            type: "POST",
            url: "/create/subscription", // Call Odoo controller
            data: formData,
            success: function (response) {
                var jsonResponse = JSON.parse(response);
                if (jsonResponse.success) {
                    $("#subscribeToOurNewsletter").modal("hide"); // Close current modal
                    $("#NewsletterThankyou").modal("show"); // Show Thank You modal
                } else {
                    alert("Error: " + jsonResponse.message);
                }
            },
            error: function () {
                alert("An error occurred. Please try again.");
            },
        });
        e.preventDefault(); // Prevent default form submission
    });

    $('.nav-burger-lottie').on('click', function () {
        const $menu = $('.nav-menu');
        const $burger = $(this);
        const isOpen = $burger.hasClass('open');

        if (isOpen) {
            // Close state (burger icon)
            $burger.find('path').eq(0).attr('d', 'M324,-250 C324,-250 3,-250 3,-250 C3,-250 -324,-250 -324,-250');
            $burger.find('path').eq(1).attr('d', 'M-324,250 C-324,250 3,250 3,250 C3,250 324,250 324,250');
            $burger.find('path').eq(2).attr('d', 'M-324,0 C-324,0 324,0 324,0');
            $menu.css({
                'opacity': '0',
                'transition': 'opacity 0.3s ease'
            });
            setTimeout(() => $menu.css('display', 'none'), 300); // Hide after fade out
        } else {
            // Open state (cross icon)
           $burger.find('path').eq(0).attr('d', ' M230,-230 C230,-230 0,0 0,0 C0,0 -228,-228 -228,-228');
            $burger.find('path').eq(1).attr('d', ' M-230,230 C-230,230 -1,1 -1,1 C-1,1 230,230 230,230');
            $burger.find('path').eq(2).attr('d', 'M0 0');
            $burger.css({
                'transition': 'opacity 0.3s ease'
            });
            $menu.css({
                'display': 'flex',
                'opacity': '1',
                'transition': 'opacity 0.3s ease'
            });
        }

        $burger.toggleClass('open');
    });

    const eurButton = $('#switchEur');
    const gbpButton = $('#switchGbp');
    const mobeurButton = $('#mobileswitchEur');
    const mobgbpButton = $('#mobileswitchGbp');

    eurButton.on('click', function() {
        eurButton.addClass('is-active');
        gbpButton.removeClass('is-active');
        $('#cloudRate').empty()
        $('#creatorRate').empty()
        $('#collabRate').empty()
        $('#capacitycollabRate').empty()
        $('#cloudRate').append('€336.8')
        $('#creatorRate').append('€74')
        $('#collabRate').append('€7.4')
        $('#capacitycollabRate').append('€50')
    });

    gbpButton.on('click', function() {
        gbpButton.addClass('is-active');
        eurButton.removeClass('is-active');
        $('#cloudRate').empty()
        $('#creatorRate').empty()
        $('#collabRate').empty()
        $('#capacitycollabRate').empty()
        $('#cloudRate').append('£306')
        $('#creatorRate').append('£66')
        $('#collabRate').append('£7')
        $('#capacitycollabRate').append('£45')
    });

    mobeurButton.on('click', function() {
        mobeurButton.addClass('is-active');
        mobgbpButton.removeClass('is-active');
        $('#mobcloudRate').empty()
        $('#mobcreatorRate').empty()
        $('#mobcollabRate').empty()
        $('#mobcapacitycollabRate').empty()
        $('#mobcloudRate').append('€336.8')
        $('#mobcreatorRate').append('€74')
        $('#mobcollabRate').append('€7.4')
        $('#mobcapacitycollabRate').append('€50')
    });

    mobgbpButton.on('click', function() {
        mobgbpButton.addClass('is-active');
        mobeurButton.removeClass('is-active');
        $('#mobcloudRate').empty()
        $('#mobcreatorRate').empty()
        $('#mobcollabRate').empty()
        $('#mobcapacitycollabRate').empty()
        $('#mobcloudRate').append('£306')
        $('#mobcreatorRate').append('£66')
        $('#mobcollabRate').append('£7')
        $('#mobcapacitycollabRate').append('£45')
    });
});

const noscript = document.createElement('noscript');
noscript.innerHTML = `<iframe src="https://www.googletagmanager.com/ns.html?id=GTM-57W656Z" height="0" width="0" style="display:none;visibility:hidden"></iframe>`;
document.body.insertBefore(noscript, document.body.firstChild);