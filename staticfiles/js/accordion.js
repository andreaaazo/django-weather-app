var acc = document.getElementsByClassName("head");
var i;


for (i = 0; i < acc.length; i++) {

    acc[i].addEventListener("mouseover", function() {
        var image = this.children[0]

        anime({
            duration: 750,
            targets: image,
            rotateZ: 90,
        }).play()

    })


    acc[i].addEventListener("mouseout", function() {
        var image = this.children[0]

        anime({
            targets: image,
            duration: 750,
            rotateZ: 0,
        }).play()


    })

    acc[i].addEventListener("click", function() {

        // Disable every active accordion
        for (i = 0; i < acc.length; i++) {
            var acc_panels = acc[i].nextElementSibling;
            var all_span_2 = acc[i].children[0].children[1]

            if (acc[i].classList.contains("active")) {

                if (!(acc[i] == this)) {

                    // animate all closings
                    anime({
                        duration: 1000,
                        targets: all_span_2,
                        left: [{ value: 30 + "%" }],
                        right: [{ value: 30 + "%" }],
                    }).play()

                    acc_panels.style.maxHeight = null;
                    acc[i].classList.remove("active")
                }
            }
        }


        // Toggle current panel 
        var panel = this.nextElementSibling;
        var span_2 = this.children[0].children[1]

        this.classList.toggle("active");

        if (panel.style.maxHeight) {

            // Close panel
            anime({
                duration: 750,
                targets: span_2,
                left: [{ value: 30 + "%" }],
                right: [{ value: 30 + "%" }],
            }).play()

            panel.style.maxHeight = null;
        } else {

            // Open panel
            anime({
                duration: 750,
                targets: span_2,
                left: [{ value: 50 + "%" }],
                right: [{ value: 50 + "%" }],
            }).play()

            panel.style.maxHeight = panel.scrollHeight + "px";
        }
    });
}