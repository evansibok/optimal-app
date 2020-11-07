import os
from os.path import join, dirname
from dotenv import load_dotenv

load_dotenv()

class Config(object):
    SECRET_KEY = os.getenv('SECRET_KEY', 'you-cant-tell-me-nothing')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', os.path.join(dirname(__file__), 'site.db')),
    SQLALCHEMY_TRACK_MODIFICATIONS=False

# FLASK DOC - Can't use as not importing app here
# os.path.join(app.instance_path, "optimal.sqlite")

# ANOTHER BLOG (ENV VARIABLE HELPFUL)
# from os.path import join, dirname
# os.path.join(dirname(__file__), '.env')

# MIGUEL GRINBERG BLOG
# basedir = os.path.abspath(os.path.dirname(__file__))
# 'sqlite:///' + os.path.join(basedir, 'app.db')

# COREY YOUTUBE VIDEO
# 'sqlite:///site.db'
