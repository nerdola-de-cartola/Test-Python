from flask import Flask, render_template, request

app = Flask(__name__)

app.config.from_pyfile('settings.py')

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search/")
def search():
    args = request.args

    if(args):
        title = args["title"]
        print(title)
        print(app.config["OMDB_API_KEY"])
    
    return render_template("search.html")