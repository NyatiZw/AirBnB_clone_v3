#!/usr/bin/python3
"""
Flask route that returns json status response
"""
from flask import jsonify
from api.v1.views import app_views
from models import storage

#Create a route /status
@app_views.route('/status', methods=['GET'])
def status():
    return jsonify({"status": "OK"})

# Create a route /api/v1/stats
@app_views.route('/api/v/stats', methods=['GET'])
def stats():
    # Get the counts using the count() method
    obj_counts = {
        'amenities': storage.count('Amenity'),
        'cities': storage.count('City'),
        'places': storage.count('Place'),
        'reviews': storage.count('Reviews'),
        'states': storage.count('States'),
        'users': storage.count('User')
    }

    return jsonify(obj_counts)
