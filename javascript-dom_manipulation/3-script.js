const button = document.getElementById("toggle_header");
const header = document.querySelector("header");

button.addEventListener("click", function() {
    header.classList.toggle("red");
    header.classList.toggle("green");
});