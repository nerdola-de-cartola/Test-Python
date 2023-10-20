from flask import Flask, render_template, request
import requests
import ast
import sqlite3

app = Flask(__name__)

app.config.from_pyfile('settings.py')

def dict_factory(cursor, row):
    fields = [column[0] for column in cursor.description]
    return {key: value for key, value in zip(fields, row)}

def db_connection():
    connection = sqlite3.connect('database/database.db')
    connection.row_factory = dict_factory
    return connection

def get_favorites():
    connection = db_connection()

    favorites = connection.execute(
        "SELECT * FROM favorites"
    ).fetchall()

    connection.close()
    print(favorites)
    return favorites

def save_favorite(film):
    connection = db_connection()

    favorites = connection.execute(
        "INSERT INTO favorites (title, release_date, director, writer, actors, poster) VALUES (?, ?, ?, ?, ?, ?)",
        (film["Title"], film["Released"], film["Director"], film["Writer"], film["Actors"], film["Poster"])
    )

    connection.commit()
    connection.close()
    return favorites

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/favorites", methods=["GET", "POST"])
def favorites():
    if request.method == 'POST':
        args = request.args

        if(args):
            film = ast.literal_eval(args["values"])
            save_favorite(film)

    return render_template("favorites.html", favorites=get_favorites())

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