#!/usr/bin/python3
"""
Flask route that returns json status response
"""
from flask import jsonify, request
from api.v1.views import app_views
from models import storage


@app_views.route('/status', methods=['GET'])
def status():
    """
    function for status route that returns the status
    """
    if request.method == 'GET':
        response = {"status": "OK"}
        return jsonify(response)


@app_views.route('/stats', methods=['GET'])
def stats():
    """
    function to return the count of all class objects
    """
    if request.method == 'GET':
        response = {}
        obj_counts = {
            'amenities': storage.count('Amenity'),
            'cities': storage.count('City'),
            'places': storage.count('Place'),
            'states': storage.count('States'),
            'reviews': storage.count('Reviews'),
            'users': storage.count('User')
        }
        for k, value in obj_counts.items():
            response[k] = value
        return jsonify(response)
