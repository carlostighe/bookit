from flask import Flask, url_for
from logging import DEBUG
import os

bookit = Flask(__name__)
bookit.logger.setLevel(DEBUG)

# Determines the destination of the build. Only usefull if you're using Frozen-Flask
bookit.config['FREEZER_DESTINATION'] = os.path.dirname(os.path.abspath(__file__))+'/../build'

# Function to easily find your assets
# In your template use <link rel=stylesheet href="{{ static('filename') }}">
bookit.jinja_env.globals['static'] = (
    lambda filename: url_for('static', filename = filename)
)

from bookit import views
