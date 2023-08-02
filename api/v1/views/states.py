#!/usr/bin/python3
"""
View for State objects that handles all default API
"""
from flask import Blueprint, request, jsonify, abort
from models.state import State


states_bp = Blueprint('states', __name__, url_prefix='/api/v1/states')


@states_bp.route('', methods=['GET'])
def get_all_states():
    states = State.query.all()
    return jsonify([state.to_dict() for state in states]), 200


@states_bp.route('/<int:state_id>', methods=['GET'])
def get_state(state_id):
    state = State.quety.get(state_id)
    if not state:
        abort(404)
    return jsonify(state.to_dict()), 200


@states_bp.route('/<int:state_id>', methods=['DELETE'])
def delete_state(state_id):
    state = State.query.get(state_id)
    if not state:
        abort(404)
    state.delete()
    return jsonify({}), 200


@states_bp.route('', methods=['POST'])
def create_state():
    data = request.get_json()
    if not data:
        abort(400, 'Not a JSON')
    if 'name' not in data:
        abort(400, 'Missing name')
    state = State(**data)
    state.save()
    return jsonify(state.to_dict()), 201


@states_bp.route('/<int:state_id>', methods=['PUT'])
def update_state(state_id):
    state = State.query.get(state_id)
    if not state:
        abort(404)
    data = request.get_json()
    if not data:
        abort(400, 'Not a JSON')
    ignored_keys = ['id', 'created_at', 'updated_at']
    for key, value in data.items():
        if key not in ignored_keys:
            setattr(state, key, value)
    state.save()
    return jsonify(state.to_dict()), 200
