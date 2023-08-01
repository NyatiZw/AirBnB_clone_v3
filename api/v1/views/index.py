#!/usr/bin/python3
"""
Flask route that returns json status response
"""
from flask import jsonify
from api.v1.views import app_views
from models import storage

"""Create a route /status"""
@app_view.route('/status', methods=['GET'])
def status():
    """
    function for status route that returns the status
    """
    return jsonify({"status": "OK"})


"""Create a route /api/v1/stats"""
@app_views.route('/api/v1/stats', methods=['GET'])
def stats():
    """
    function to return the count of all class objects
    """
    @Get the count using the count() method
    obj_counts = {
        'amenities': storage.count('Amenity'),
        'cities': storage.count('City'),
        'places': storage.count('Place'),
        'states': storage.count('States'),
        'reviews': storage.count('Reviews'),
        'users': storage.count('User')
    }

    return jsonify(obj_counts)
