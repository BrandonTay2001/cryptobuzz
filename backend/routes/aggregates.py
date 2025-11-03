from flask import Blueprint, jsonify
from util.coingecko_util import CoingeckoUtil
from util.coinmarketcap_util import CoinmarketcapUtil
from util.twitter_util import TwitterUtil
from pymongo import MongoClient
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

def get_mongodb_connection():
    uri = f"mongodb+srv://cryptobuzzAdmin:{os.getenv('MONGODB_PASSWORD')}@cryptobuzz-cluster.dwu4ywc.mongodb.net/?appName=cryptobuzz-cluster"
    client = MongoClient(uri)
    return client['cryptobuzz']['aggregates']

aggregates_bp = Blueprint('aggregates', __name__)

@aggregates_bp.route('/fetchTrendingCoins', methods=['POST'])
def get_trending_coins():
    """Get top 5 trending coins from CoinGecko and store in MongoDB"""
    coingecko_util = CoingeckoUtil()
    trending_coins = coingecko_util.get_trending_coins()
    top_5_coins = trending_coins[:5]
    
    # Store in MongoDB
    collection = get_mongodb_connection()
    document = {
        'data_type': 'trending_coins',
        'data': top_5_coins,
        'timestamp': datetime.now()
    }
    collection.insert_one(document)
    
    return jsonify({
        'status': 'success',
        'message': 'Trending coins data stored successfully'
    })

@aggregates_bp.route('/fetchTrendingTopics', methods=['POST'])
def get_trending_topics():
    """Get top 5 trending topics from CoinMarketCap and store in MongoDB"""
    coinmarketcap_util = CoinmarketcapUtil()
    trending_topics = coinmarketcap_util.get_trending_topics()
    top_5_topics = trending_topics[:5]
    
    # Store in MongoDB
    collection = get_mongodb_connection()
    document = {
        'data_type': 'trending_topics',
        'data': top_5_topics,
        'timestamp': datetime.now()
    }
    collection.insert_one(document)
    
    return jsonify({
        'status': 'success',
        'message': 'Trending topics data stored successfully'
    })

@aggregates_bp.route('/fetchFearAndGreed', methods=['POST'])
def get_fear_and_greed():
    """Get current fear and greed index with classification from CoinMarketCap and store in MongoDB"""
    coinmarketcap_util = CoinmarketcapUtil()
    fear_and_greed_data = coinmarketcap_util.get_fear_and_greed_index()
    
    # Store in MongoDB
    collection = get_mongodb_connection()
    document = {
        'data_type': 'fear_and_greed_index',
        'data': fear_and_greed_data,
        'timestamp': datetime.now()
    }
    collection.insert_one(document)
    
    return jsonify({
        'status': 'success',
        'message': 'Fear and greed index data stored successfully'
    })

@aggregates_bp.route('/getLatest')
def get_latest():
    """Get the latest data for trending coins, topics, and fear and greed index"""
    collection = get_mongodb_connection()
    
    # Get latest trending coins
    latest_coins = collection.find_one(
        {'data_type': 'trending_coins'},
        sort=[('timestamp', -1)]
    )
    
    # Get latest trending topics
    latest_topics = collection.find_one(
        {'data_type': 'trending_topics'},
        sort=[('timestamp', -1)]
    )
    
    # Get latest fear and greed index
    latest_fear_greed = collection.find_one(
        {'data_type': 'fear_and_greed_index'},
        sort=[('timestamp', -1)]
    )
    
    # Get latest social volume
    latest_social_volume = collection.find_one(
        {'data_type': 'total_social_volume'},
        sort=[('timestamp', -1)]
    )
    
    response_data = {
        'trending_coins': {},
        'trending_topics': {},
        'fear_and_greed_index': {},
        'total_social_volume': {}
    }
    
    if latest_coins:
        transformed_coins = []
        for coin in latest_coins['data']:
            transformed_coins.append({
                'name': coin['name'],
                'symbol': coin['symbol'],
                'image': coin['image'],
                'coingeckoLink': f"https://www.coingecko.com/en/coins/{coin['id']}"
            })

        response_data['trending_coins'] = {
            'data': transformed_coins,
            'count': len(transformed_coins),
            'timestamp': latest_coins['timestamp']
        }
    
    if latest_topics:
        response_data['trending_topics'] = {
            'data': latest_topics['data'],
            'count': latest_topics['count'],
            'timestamp': latest_topics['timestamp']
        }
    
    if latest_fear_greed:
        response_data['fear_and_greed_index'] = {
            'data': latest_fear_greed['data'],
            'timestamp': latest_fear_greed['timestamp']
        }
    
    if latest_social_volume:
        response_data['total_social_volume'] = {
            'data': latest_social_volume['data'],
            'timestamp': latest_social_volume['timestamp']
        }
    
    return jsonify({
        'status': 'success',
        'data': response_data
    })

@aggregates_bp.route('/fetchTotalSocialVolume', methods=['POST'])
def get_total_social_volume():
    """Get total social volume for major crypto terms and store in MongoDB"""
    twitter_util = TwitterUtil()
    crypto_query = "crypto OR #crypto OR cryptocurrency OR bitcoin OR #btc OR ethereum OR #eth"
    mention_count = twitter_util.get_mention_count(crypto_query)
    
    # Store in MongoDB
    collection = get_mongodb_connection()
    document = {
        'data_type': 'total_social_volume',
        'data': {
            'mention_count': mention_count
        },
        'timestamp': datetime.now()
    }
    collection.insert_one(document)
    
    return jsonify({
        'status': 'success',
        'message': 'Total social volume data stored successfully'
    })
