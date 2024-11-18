fetch('https://swapi-api.hbtn.io/api/films/?format=json')
    .then(function(response) {
        return response.json(); // converts code in JSON friendly format 
    })
    .then(function(data) { // function is passing parameter data that "then" handles what to do with the data
        const movieList = document.querySelector("#list_movies"); // searching a HTML element with the ID "list_movies"
        data.results.forEach(function(movie) {
            const li = document.createElement('li'); // creates new list of item (movie)
            li.textContent = movie.title; // list items (movies title) in dot points
            movieList.appendChild(li); // adds list of items of movies
        });
    })
    .catch(function(error) {
        console.log(error); // just in case internet crashes, console will print an error message
    });