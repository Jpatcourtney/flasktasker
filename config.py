import os

# grabs the folder where this script lives
basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE = 'flasktasker.db'
USERNAME = 'admin'
PASSWORD = 'password'
WTF_CSRF_ENABLED = True
SECRET_KEY = 'dont_you_ever_guess_this_please'

# define the full path for the DATABASE
DATABASE_PATH = os.path.join(basedir, DATABASE)