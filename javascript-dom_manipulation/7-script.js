fetch('https://swapi-api.hbtn.io/api/films/?format=json')
    .then(function(response) {
        return response.json();
    })
    .then(function(data) {
        const movieList = document.querySelector("#list_movies");
        data.results.forEach(function(movie) {
            const li = document.createElement('li');
            li.textContent = movie.title;
            movieList.appendChild(li);
        });
    })
    .catch(function(error) {
        console.log(error);
    });