import requests
import os
from dotenv import load_dotenv

load_dotenv()

class LunarcrushUtil:
    def __init__(self):
        self.root = "https://lunarcrush.com/api4/public"
        self.headers = {
            "Authorization": "Bearer " + os.getenv('LUNARCRUSH_API_KEY'),
            "Content-Type": "application/json"
        }

    def get_top_creators(self):
        url = f"{self.root}/category/cryptocurrencies/creators/v1"
        response = requests.get(url, headers=self.headers)
        response = response.json()
        data = response.get('data', [])
        formatted = []
        rank = 1
        for dataObject in data:
            if 'twitter' in dataObject['creator_id']:
                formatted.append({
                    'rank': rank,
                    'name': dataObject['creator_name'],
                    'avatar': dataObject.get('creator_avatar', ''),
                    'link': f"https://x.com/{dataObject['creator_name']}",
                    'followers': dataObject['creator_followers'],
                    'dailyInteractions': dataObject['interactions_24h'],
                })
                rank += 1
        return formatted[:100]