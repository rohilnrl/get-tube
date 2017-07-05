import os, subprocess, hashlib

def gethash(url):
    try:
        return hashlib.new(url).hexdigest()
    except Exception:
        print("error: failed to  generate sha hash")

def audio(url, audioquality="0", audioformat="mp3", *args):
    getargs = ["youtube-dl", "-x", "-g", "--audio-quality", audioquality, "--audio-format", audioformat]
    getargs.append(args)
    getargs.append(url)

    if(subprocess.call(getargs) == 0):
        pass
    else:
        raise Exception("error: failed to get audio")    
