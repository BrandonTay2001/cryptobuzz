from flask import Blueprint, jsonify

aggregates_bp = Blueprint('aggregates', __name__)

@aggregates_bp.route('/')
def aggregates_index():
    """Aggregates API endpoint"""
    return jsonify({
        'message': 'Aggregates API endpoint',
        'status': 'ok'
    })
