import os

from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from forms import RegForm
from forms import LoginForm
db = SQLAlchemy()

blogPosts = [
    {
        'id': 1,
        'author': 'evansibok',
        'title': 'First Blog Post',
        'content': 'This is the first blog post!',
        'date_posted': 'Nov 6, 2020',
    },
    {
        'id': 2,
        'author': 'jonwen',
        'title': 'Second Blog Post',
        'content': 'This is the second blog post!',
        'date_posted': 'Nov 6, 2020',
    },
]


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="dev",
        SQLALCHEMY_DATABASE_URI=os.path.join(
            app.instance_path, "optimal.sqlite")
    )
    db.init_app(app)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/')
    @app.route('/home')
    def home():
        return render_template("home.html")

    @app.route('/register')
    def register():
        form = RegForm()
        return render_template('register.html', title="Register", form=form)

    @app.route('/login')
    def login():
        form = LoginForm()
        return render_template('login.html', title="Login", form=form)

    @app.route('/posts')
    def posts():
        return render_template("posts.html", title="Posts", posts=blogPosts)

    return app
