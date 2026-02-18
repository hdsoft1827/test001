const movieList = document.getElementById("movie-list");

movies.forEach(movie => {
  movieList.innerHTML += `
    <div class="movie-card">
      <img src="${movie.poster}" alt="${movie.title}">
      <div class="movie-info">
        <h3>${movie.title}</h3>
        <p>${movie.year}</p>
        <button onclick="location.href='/detail?id=${movie.id}'">
          상세보기
        </button>
      </div>
    </div>
  `;
});
