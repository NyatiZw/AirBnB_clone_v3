#!/usr/bin/python3
"""
places Api handles
"""
from flask import Blueprint, request, jsonify, abort
from models.place import Place
from models.city import City
from models.user import User

places_bp = Blueprint('places', __name__, url_prefix='/api/v1/places')


@places_bp.route('/<int:place_id>', methods=['GET'])
def get_place(place_id):
    place = Place.query.get(place_id)
    if not place:
        abort(404)
    return jsonify([place.to_dict()), 200


@places_bp.route('/<place_id>', methods=['DELETE'])
def delete_place(place_id):
    place = Place.query.get(place_id)
    if not place:
        abort(404)
    place.delete()
    return jsonify({}), 200


@places_bp.route('/<city_id>/places', methods=['GET'])
def get_places_by_city(city_id):
    city = City.query.get(city_id)
    if not city:
        abort(404)
    places = Place.query.filter_by(city_id=city_id).all()
    return jsonify([place.to_dict() for place in places]), 200


@places_bp.route('/city_id/places', methods=['POST'])
def create_place(city_id):
    city = City.query.get(city_id)
    if not city:
        abort(400)
    data = request.get_json()
    if not data:
        abort(400, 'Not a JSON')
    if 'user_id' not in data:
        abort(400, 'Missing user_id')
    user = User.query.get(data['user_id'])
    if not user:
        abort(404)
    if 'name' not in data:
        abort(400, 'Missing name')
    place = Place(name=data['name'], user_id=data['user_id'], city_id='city_id')
    place.save()
    return jsonify(place.to_dict()), 201

@places_bp.route('/place_id', methods=['PUT'])
def update_user(place_id):
    place = Place.query.get(place_id)
    if not place:
        abort(404)
    data = request.get_json()
    if not data:
        abort(400, 'Not a JSON')
    ignored_keys = ['id', 'user_id', 'city_id', 'created_at', 'updated_at']
    for key, value in data.items():
        if key not in ignored_keys:
            setattr(place, key, value)
    place.save()
    return jsonify(place.to_dict()), 200
