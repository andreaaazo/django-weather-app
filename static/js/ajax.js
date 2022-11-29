$.ajax({
    type: "GET",
    beforeSend: function () {
        $(".preloader").fadeIn(500)
    },

    complete: function () {
        $(".preloader").fadeOut(800)
    } 
})