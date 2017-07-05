# -*- coding: utf-8 -*-


import hashlib
import subprocess


def gethash(url):
    try:
        return hashlib.new(url).hexdigest()
    except Exception:
        print('error: failed to generate sha hash')


def audio(url, audioquality='0', audioformat='mp3'):
    outurl = '/'

    getargs = ['youtube-dl', '-x', '--id', '--get-url',
               '--audio-quality', audioquality,
               '--audio-format', audioformat]

    getargs.append(url)

    try:
        outurl = subprocess.check_output(getargs)
    except subprocess.CalledProcessError:
        print('error: failed to get audio')

    outurl = outurl.decode('utf-8')
    print(outurl)

    return outurl
