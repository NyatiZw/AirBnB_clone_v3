#!/usr/bin/python3
"""
flask route
"""
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from models import storage, CNC


@app_views.route('/states', methods=['GET', 'POST'])
def no_states_id():
    """
    Route to handle requests with no id
    """
    if request.method == 'GET':
        all_states = storage.all('State')
        all_states = list(obj.to_json() for obj in all_states.values())
        return jsonify(all_states)

    if request.method == 'POST':
        request_json = request.get_json()
        if request_json is None:
            abort(400, 'Not a json')
        if request_json.get("name") is None:
            abort(400, 'Missing name')
        State = CNC.get("State")
        new_object = State(**request_json)
        new_object.save()
        return jsonify(new_object.to_json()), 201


@app_views.route('/states/<state_id>', method=['GET', 'DELETE', 'PUT'])
def states_id(state_id=None):
    """
    Route to handle state id requests
    """
    state_obj = storage.get('State', state_id)
    if state_obj is None:
        abort(404, 'Not found')

    if request.method == 'GET':
        return jsonify(state_obj.to_json())

    if request.method == 'DELETE':
        state_obj.delete()
        del state_obj
        return jsonify({})

    if request.method == 'PUT':
        request_json = request.get_json()
        if request_json is None:
            abort(400, 'Not a JSON')
        state_obj.bm_update(request_json)
        return jsonify(state_obj.to_json())
