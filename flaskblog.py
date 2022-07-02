# save this as app.py
from flask import Flask, escape, request, render_template

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template("home.html")


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)
