from flask import Blueprint, jsonify

users_bp = Blueprint("users", __name__)

@users_bp.route("/users", methods=["GET"])
def get_users():
    return jsonify([{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}])