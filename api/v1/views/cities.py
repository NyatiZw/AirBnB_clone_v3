#!/usr/bin/python3

"""
API to return CIty objects
"""
from flask import Blueprint, request, jsonify, abort
from models.city import City
from models.state import State


cities_bp = Blueprint('cities', __name__, url_prefix='/api/v1/cities')


@cities_bp.route('/<int:city_id>', methods=['GET'])
def get_city(city_id):
    city = City.query.get(city_id)
    if not city:
        abort(404)
    return jsonify(city.to_dict()), 200


@cities_bp.route('/<int:city_id>', methods=['DELETE'])
def delete_city(city_id):
    city = City.query.get(city_id)
    if not city:
        abort(404)
    city.delete()
    return jsonify({}), 200


@cities_bp.route('/<int:state_id>/cities', methods=['GET'])
def get_cities_by_state(state_id):
    state = State.query.get(state_id)
    if not state:
        abort(404)
    cities = City.query.filter_by(state_id=state_id).all()
    return jsonify([city.to_dict() for city in cities]), 200


@cities_bp.route('/<int:state_id>/cities', methods=['POST'])
def create_city(state_id):
    state = State.query.get(state_id)
    if not state:
        abort(404)
    data = request.get_json()
    if not data:
        abort(400, 'Not a JSON')
    if 'name' not in data:
        abort(400, 'Missing name')
    city = City(name=data['name'], state_id=state_id)
    city.save()
    return jsonify(city.to_dict()), 201


@cities_bp.route('/<int:city_id', methods=['PUT'])
def update_city(city_id):
    city = City.query.get(city_id)
    if not city:
        abort(404)
    data = request.get_json()
    if not data:
        abort(400, 'Not a JSON')
    ignored_keys = ['id', 'state_id', 'created_at', 'updated_at']
    for key, value in dta.items():
        if key not in ignored_keys:
            setattr(city, key, value)
    city.save()
    return jsonify(city.to_dict()), 200
