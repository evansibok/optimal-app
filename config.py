import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

class Config(object):
    SECRET_KEY = os.getenv('SECRET_KEY') or 'you-cant-tell-me-nothing'
