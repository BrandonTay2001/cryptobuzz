from flask import Blueprint, jsonify
from util.coindesk_rss_util import CoindeskRSSUtil
from pymongo import MongoClient
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

def get_mongodb_connection():
    uri = f"mongodb+srv://cryptobuzzAdmin:{os.getenv('MONGODB_PASSWORD')}@cryptobuzz-cluster.dwu4ywc.mongodb.net/?appName=cryptobuzz-cluster"
    client = MongoClient(uri)
    return client['cryptobuzz']['news']

news_bp = Blueprint('news', __name__)

@news_bp.route('/')
def news_index():
    """News API endpoint"""
    return jsonify({
        'message': 'News API endpoint',
        'status': 'ok'
    })

@news_bp.route('/fetchNews', methods=['POST'])
def fetch_news():
    """Get top 10 news articles from CoinDesk RSS and store in MongoDB"""
    try:
        coindesk_util = CoindeskRSSUtil()
        news_articles = coindesk_util.get_top_news_articles(limit=10)
        
        # Store in MongoDB
        collection = get_mongodb_connection()
        document = {
            'data_type': 'top_news_articles',
            'data': news_articles,
            'count': len(news_articles),
            'timestamp': datetime.utcnow()
        }
        collection.insert_one(document)
        
        return jsonify({
            'status': 'success',
            'message': 'News articles data stored successfully'
        })
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

@news_bp.route('/getLatest')
def get_latest():
    """Get the latest news articles data"""
    try:
        collection = get_mongodb_connection()
        
        # Get latest news articles
        latest_news = collection.find_one(
            {'data_type': 'top_news_articles'},
            sort=[('timestamp', -1)]
        )
        
        if latest_news:
            articles = [obj['paraphrased_title'] for obj in latest_news['data']]
        else:
            articles = []
        
        return jsonify({
            'status': 'success',
            'data': {
                'articles': articles
            }
        })
        
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500