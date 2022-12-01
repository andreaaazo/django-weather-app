$.ajax({
    type: "GET",
    beforeSend: function () {
        $(".preloader").show()
        const animation = anime({
            targets: '.spinner path',
            strokeDashoffset: [anime.setDashoffset, 0],
            easing: 'cubicBezier(.5, .2, .3, 1, 1)',
            duration: 500,
            delay: function(el, i) { return i * 50 },
            direction: 'alternate',
            loop: true
        });

        animation.play()
    },

    complete: function () {
        setTimeout(function () {
            $(".preloader").fadeOut(500)
        }, 500)
    }
})