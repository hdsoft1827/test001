from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# 간단한 메모리 저장용 리스트 (과제 수준)
movies = []
movie_id_counter = 1


@app.route("/")
def index():
    return render_template("index.html", movies=movies)


@app.route("/add", methods=["POST"])
def add_movie():
    global movie_id_counter

    title = request.form.get("title")
    description = request.form.get("description")
    rating = request.form.get("rating")

    if not title:
        return redirect(url_for("index"))

    movie = {
        "id": movie_id_counter,
        "title": title,
        "description": description,
        "rating": rating
    }

    movies.append(movie)
    movie_id_counter += 1

    return redirect(url_for("index"))


@app.route("/detail/<int:movie_id>")
def detail(movie_id):
    movie = next((m for m in movies if m["id"] == movie_id), None)
    if movie is None:
        return "Movie not found", 404
    return render_template("detail.html", movie=movie)


@app.route("/delete/<int:movie_id>")
def delete_movie(movie_id):
    global movies
    movies = [m for m in movies if m["id"] != movie_id]
    return redirect(url_for("index"))


# 🔥 Docker & CI 안정 실행용
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
