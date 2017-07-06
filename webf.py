from flask import Flask, redirect, request
from downloader import audio, video

app = Flask(__name__)


@app.route('/audio', methods = ['POST'])
def dl_audio():
    return redirect(audio(request.form["audio"]))

@app.route('/video', methods = ['POST'])
def dl_video():
    url = video(request.form["video"])
    return redirect(url)

@app.route('/')
def index():
    return open('index.html').read()


if __name__ == '__main__':
    app.run('127.0.0.1', port=8080, debug=True)
