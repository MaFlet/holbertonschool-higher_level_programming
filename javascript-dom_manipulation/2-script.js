const header = document.querySelector("header");

header.addEventListener("click", function() {
    updateColor();
});

function updateColor() {
    header.style.color = "#FF0000";
    button.textContent = 'red_header'
}