const params = new URLSearchParams(window.location.search);
const id = params.get("id");

const movie = movies.find(m => m.id == id);

const container = document.getElementById("movie-detail");

if (movie) {
  container.innerHTML = `
  <div class="detail-layout">
    <img src="${movie.poster}" alt="${movie.title}">
    <div class="detail-text">
      <h2>${movie.title} (${movie.year})</h2>
      <p>${movie.description}</p>
    </div>
  </div>
`;
} else {
  container.innerHTML = "<p>영화를 찾을 수 없습니다.</p>";
}