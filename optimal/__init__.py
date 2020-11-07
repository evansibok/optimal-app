"""
The beginning of the Optimal App
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


from optimal import routes, models

# import os

# from flask import Flask, render_template, url_for, flash, redirect, request
# from flask_sqlalchemy import SQLAlchemy
# from forms import RegForm
# from forms import LoginForm
# db = SQLAlchemy()


# def create_app(test_config=None):
#     app = Flask(__name__, instance_relative_config=True)
#     app.config.from_mapping(
#         SECRET_KEY="dev",
#         SQLALCHEMY_DATABASE_URI=os.path.join(
#             app.instance_path, "optimal.sqlite"),
#         SQLALCHEMY_TRACK_MODIFICATIONS=False
#     )
#     db.init_app(app)

#     if test_config is None:
#         # load the instance config, if it exists, when not testing
#         app.config.from_pyfile('config.py', silent=True)
#     else:
#         # load the test config if passed in
#         app.config.from_mapping(test_config)

#     # ensure the instance folder exists
#     try:
#         os.makedirs(app.instance_path)
#     except OSError:
#         pass



#     return app
