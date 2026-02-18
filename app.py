from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/detail')
def detail():
    movie_id = request.args.get('id')
    return render_template('detail.html', movie_id=movie_id)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
