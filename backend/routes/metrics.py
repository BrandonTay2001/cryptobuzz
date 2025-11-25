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

timespans = ['day', 'week', 'month']

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
    santiment_util = SantimentUtil()

    for timespan in timespans:
        negatives = santiment_util.get_sentiment_weighted_negatives(timespan)
        positives = santiment_util.get_sentiment_weighted_positives(timespan)
        combined = negatives + positives

        ticker_to_obj = {}
        for obj in combined:
            ticker = obj['ticker']
            if ticker in ticker_to_obj:
                pass
            else:
                ticker_to_obj[ticker] = obj
        combined = list(ticker_to_obj.values())


        for obj in combined:
            obj['absoluteSentiment'] = abs(obj['sentimentWeighted'])
            obj['name'] = obj['name'].split(' (')[0].split(' [')[0]
        sorted_combined = sorted(combined, key=lambda x: x['absoluteSentiment'], reverse=True)
        top_100 = sorted_combined[:100]

        # Store in MongoDB
        collection = get_mongodb_connection()
        document = {
            'data_type': f'sentiment_weighted_{timespan}',
            'data': top_100,
            'timestamp': datetime.now()
        }
        collection.insert_one(document)

    return jsonify({
        'status': 'success',
        'message': 'Sentiment weighted metrics fetched and stored successfully'
    }), 200

@metrics_bp.route('/fetchSocialScore', methods=['POST'])
def fetch_social_score():
    # social score = unique social volume * percentage price change
    santiment_util = SantimentUtil()
    
    for timespan in timespans:
        top_social_volume_and_price_change = santiment_util.get_social_volume_and_price_change(timespan=timespan)

        filtered = [obj for obj in top_social_volume_and_price_change if obj['socialVolume'] is not None and obj['percentChange24h'] is not None]
        
        ticker_to_obj = {}
        for obj in filtered:
            ticker = obj['ticker']
            if ticker in ticker_to_obj:
                ticker_to_obj[ticker]['socialVolume'] += obj['socialVolume']
                print(ticker_to_obj[ticker])
            else:
                ticker_to_obj[ticker] = obj
        filtered = list(ticker_to_obj.values())

        filtered = filtered[:100]
        
        # add a social score field and absolute social score field
        for obj in filtered:
            if not obj['percentChange24h'] or not obj['socialVolume']:
                continue
            obj['percentChange24h'] = float(obj['percentChange24h'])
            obj['socialScore'] = obj['socialVolume'] * (obj['percentChange24h'] / 100)
            obj['absoluteSocialScore'] = abs(obj['socialScore'])
            obj['name'] = obj['name'].split(' (')[0].split(' [')[0]

        sorted_by_absolute_social_score = sorted(filtered, key=lambda x: x['absoluteSocialScore'], reverse=True)

        # store in MongoDB
        collection = get_mongodb_connection()
        document = {
            'data_type': f'social_score_{timespan}',
            'data': sorted_by_absolute_social_score,
            'timestamp': datetime.now()
        }
        collection.insert_one(document)
    return jsonify({
        'status': 'success',
        'message': 'Social score metrics fetched and stored successfully'
    }), 200

@metrics_bp.route('/fetchSocialDominance', methods=['POST'])
def fetch_social_dominance():
    santiment_util = SantimentUtil()

    for timespan in timespans:
        social_dominance = santiment_util.get_social_dominance(timespan)

        filtered = [obj for obj in social_dominance if obj['logoUrl'] is not None]

        ticker_to_obj = {}
        for obj in filtered:
            ticker = obj['ticker']
            if ticker in ticker_to_obj:
                ticker_to_obj[ticker]['socialDominance'] += obj['socialDominance']
                print(ticker_to_obj[ticker])
            else:
                ticker_to_obj[ticker] = obj
        
        filtered = list(ticker_to_obj.values())
        for obj in filtered:
            obj['name'] = obj['name'].split(' (')[0].split(' [')[0]

        filtered = filtered[:100]

        # Store in MongoDB
        collection = get_mongodb_connection()
        document = {
            'data_type': f'social_dominance_{timespan}',
            'data': filtered,
            'timestamp': datetime.now()
        }
        collection.insert_one(document)

    return jsonify({
        'status': 'success',
        'message': 'Social dominance metrics fetched and stored successfully'
    }), 200

@metrics_bp.route('/getSentimentWeighted')
def get_sentiment_weighted():
    num_days = request.args.get('days', default=1, type=int)
    collection = get_mongodb_connection()
    sentiment_formatter = SentimentFormatter()

    timespan = 'day'
    if num_days == 1:   timespan = 'day'
    elif num_days <= 7: timespan = 'week'
    else:               timespan = 'month'
    
    result = collection.find_one({
        'data_type': f'sentiment_weighted_{timespan}',
    }, sort=[('timestamp', -1)])

    data_list = [result['data']]
    formatted_data, coin_count, total_absolute_sentiment = sentiment_formatter.format_sentiment_data(data_list)
    return jsonify({
        'status': 'success',
        'data': formatted_data,
        'count': coin_count,
        'totalAbsoluteSentiment': total_absolute_sentiment
    }), 200
    
@metrics_bp.route('/getSocialScore')
def get_social_score():
    num_days = request.args.get('days', default=1, type=int)
    collection = get_mongodb_connection()
    social_score_formatter = SocialScoreFormatter()

    timespan = 'day'
    if num_days == 1:   timespan = 'day'
    elif num_days <= 7: timespan = 'week'
    else:               timespan = 'month'

    result = collection.find_one({
        'data_type': f'social_score_{timespan}',
    }, sort=[('timestamp', -1)])

    data_list = [result['data']]
    formatted_data, coin_count, total_absolute_social_score = social_score_formatter.format_social_score_data(data_list)
    return jsonify({
        'status': 'success',
        'data': formatted_data,
        'count': coin_count,
        'totalAbsoluteSocialScore': total_absolute_social_score
    }), 200

@metrics_bp.route('/getSocialDominance')
def get_social_dominance():
    num_days = request.args.get('days', default=1, type=int)
    collection = get_mongodb_connection()
    social_dominance_formatter = SocialDominanceFormatter()

    timespan = 'day'
    if num_days == 1:   timespan = 'day'
    elif num_days <= 7: timespan = 'week'
    else:               timespan = 'month'

    result = collection.find_one(
        {'data_type': f'social_dominance_{timespan}'},
        sort=[('timestamp', -1)]
    )

    formatted_data, coin_count, total_percentage = social_dominance_formatter.format_single_social_dominance_data(result['data'])
    return jsonify({
        'status': 'success',
        'data': formatted_data,
        'count': coin_count,
        'totalPercentage': total_percentage
    }), 200