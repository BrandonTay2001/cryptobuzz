from flask import Blueprint, jsonify, request

twitter_bp = Blueprint('twitter', __name__)

@twitter_bp.route('/getLeaderboard')
def get_leaderboard():
    """Get Twitter leaderboard data"""
    # Placeholder implementation
    leaderboard_data = [
        {'username': 'crypto_influencer1', 'followers': 150000},
        {'username': 'crypto_influencer2', 'followers': 120000},
        {'username': 'crypto_influencer3', 'followers': 100000},
    ]
    return jsonify({
        'status': 'success',
        'data': leaderboard_data
    })