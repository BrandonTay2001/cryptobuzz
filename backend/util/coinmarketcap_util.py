import requests
import os
from dotenv import load_dotenv

load_dotenv()

class CoinmarketcapUtil:
    def __init__(self):
        self.root = "https://pro-api.coinmarketcap.com"
        self.headers = {
            "X-CMC_PRO_API_KEY": os.getenv('CMC_API_KEY'),
            "Content-Type": "application/json"
        }
        self.non_authenticated_headers = {
            "Content-Type": "application/json"
        }
        self.community_topics_url = "https://api.coinmarketcap.com/gravity/v3/gravity/today-top-topic/list"
        self.trending_listings_url = "https://api.coinmarketcap.com/data-api/v3/unified-trending/listing"

    def get_fear_and_greed_index(self):
        url = f"{self.root}/v3/fear-and-greed/latest"
        response = requests.get(url, headers=self.headers)
        return {'value': response.json()['data']['value']}
    
    def get_trending_topics(self):
        response = requests.post(self.community_topics_url, headers=self.non_authenticated_headers, json={})
        return [{'topic': topic['title']} for topic in response.json()['data']['list']]

    def get_trending_listings(self):
        payload = {"interval": "24h", "pageNum": 1, "pageSize": 10, "boostType": "hideBoost"}
        response = requests.post(self.trending_listings_url, headers=self.non_authenticated_headers, json=payload)
        return response.json()['data']['list']

# test = CoinmarketcapUtil()
# print(test.get_trending_topics())