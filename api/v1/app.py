#!/usr/bin/python3
"""
API to return status
"""

from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views
import os
from flask_cors import CORS, cross_origin

#Flask Application Variable
app = Flask(__name__)

app.url_map.strict_slashes = False

#Register blueprint app_views for Flask instance
app.register_blueprint(app_views)

# Declare a method to handle teardown
def teardown(exception):
    storage.close()

# Flask server environment setup
host = os.getenv('HBNB_API_HOST', '0.0.0.0')
port = os.getenv('HBNB_API_PORT', 5000)

cors = CORS(app, resources={r'/*': {'origins': host}})


If __name__ == '__main__':
    """
    MAIN FLASK APP
    """
    app.run(host=host, port=port)
