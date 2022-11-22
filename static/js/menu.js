const menu = document.getElementsByClassName("menu")[0]
const menu_button = document.getElementsByClassName("menu-button")[0]
const menu_container = document.getElementsByClassName("container-menu")[0]
const navbar = document.getElementsByClassName("navbar")[0]
const nav = document.getElementsByTagName("nav")[0]

menu_button.addEventListener("click", function () {

    this.classList.toggle("active");

    if (this.classList.contains("active")) {
        menu.style.display = "flex"
        menu_button.style.margin = "50px 50px 0 0"
        menu_button.style.alignSelf = "flex-start"
        navbar.style.position = "fixed"
        navbar.style.height = "100%"
        menu_container.style.padding = "0"
        menu_container.style.marginLeft = "0"
        menu_container.style.marginRight = "0"
        nav.style.padding = "0 0"


    } else {
        menu.style.display = ""
        menu_button.style.margin = ""
        menu_button.style.alignSelf = ""
        navbar.style.position = ""
        navbar.style.height = ""
        menu_container.style.padding = ""
        menu_container.style.marginLeft = ""
        menu_container.style.marginRight = ""
        nav.style.padding = ""
    }
});

window.addEventListener("resize", function () {
    menu_button.classList.remove("active")
    menu.style.display = ""
    menu_button.style.margin = ""
    menu_button.style.alignSelf = ""
    navbar.style.position = ""
    navbar.style.height = ""
    menu_container.style.padding = ""
    menu_container.style.marginLeft = ""
    menu_container.style.marginRight = ""
    nav.style.padding = ""
})