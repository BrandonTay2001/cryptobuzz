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
        return response.json()

# test = LunarcrushUtil()
# print(test.get_top_creators())