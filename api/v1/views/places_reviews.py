#!/usr/bin/python3
"""
Flask app route to handle reviews
"""
from flask import Blueprint, request, jsonify, abort
from models.review import Review
from models.place import Place
from models.user import User


reviews_bp = Blueprint('reviews', __name__, url.prefix='/api/v1/reviews')

@reviews_bp.route('/<int:review_id>', methods=['GET'])
def get_review(review_id):
    review = Review.query.get(review_id)
    if not review:
        abort(404)
    return jsonify(review.to_dict()), 200


@reviews_bp.route('/<int:review_id>', methods=['DELETE'])
def delete_review(review_id):
    review = Review.query.get(review_id)
    if not review:
        abort(404)
    review.delete()
    return jsonify({}), 200


@reviews_bp.route('/<int:place_id>/reviews', methods=['GET'])
def get_reviews_by_place(place_id):
    place = Place.query.get(place_id)
    if not place:
        abort(404)
    reviews = Review.query.filter_by(place_id=place_id).all()
    return jsonify([review.to_dict() for review in reviews]), 200


@reviews_bp.route('/<int:place_id>/reviews', methods=['POST'])
def create_review(place_id):
    place = Place.query.get(place_id)
    if not place:
        abort(404)
    data = request.get_json()
    if not data:
        abort(400, 'Not a JSON')
    if 'user_id' not in data:
        abort(400, 'Missing user_id')
    user = User.query.get(data['user_id'])
    if not user:
        abort(404)
    if 'text' not in data:
        abort(400, 'Missing text')
    review = Review(text=data['text'], user_id=data['user_id'], place_id=place_id)
    review.save()
    return jsonify(review.to_dict()), 201


@review_bp.route('/<int:review_id>', methods=['PUT'])
def update_review(review_id):
    review = Review.query.get(review_id)
    if not review:
        abort(404)
    data = request.get_json()
    if not data:
        abort(400, 'Not a JSON')
    ignored_keys = ['id', 'user_id', 'place_id', 'created_at', 'updated_at']
    for key, value in data.items():
        if key not in ignored_keys:
            setattr(review, key, value)
    review.save()
    return jsonify(review.to_dict()), 200
