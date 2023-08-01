#!/usr/bin/python3
"""
Flask route that returns json status response
"""
from flask import jsonify
from api.v.views import app_views
from models import storage

#Create a route /status
@app_view.route('/status', methods=['GET'])
def status():
    return jsonify({"status": "OK"})

#create a route /api/v1/stats
@app_views.route('/api/v1/stats', methods=['GET'])
def stats():
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
