"""Server for movie ratings app."""

from flask import Flask, render_template, request, flash, session, redirect

from model import connect_to_db

import crud

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "%$E^R&T*()(UYTF"
app.jinja_env.undefined = StrictUndefined
# Replace this with routes and view functions!


if __name__ == "__main__":
    # DebugToolbarExtension(app)
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)
