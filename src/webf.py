from flask import Flask, redirect

app = Flask(__name__)


@app.route('/')
def index():
    return open('index.html').read()

@app.route('/audio')
def dl_audio():
    pass

if __name__ == '__main__':
    app.run('127.0.0.1', port=8080, debug=True)
