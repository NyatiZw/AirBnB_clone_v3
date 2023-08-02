#!/usr/bin/python3
"""
API to return status
"""
from flask import Flask, jsonify, make_response, render_template, url_for
from models import storage
from api.v1.views import app_views
import os
from flask_cors import CORS, cross_origin
from werkzeug.exceptions import HTTPException

# Flask Application Variable: app
app = Flask(__name__)

# global strict slashes
app.url_map.strict_slashes = False

# Flask server environment setup
host = os.getenv('HBNB_API_HOST', '0.0.0.0')
port = os.getenv('HBNB_API_PORT', 5000)

# Cross-Origin Resource Sharing
cors = CORS(app, resources={r'/*': {'origins': host}})

# Register blueprint app_views for Flask instance
app.register_blueprint(app_views)


# Declare a method to handle teardown"""
@app.teardown_appcontext
def teardown_database(exception):
    """
    removes current SQLAlchemy
    after each request
    """
    storage.close()


@app.errorhandler(Exception)
def global_error_handler(err):
    """
    Global Route for all errors
    """
    if isinstance(err, HTTPException):
        if type(err).__name__ == 'NotFound':
            err.description = "Not Found"
        message = {'error': err.description}
        error_code = err.code
    else:
        message = {'error': err}
        error_code = 500
    return make_response(jsonify(message), error_code)


def setup_global_errors():
    """
    This updates HTTPException Class
    """
    for cls in HTTPException.__subclasses__():
        app.register_error_handler(cls, global_error_handler)


if __name__ == '__main__':
    """
    MAIN Flask App
    """
    app.run(host=host, port=port)
