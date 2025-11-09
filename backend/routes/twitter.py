from flask import Blueprint, jsonify, request
from util.lunarcrush_util import LunarcrushUtil
from pymongo import MongoClient
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

def get_mongodb_connection():
    uri = f"mongodb+srv://cryptobuzzAdmin:{os.getenv('MONGODB_PASSWORD')}@cryptobuzz-cluster.dwu4ywc.mongodb.net/?appName=cryptobuzz-cluster"
    client = MongoClient(uri)
    return client['cryptobuzz']['twitter']

twitter_bp = Blueprint('twitter', __name__)

@twitter_bp.route('/fetchLeaderboard', methods=['POST'])
def fetch_leaderboard():
    lunarcrush_util = LunarcrushUtil()
    leaderboard_data = lunarcrush_util.get_top_creators()

    # Store in MongoDB
    collection = get_mongodb_connection()
    document = {
        'data_type': 'twitter_leaderboard',
        'data': leaderboard_data,
        'timestamp': datetime.now()
    }
    collection.insert_one(document)

    return jsonify({
        'status': 'success',
        'message': 'Twitter leaderboard data fetched and stored successfully'
    })

@twitter_bp.route('/getLeaderboard')
def get_leaderboard():
    collection = get_mongodb_connection()
    latest_entry = collection.find_one(
        {'data_type': 'twitter_leaderboard'},
        sort=[('timestamp', -1)]
    )
    if not latest_entry:
        return jsonify({
            'status': 'error',
            'message': 'No leaderboard data found'
        }), 404
    leaderboard_data = latest_entry['data']

    return jsonify({
        'status': 'success',
        'data': leaderboard_data
    })