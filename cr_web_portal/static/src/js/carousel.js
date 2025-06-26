//if (!$(".testimonial-carousel > .owl-stage-outer").length) {
//    $(".testimonial-carousel").owlCarousel({
//    autoplay: true,
//    smartSpeed: 1000,
//    center: true,
//    dots: true,
//    loop: true,
//    nav: true,
//    navText:["<span class='icon'><svg xmlns='http://www.w3.org/2000/svg' width='30' height='30' fill='none' stroke='currentColor' stroke-width='2' stroke-linecap='round' stroke-linejoin='round' viewBox='0 0 24 24'> <circle cx='12' cy='12' r='' stroke-opacity='0.5' /> <polyline points='14 8 10 12 14 16' /> </svg> </span>", "<span class='icon'><svg xmlns='http://www.w3.org/2000/svg' width='30' height='30' fill='none' stroke='currentColor' stroke-width='2' stroke-linecap='round' stroke-linejoin='round' viewBox='0 0 24 24'> <circle cx='12' cy='12' r='' stroke-opacity='0.5' /> <polyline points='10 8 14 12 10 16' /> </svg> </span>"],
//    margin: 20,
//    responsive: {
//        0:{
//            items:1
//        },
//        768:{
//            items:2
//        },
//        992:{
//            items:3
//        },
//        1024:{
//            items:2
//        }
//    }
//});
//}

$(".italtronics-products-carousel").each(function() {
    if (!$(this).find(".owl-stage-outer").length) {
        $(this).owlCarousel({
            autoplay: true,
            smartSpeed: 1500,
            dots: false,
            loop: true,
            nav: true,
            margin: 24,
            navText: [
                "<span class='icon'><svg xmlns='http://www.w3.org/2000/svg' width='30' height='30' fill='none' stroke='currentColor' stroke-width='2' stroke-linecap='round' stroke-linejoin='round' viewBox='0 0 24 24'> <circle cx='12' cy='12' r='' stroke-opacity='0.5' /> <polyline points='14 8 10 12 14 16' /> </svg> </span>",
                "<span class='icon'><svg xmlns='http://www.w3.org/2000/svg' width='30' height='30' fill='none' stroke='currentColor' stroke-width='2' stroke-linecap='round' stroke-linejoin='round' viewBox='0 0 24 24'> <circle cx='12' cy='12' r='' stroke-opacity='0.5' /> <polyline points='10 8 14 12 10 16' /> </svg> </span>"
            ],
            responsive: {
                0: {
                    items: 2
                },
                576: {
                    items: 2
                },
                768: {
                    items: 4
                },
                992: {
                    items: 4
                },
                1024: {
                    items: 4
                }
            }
        });
    }
});

//if (!$(".product-cards-carousel > .owl-stage-outer").length) {
//    $(".product-cards-carousel").owlCarousel({
//    autoplay: true,
//    smartSpeed: 1500,
//    dots: false,
//    loop: true,
//    nav:true,
//    margin: 24,
//    navText:["<span class='icon'><svg xmlns='http://www.w3.org/2000/svg' width='30' height='30' fill='none' stroke='currentColor' stroke-width='2' stroke-linecap='round' stroke-linejoin='round' viewBox='0 0 24 24'> <circle cx='12' cy='12' r='' stroke-opacity='0.5' /> <polyline points='14 8 10 12 14 16' /> </svg> </span>", "<span class='icon'><svg xmlns='http://www.w3.org/2000/svg' width='30' height='30' fill='none' stroke='currentColor' stroke-width='2' stroke-linecap='round' stroke-linejoin='round' viewBox='0 0 24 24'> <circle cx='12' cy='12' r='' stroke-opacity='0.5' /> <polyline points='10 8 14 12 10 16' /> </svg> </span>"],
//    responsive: {
//        0:{
//            items:1
//        },
//        576:{
//            items:1
//        },
//        768:{
//            items:3
//        },
//        992:{
//            items:3
//        },
//        1024:{
//            items:3
//        }
//    }
//});
//}

document.querySelectorAll('.toc-link').forEach(link => {
    link.addEventListener('click', function() {
        document.querySelectorAll('.toc-link').forEach(item => item.classList.remove('active'));
        this.classList.add('active');
    });
});


document.querySelectorAll('.accordion-button').forEach(button => {
    button.addEventListener('click', function () {
        const icon = this.nextElementSibling; // Select the next sibling (SVG element)

        // Toggle the rotation class
        if (icon.classList.contains('icon-rotate')) {
            icon.classList.remove('icon-rotate');
        } else {
            icon.classList.add('icon-rotate');
        }
    });
});