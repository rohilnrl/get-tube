# -*- coding: utf-8 -*-


import hashlib
import subprocess


def gethash(url):
    """This function returns a 40 character long SHA hash.

    Args:
        url (string): The URL to be hashed.

    Returns:
        string: The hash value.

    """

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

    return outurl
