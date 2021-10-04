"""Server for movie ratings app."""

from flask import Flask, render_template, request, flash, session, redirect

from model import connect_to_db

import crud

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "%$E^R&T*()(UYTF"
app.jinja_env.undefined = StrictUndefined
# Replace this with routes and view functions!

@app.route("/")
def show_homepage():
    """View homepage"""

    return render_template("homepage.html")

@app.route("/movies")
def show_movies():
    """View a list of all movies"""

    movies = crud.show_movie()
    return render_template("all_movies.html", movies=movies)

@app.route("/movies/<movie_id>")
def show_movie_detail(movie_id):
    """View a page with details for a particular movie"""

    movie = crud.get_movie_by_id(movie_id)
    
    return render_template("movie_details.html", movie=movie)

@app.route("/users")
def show_users():
    """View a page with a list of all app users"""

    users = crud.show_users()
    return render_template("all_users.html", users=users)

@app.route("/users/<user_id>")
def show_user_profile(user_id):
    """Show an individual user's profile"""

    user = crud.get_user_by_id(user_id)
    return render_template("user_profile.html", user=user)

if __name__ == "__main__":
    # DebugToolbarExtension(app)
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)
