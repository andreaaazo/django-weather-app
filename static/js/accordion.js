var acc = document.getElementsByClassName("head");
var i;


for (i = 0; i < acc.length; i++) {
    acc[i].addEventListener("click", function () {
        for (i = 0; i < acc.length; i++) {
            if (acc[i].classList.contains("active")) {
                var acc_panel = acc[i].nextElementSibling;
                
                if (!(acc[i] == this)) {
                    acc_panel.style.maxHeight = null;
                    acc[i].classList.remove("active")
                }
            }
        }
        
        var panel = this.nextElementSibling;
        this.classList.toggle("active");
        if (panel.style.maxHeight) {
        panel.style.maxHeight = null;
        } else {
            panel.style.maxHeight = panel.scrollHeight + "px";
        }
  });
}