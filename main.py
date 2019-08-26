from flask import Flask
from flask import render_template

app = Flask(__name__)

posts = ["https://raikou4.donmai.us/preview/b6/1d/b61d520fc98495185487ab3af37407f9.jpg","https://raikou4.donmai.us/preview/ff/70/ff7032ecc5aa8bbe529a335842ac7463.jpg","https://raikou4.donmai.us/preview/ed/2f/ed2fd218b14ba9f6fc9b04f358d3b9c8.jpg","https://raikou4.donmai.us/preview/11/b2/11b2741bb1257c41a71ed0802f4b79bf.jpg"]

@app.route('/')
def hello_world():
    return render_template("hello.html",posts=posts)

if __name__ == "__main__":

    app.run(host='0.0.0.0',port=8080)