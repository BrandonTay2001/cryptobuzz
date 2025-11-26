from flask import Blueprint, jsonify, request
from pymongo import MongoClient
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

def get_mongodb_connection():
    uri = f"mongodb+srv://cryptobuzzAdmin:{os.getenv('MONGODB_PASSWORD')}@cryptobuzz-cluster.dwu4ywc.mongodb.net/?appName=cryptobuzz-cluster"
    client = MongoClient(uri)
    return client['cryptobuzz']['admin']

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/blacklistCoin', methods=['POST'])
def blacklist_coin():
    data = request.get_json()
    coin_ticker = data.get('ticker')
    if not coin_ticker:
        return jsonify({'status': 'error', 'message': 'Ticker is required'}), 400
    collection = get_mongodb_connection()
    document = {
        'type': 'blacklist',
        'ticker': coin_ticker,
        'timestamp': datetime.now()
    }
    collection.insert_one(document)

    return jsonify({'status': 'success', 'message': f'{coin_ticker} has been blacklisted'}), 200