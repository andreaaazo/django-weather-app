var swiper = new Swiper(".card-container", {
    autoplay: {
        delay: 3500,
    },
    spaceBetween: 24,
    loop: false,
    grabCursor: true,
    fade: true,
    pagination: {
        el: ".swiper-pagination",
        clickable: true,
        dynamicBullets: true
    },

    breakpoints: {
        0: {
            slidesPerView: 1,
        },
        768: {
            slidesPerView: 2,
        },
        1200: {
            slidesPerView: 4,
        }
    }
})