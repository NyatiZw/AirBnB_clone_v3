#!/usr/bin/python3
"""
Amenity Api handles
"""
from flask import Blueprint, request, jsonify, abort
from models.amenity import Amenity


amenities_bp = Blueprint('amenities', __name__, url_prefix='/api/v1/amenities')


@amenities_bp.route('', methods=['GET'])
def get_all_amenities():
    amenities = Amenity.query.all()
    return jsonify([amenity.to_dict() for amenity in amenities]), 200


@amenities_bp.route('/<int:amenity_id>', methods=['GET'])
def get_amenity(amenity_id):
    amenity = Amenity.query.get(amenity_id)
    if not amenity:
        abort(404)
    return jsonify(amenity.to_dict()), 200


@amenities_bp.route('/<int:amenity_id>', methods=['DELETE'])
def delete_amenity(amenity_id):
    amenity = Amenity.query.get(amenity_id)
    if not amenity:
        abort(404)
    amenity.delete()
    return jsonify({}), 200


@amenities_bp.route('', methods=['POST'])
def create_amenity():
    data = request.get_json()
    if not data:
        abort(400, 'Not a JSON')
    if 'name' not in data:
        abort(400, 'Missing name')
    amenity = Amenity(name=data['name'])
    amenity.save()
    return jsonify(amenity.to_dict()), 201


@amenities_bp.route('/<int:amenity_id>', methods=['PUT'])
def update_amenity(amenity_id):
    amenity = Amenity.query.get(amenity_id)
    if not amenity:
        abort(404)
    data = request.get_json()
    if not data:
        abort(400, 'Not a JSON')
    ignored_keys = ['id', 'created_at', 'updated_at']
    for key, value in data.items():
        if key not in ignored_keys:
            setattr(amenity, key, value)
    amenity.save()
    return jsonify(amenity.to_dict()), 200
