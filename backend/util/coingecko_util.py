import requests
import os
from dotenv import load_dotenv

load_dotenv()

class CoingeckoUtil:
    def __init__(self):
        self.root = "https://api.coingecko.com/api/v3"
        self.headers = {
            "x-cg-pro-api-key": os.getenv('COINGECKO_API_KEY'),
            "Content-Type": "application/json"
        }

    def get_trending_coins(self):
        url = f"{self.root}/search/trending"
        response = requests.get(url, headers=self.headers)
        coin_objects = response.json()['coins']
        return [
            {'name': coin['item']['name'], 'symbol': coin['item']['symbol'], 'image': coin['item']['thumb'], 'id': coin['item']['id']} 
            for coin in coin_objects]