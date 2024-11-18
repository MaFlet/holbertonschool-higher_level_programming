document.addEventListener('DOMContentLoaded', function() {
    const myList = document.querySelector(".my_list");
    const addItem = document.querySelector("li");
    addItem.textContent ="Item";
    myList.appendChild(addItem);
});