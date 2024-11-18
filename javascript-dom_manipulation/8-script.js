fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
    .then(function(response) {
        return response.json(); // Once website response, the code converts to readable javascript format(JSON)
    })
    .then(function(data) {
        document.querySelector("#hello").textContent = data.hello; // the hello french language will be stored in data.hello
    })
    .catch(function(error) {
        console.log(error); // if anything goes wrong during the process it will display a message on a console
    });