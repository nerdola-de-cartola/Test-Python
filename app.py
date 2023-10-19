from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search/")
def search():
    args = request.args

    if(args):
        title = args["title"]
        print(title)
    
    return render_template("search.html")