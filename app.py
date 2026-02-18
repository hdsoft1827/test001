from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "supersecretkey"  # 세션 사용을 위한 키

# 영화별 댓글 저장 (DB 없이 메모리 저장)
comments = {}  # { movie_id: [댓글들] }


# -----------------------
# 로그인 페이지
# -----------------------
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # 간단한 테스트용 계정
        if username == "admin" and password == "1234":
            session['user'] = username
            return redirect(url_for('home'))
        else:
            return "로그인 실패 😢"

    return render_template('login.html')


# -----------------------
# 메인 페이지
# -----------------------
@app.route('/home')
def home():
    if 'user' not in session:
        return redirect(url_for('login'))

    return render_template('index.html')


# -----------------------
# 상세 페이지 + 댓글
# -----------------------
@app.route('/detail', methods=['GET', 'POST'])
def detail():
    if 'user' not in session:
        return redirect(url_for('login'))

    movie_id = request.args.get('id')

    if request.method == 'POST':
        comment = request.form.get('comment')

        if comment:
            comments.setdefault(movie_id, []).append(comment)

        # 🔥 여기 핵심: 저장 후 리다이렉트
        return redirect(url_for('detail', id=movie_id))

    movie_comments = comments.get(movie_id, [])

    return render_template(
        'detail.html',
        movie_id=movie_id,
        comments=movie_comments
    )



# -----------------------
# 로그아웃
# -----------------------
@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)