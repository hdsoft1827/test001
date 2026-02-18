from flask import Flask, render_template, request, redirect, url_for, session
import os

app = Flask(__name__)
app.secret_key = "secret"

movies = []
movie_id_counter = 1


# ✅ 1. 로그인 페이지
@app.route("/")
def login_page():
    return render_template("login.html")


# ✅ 2. 로그인 처리
@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    if username == "admin" and password == "admin":
        session["user"] = username
        return redirect(url_for("main"))

    return "Login Failed"


# ✅ 3. 로그아웃
@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login_page"))


# ✅ 4. 메인 페이지
@app.route("/main")
def main():
    if "user" not in session:
        return redirect(url_for("login_page"))

    return render_template("index.html", movies=movies)


# ✅ 5. 영화 추가
@app.route("/add", methods=["POST"])
def add_movie():
    global movie_id_counter

    if "user" not in session:
        return redirect(url_for("login_page"))

    title = request.form.get("title")
    description = request.form.get("description")
    rating = request.form.get("rating")

    movie = {
        "id": movie_id_counter,
        "title": title,
        "description": description,
        "rating": rating
    }

    movies.append(movie)
    movie_id_counter += 1

    return redirect(url_for("main"))


# ✅ 6. 상세 페이지
@app.route("/detail/<int:movie_id>")
def detail(movie_id):
    if "user" not in session:
        return redirect(url_for("login_page"))

    movie = next((m for m in movies if m["id"] == movie_id), None)
    if movie is None:
        return "Not Found", 404

    return render_template("detail.html", movie=movie)


# ✅ Docker 실행
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
