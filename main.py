from flask import Flask
from flask import render_template

app = Flask(__name__)

posts = "https://raikou4.donmai.us/preview/b6/1d/b61d520fc98495185487ab3af37407f9.jpg"

@app.route('/')
def hello_world():
    return render_template("hello.html",posts=posts)

if __name__ == "__main__":

    app.run(host='0.0.0.0',port=8080)
