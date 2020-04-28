import contextlib
import glob
import json
import os
import sys

from sqlalchemy.orm import scoped_session

import get
import db

from flask import *

app = Flask(__name__)


@contextlib.contextmanager
def working_directory(path):
    prev_cwd = os.getcwd()
    os.chdir(path)
    yield
    os.chdir(prev_cwd)


# Get files
#with working_directory('./static/pixiv'):
#    posts = glob.glob('*.png') + glob.glob('*.jpg')
dbsession = scoped_session(db.Session())
if db.isempty():
    print("downloading")
    get.main()
    with working_directory('./static/pixiv'):
        ids = glob.glob('*.json')
    print(str(ids))
    ids = map(lambda x : x.split('.')[0], ids)
    for id in ids:
        db.addpixiv(id)
print(db.session.query(db.Posts).all())
#posts = map(addition, numbers)


@app.route('/')
def hello_world():
    return render_template("hello.html", posts=map(lambda x : x.file_name,db.session.query(db.Posts).all()))

@app.route('/download_pixiv', methods=['GET'])
def presentpixiv():
    return """<!DOCTYPE html>
<html>
<body>
<form action="/download_pixiv" method="post" >
  <label for="fname">pixiv id:</label><br>
  <input type="text" id="pixiv_id" name="pixiv_id" value="20"><br>
  <input type="submit" value="Submit">
</form> 
<p>If you click the "Submit" button, the form-data will be sent to a page called "/download_pixiv".</p>
</body>
</html>"""

@app.route('/download_pixiv', methods=['POST'])
def downloadpixiv():
    id = request.form.get('pixiv_id')
    get.download(id);
    db.addpixiv(id)
    return "done"



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
