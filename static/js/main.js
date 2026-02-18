const movieList = document.getElementById("movie-list");

movies.forEach(movie => {
  const card = document.createElement("div");
  card.className = "movie-card";

  card.innerHTML = `
    <img src="${movie.poster}" alt="${movie.title}">
    <h3>${movie.title}</h3>
    <p>${movie.year}</p>
    <button data-id="${movie.id}">상세보기</button>
  `;

  card.querySelector("button").addEventListener("click", () => {
    window.location.href = `detail.html?id=${movie.id}`;
  });

  movieList.appendChild(card);
});
