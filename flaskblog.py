# save this as app.py
from flask import Flask, escape, request, render_template

app = Flask(__name__)

posts = [
    {
        "author": "Michael Love",
        "title": "Blog Post 1",
        "content": "First post content",
        "date_posted": "July 2, 2022",
    },
    {
        "author": "Jane Doe",
        "title": "Blog Post 2",
        "content": "Second post content",
        "date_posted": "July 1, 2022",
    },
]


@app.route("/")
def hello():
    return render_template("home.html", posts=posts)


@app.route("/about")
def about():
    return render_template("about.html", title="About")


if __name__ == "__main__":
    app.run(debug=True)
