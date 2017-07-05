from flask import redirect

import hashlib
import subprocess


def gethash(url):
    try:
        return hashlib.new(url).hexdigest()
    except Exception:
        print("error: failed to generate sha hash")


def audio(url, audioquality="0", audioformat="mp3", *args):
    outurl = '/'

    getargs = ["youtube-dl", "-x", "--id", "--get-url",
               "--audio-quality", audioquality,
               "--audio-format", audioformat]

    getargs.append(args)
    getargs.append(url)

    try:
        outurl = subprocess.check_output(getargs)
    except CalledProcessError:
        print("error: failed to get audio")

    redirect(outurl)
