from flask import Blueprint, jsonify

news_bp = Blueprint('news', __name__)

@news_bp.route('/')
def news_index():
    """News API endpoint"""
    return jsonify({
        'message': 'News API endpoint',
        'status': 'ok'
    })