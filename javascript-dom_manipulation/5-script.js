document.addEventListener('DOMContentLoaded', function () { // wait till the webpage is fully loaded "DOMContendLoaded"
    const header = document.querySelector("header");
    const updateHeader = document.querySelector("#update_header") // search for two HTML elements - with ID "update_header" and <header>
  
      updateHeader.addEventListener('click', function () {
      header.textContent = "New Header!!!"; // once user click on update the header heading it will change  to New Header !
    });
  });