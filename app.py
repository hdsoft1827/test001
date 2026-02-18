from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "supersecretkey"

# { movie_id: [ {text: "", rating: 5}, ... ] }
comments = {}


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username == "admin" and password == "1234":
            session['user'] = username
            return redirect(url_for('home'))
        else:
            return "로그인 실패 😢"

    return render_template('login.html')


@app.route('/home')
def home():
    if 'user' not in session:
        return redirect(url_for('login'))

    return render_template('index.html')


@app.route('/detail', methods=['GET', 'POST'])
def detail():
    if 'user' not in session:
        return redirect(url_for('login'))

    movie_id = request.args.get('id')

    if request.method == 'POST':
        comment_text = request.form.get('comment')
        rating = request.form.get('rating')

        if comment_text and rating:
            comments.setdefault(movie_id, []).append({
                "text": comment_text,
                "rating": int(rating)
            })

        return redirect(url_for('detail', id=movie_id))

    movie_comments = comments.get(movie_id, [])

    # 평균 평점 계산
    if movie_comments:
        avg_rating = round(
            sum(c["rating"] for c in movie_comments) / len(movie_comments),
            1
        )
    else:
        avg_rating = 0

    return render_template(
        'detail.html',
        movie_id=movie_id,
        comments=movie_comments,
        avg_rating=avg_rating
    )


@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
