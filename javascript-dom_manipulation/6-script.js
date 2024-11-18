fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
    .then(function(response) {
        return response.json(); // converts code into JSON, javascript friendly format
    })
    .then(function(data) { // function passes "data" parameter
        document.querySelector("#character").textContent = data.name; // search for HTML tag with ID character and then it will be stored "data.name"
    })
    .catch(function(error) {
        console.log(error);
    });