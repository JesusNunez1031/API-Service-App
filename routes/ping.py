from flask import Blueprint, jsonify

ping_bp = Blueprint('ping', __name__)

@ping_bp.route('/ping', methods=['GET'])
def ping_service():
    return jsonify({'response': 'Pong! Service is up!'})