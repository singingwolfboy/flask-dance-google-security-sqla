from flask import Flask, redirect, url_for, flash, render_template
from flask_security import login_required, logout_user
from .config import Config
from .models import db, security, user_datastore
from .oauth import blueprint
from .cli import create_db


app = Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(blueprint, url_prefix="/login")
app.cli.add_command(create_db)
db.init_app(app)
security.init_app(app, user_datastore)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You have logged out")
    return redirect(url_for("index"))


@app.route("/")
def index():
    return render_template("home.html")
