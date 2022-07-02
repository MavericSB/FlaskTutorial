# save this as app.py
from flask import Flask, escape, request

app = Flask(__name__)


@app.route("/")
def hello():
    return f"<h1>Home Page</h1>"


@app.route("/about")
def about():
    return f"<h1>About Page</h1>"


if __name__ == "__main__":
    app.run(debug=True)
