from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "supersecretkey"

# 댓글 + 별점 저장
# { movie_id: [ { "text": "...", "rating": 4 }, ... ] }
comments = {}


# -----------------------
# 로그인
# -----------------------
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


# -----------------------
# 메인
# -----------------------
@app.route('/home')
def home():
    if 'user' not in session:
        return redirect(url_for('login'))

    return render_template('index.html')


# -----------------------
# 상세 + 댓글 + 별점
# -----------------------
@app.route('/detail', methods=['GET', 'POST'])
def detail():
    if 'user' not in session:
        return redirect(url_for('login'))

    movie_id = request.args.get('id')

    if request.method == 'POST':
        comment = request.form.get('comment')
        rating = request.form.get('rating')

        if comment and rating:
            comments.setdefault(movie_id, []).append({
                "text": comment,
                "rating": int(rating)
            })

        return redirect(url_for('detail', id=movie_id))

    mov
