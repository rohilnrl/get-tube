# -*- coding: utf-8 -*-
from hashlib import new
from subprocess import check_output, CalledProcessError


def gethash(url):
    try:
        return new(url).hexdigest()
    except Exception:
        print('error: failed to generate sha hash')


def audio(url, audioquality='0', audioformat='mp3'):
    outurl = '/'

    getargs = ['youtube-dl', '-x', '--id', '--get-url',
               '--audio-quality', audioquality,
               '--audio-format', audioformat]

    getargs.append(url)

    try:
        outurl = check_output(getargs).decode('utf-8')
    except CalledProcessError:
        print('error: failed to get audio')

    return outurl

def video(url, videoformat='mp4'):
    outurl = '/'

    getargs = ['youtube-dl', '-g', '--format', videoformat]

    getargs.append(url)

    try:
        outurl = check_output(getargs).decode('utf-8')
    except CalledProcessError:
        print('error: failed to get video')

    return outurl
