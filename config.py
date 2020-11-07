"""
Optimal App Config File
"""
import os
from os.path import join, dirname
from dotenv import load_dotenv

load_dotenv()

class Config():
    """
    Initializes the Config for Optimal App
    """
    
    SECRET_KEY = os.getenv('SECRET_KEY', 'you-cant-tell-me-nothing')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///' + join(dirname(__file__), 'site.db'))
    SQLALCHEMY_TRACK_MODIFICATIONS=False


# ANOTHER BLOG (ENV VARIABLE HELPFUL)
# from os.path import join, dirname
# os.path.join(dirname(__file__), '.env')

# MIGUEL GRINBERG BLOG
# basedir = os.path.abspath(os.path.dirname(__file__))
# 'sqlite:///' + os.path.join(basedir, 'app.db')


