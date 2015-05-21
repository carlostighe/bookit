import os
from flask import Flask, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

basedir = os.path.abspath(os.path.dirname(__file__))

bookit = Flask(__name__)
bookit.config['SECRET_KEY'] = '\x96\x03\x9aQ\x86\x99\x18\xd3t\xb5z\xe5\xc7\xec\xc3{\x93 t\\\rB\x8c\xbd'
bookit.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'bookit.db')
db = SQLAlchemy(bookit)

# Function to easily find your assets
# In your template use <link rel=stylesheet href="{{ static('filename') }}">
bookit.jinja_env.globals['static'] = (
    lambda filename: url_for('static', filename = filename)
)

# Configure authentication
login_manager = LoginManager()
login_manager.session_protection = "strong"
login_manager.login_view = "login"
login_manager.init_app(bookit)

import models
import views
