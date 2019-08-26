import contextlib
import glob
import json
import os
import sys

from flask import Flask, render_template

app = Flask(__name__)


@contextlib.contextmanager
def working_directory(path):
    prev_cwd = os.getcwd()
    os.chdir(path)
    yield
    os.chdir(prev_cwd)


# Get files
with working_directory('./static/pixiv'):
    posts = glob.glob('*.png') + glob.glob('*.jpg')


@app.route('/')
def hello_world():
    return render_template("hello.html", posts=posts)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
