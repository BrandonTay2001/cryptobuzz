from flask import Blueprint, jsonify, request
from util.santiment_util import SantimentUtil
from formatters.sentiment_formatter import SentimentFormatter
from formatters.social_score_formatter import SocialScoreFormatter
from formatters.social_dominance_formatter import SocialDominanceFormatter
from pymongo import MongoClient
import os
from datetime import datetime, timedelta
from dotenv import load_dotenv
import math

load_dotenv()

def get_mongodb_connection():
    uri = f"mongodb+srv://cryptobuzzAdmin:{os.getenv('MONGODB_PASSWORD')}@cryptobuzz-cluster.dwu4ywc.mongodb.net/?appName=cryptobuzz-cluster"
    client = MongoClient(uri)
    return client['cryptobuzz']['metrics']

metrics_bp = Blueprint('metrics', __name__)

@metrics_bp.route('/')
def metrics_index():
    """Metrics API endpoint"""
    return jsonify({
        'message': 'Metrics API endpoint',
        'status': 'ok'
    })

@metrics_bp.route('/fetchSentimentWeighted', methods=['POST'])
def fetch_sentiment_weighted():
    """Get sentiment weighted metrics from Santiment and store in MongoDB"""
    try:
        santiment_util = SantimentUtil()
        negatives = santiment_util.get_sentiment_weighted_negatives()
        positives = santiment_util.get_sentiment_weighted_positives()
        combined = negatives + positives

        for obj in combined:
            obj['absoluteSentiment'] = abs(obj['sentimentWeighted'])
        sorted_combined = sorted(combined, key=lambda x: x['absoluteSentiment'], reverse=True)
        top_100 = sorted_combined[:100]

        # Store in MongoDB
        collection = get_mongodb_connection()
        document = {
            'data_type': 'sentiment_weighted',
            'data': top_100,
            'timestamp': datetime.now()
        }
        collection.insert_one(document)

        return jsonify({
            'status': 'success',
            'message': 'Sentiment weighted metrics fetched and stored successfully'
        }), 200
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

@metrics_bp.route('/fetchSocialScore', methods=['POST'])
def fetch_social_score():
    # social score = unique social volume * percentage price change
    try:
        santiment_util = SantimentUtil()
        top_social_volume_and_price_change = santiment_util.get_social_volume_and_price_change()

        filtered = [obj for obj in top_social_volume_and_price_change if obj['socialVolume'] is not None and obj['percentChange24h'] is not None]
        filtered = filtered[:100]
        
        # add a social score field and absolute social score field
        for obj in filtered:
            if not obj['percentChange24h'] or not obj['socialVolume']:
                continue
            obj['percentChange24h'] = float(obj['percentChange24h'])
            obj['socialScore'] = obj['socialVolume'] * (obj['percentChange24h'] / 100)
            obj['absoluteSocialScore'] = abs(obj['socialScore'])

        sorted_by_absolute_social_score = sorted(filtered, key=lambda x: x['absoluteSocialScore'], reverse=True)

        # store in MongoDB
        collection = get_mongodb_connection()
        document = {
            'data_type': 'social_score',
            'data': sorted_by_absolute_social_score,
            'timestamp': datetime.now()
        }
        collection.insert_one(document)
        return jsonify({
            'status': 'success',
            'message': 'Social score metrics fetched and stored successfully'
        }), 200
    
    except Exception as e:
        print(e)
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

@metrics_bp.route('/fetchSocialDominance', methods=['POST'])
def fetch_social_dominance():
    try:
        santiment_util = SantimentUtil()
        social_dominance = santiment_util.get_social_dominance()

        filtered = [obj for obj in social_dominance if obj['logoUrl'] is not None]
        filtered = filtered[:100]

        # Store in MongoDB
        collection = get_mongodb_connection()
        document = {
            'data_type': 'social_dominance',
            'data': filtered,
            'timestamp': datetime.now()
        }
        collection.insert_one(document)

        return jsonify({
            'status': 'success',
            'message': 'Social dominance metrics fetched and stored successfully'
        }), 200

    except Exception as e:
        print(e)
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

@metrics_bp.route('/getSentimentWeighted')
def get_sentiment_weighted():
    try:
        num_days = request.args.get('days', default=1, type=int)
        collection = get_mongodb_connection()
        sentiment_formatter = SentimentFormatter()
        cutoff_date = datetime.now() - timedelta(days=num_days)
        results = collection.find({
            'data_type': 'sentiment_weighted',
            'timestamp': {'$gte': cutoff_date},
        }).sort('timestamp', -1)

        data_list = [r['data'] for r in results]
        formatted_data, coin_count, total_absolute_sentiment = sentiment_formatter.format_sentiment_data(data_list, num_days)
        return jsonify({
            'status': 'success',
            'data': formatted_data,
            'count': coin_count,
            'totalAbsoluteSentiment': total_absolute_sentiment
        }), 200
    except Exception as e:
        print(e)
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500
    
@metrics_bp.route('/getSocialScore')
def get_social_score():
    try:
        num_days = request.args.get('days', default=1, type=int)
        collection = get_mongodb_connection()
        social_score_formatter = SocialDominanceFormatter()
        cutoff_date = datetime.now() - timedelta(days=num_days)
        results = collection.find({
            'data_type': 'social_score',
            'timestamp': {'$gte': cutoff_date}
        }).sort('timestamp', -1)

        data_list = [r['data'] for r in results]
        formatted_data, coin_count, total_absolute_social_score = social_score_formatter.format_social_score_data(data_list, num_days)
        return jsonify({
            'status': 'success',
            'data': formatted_data,
            'count': coin_count,
            'totalAbsoluteSocialScore': total_absolute_social_score
        }), 200
    except Exception as e:
        print(e)
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

@metrics_bp.route('/getSocialDominance')
def get_social_dominance():
    try:
        collection = get_mongodb_connection()
        social_dominance_formatter = SocialDominanceFormatter()
        result = collection.find_one(
            {'data_type': 'social_dominance'},
            sort=[('timestamp', -1)]
        )

        formatted_data, coin_count, total_percentage = social_dominance_formatter.format_single_social_dominance_data(result['data'])
        return jsonify({
            'status': 'success',
            'data': formatted_data,
            'count': coin_count,
            'totalPercentage': total_percentage
        }), 200
    except Exception as e:
        print(e)
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500