from flask import Blueprint, jsonify

metrics_bp = Blueprint('metrics', __name__)

@metrics_bp.route('/')
def metrics_index():
    """Metrics API endpoint"""
    return jsonify({
        'message': 'Metrics API endpoint',
        'status': 'ok'
    })