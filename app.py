from flask import Flask, render_template, request
import requests
import settings
import ast
import sqlite3

app = Flask(__name__)

app.config.from_pyfile('settings.py')

def db_connection():
    connection = sqlite3.connect('database/database.db')
    connection.row_factory = sqlite3.Row
    return connection

@app.route("/")
def index():
    connection = db_connection()
    posts = connection.execute('SELECT * FROM posts').fetchall()
    print(posts[0]["title"])
    connection.close()
    return render_template("index.html")

@app.route("/favorites", methods=["GET", "POST"])
def favorites():
    if request.method == 'POST':
        args = request.args

        if(args):
            film = args["values"]
            settings.favorites.append(ast.literal_eval(film))

    return render_template("favorites.html", favorites=settings.favorites)

@app.route("/search/")
def search():
    args = request.args
    data = None
    error = False

    if(args):
        title = args["title"]
        api_key = app.config["OMDB_API_KEY"]
        url = f'http://www.omdbapi.com/'
        payload = {
            "apikey": api_key,
            "t": title
        }

        response = requests.get(url, params=payload)

        data = response.json()
        error = response.status_code != 200 or data["Response"] == "False"
    
    return render_template("search.html", film=data, error=error)