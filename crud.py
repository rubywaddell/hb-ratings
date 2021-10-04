"""CRUD operations"""

from model import db, User, Movie, Rating, connect_to_db


def create_user(email, password):
    """Create and return a new user."""

    user = User(user_email=email, user_password=password)

    db.session.add(user)
    db.session.commit()

    return user

def show_users():
    """Return a list of users"""

    return User.query.all()

def get_user_by_id(user_id):
    """Return the first user with a given id"""

    user = User.query.filter(User.user_id == user_id).first()
    return user

def get_user_by_email(user_email):
    """Determine if a user profile exists already"""

    user = User.query.filter(User.user_email == user_email).first()
    return user

def create_movie(title, overview, release_date, poster_path):
    """Create and return a new movie"""

    movie = Movie(movie_title=title, movie_overview=overview, movie_release_date=release_date, movie_poster_path=poster_path)

    db.session.add(movie)
    db.session.commit()

    return movie

def show_movie():
    """Return a list of all movie objects"""

    return Movie.query.all()

def get_movie_by_id(movie_id):
    """Return the first movie that has a given id"""

    movie = Movie.query.filter(Movie.movie_id == movie_id).first()
    return movie

def create_rating(user, movie, score):
    """Create and return a new rating."""

    rating = Rating(user=user, movie=movie, score=score)

    db.session.add(rating)
    db.session.commit()

    return rating


if __name__ == '__main__':
    from server import app
    connect_to_db(app)