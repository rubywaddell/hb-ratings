"""Models for movie ratings app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    """Movie app user"""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement = True, primary_key = True)
    user_email = db.Column(db.String, unique = True, nullable = False)
    user_password = db.Column(db.String, unique = False, nullable = False)

    # ratings = a list of Rating objects (product of backref in Rating class)

    def __repr__(self):
        return f"<User user_id={self.user_id} email={self.user_email} password={self.user_password}>"


class Movie(db.Model):
    """Movies in app"""

    __tablename__ = "movies"

    movie_id = db.Column(db.Integer, autoincrement = True, primary_key = True)
    movie_title = db.Column(db.String)
    movie_overview = db.Column(db.Text)
    movie_release_date = db.Column(db.DateTime)
    movie_poster_path = db.Column(db.String)

    # ratings = a list of Rating objects (product of backref in Rating class)

    def __repr__(self):
        return f"<Movie movie_id={self.movie_id} movie_title={self.movie_title}>"


class Rating(db.Model):
    """Ratings of movies in app"""

    __tablename__ = "ratings"

    rating_id = db.Column(db.Integer, autoincrement = True, primary_key = True) 
    score = db.Column(db.Integer)
    movie_id = db.Column(db.Integer, db.ForeignKey("movies.movie_id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))

    movie = db.relationship("Movie", backref="ratings")
    user = db.relationship("User", backref="ratings")

    def __repr__(self):
        return f"<Movie Rating rating_id={self.rating_id} score={self.score}>"


def connect_to_db(flask_app, db_uri="postgresql:///ratings_lab", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")


if __name__ == "__main__":
    from server import app

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.

    connect_to_db(app)
