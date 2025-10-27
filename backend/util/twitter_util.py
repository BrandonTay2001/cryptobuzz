import tweepy
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta
import requests
from xai_sdk import Client
from xai_sdk.chat import user
from xai_sdk.search import SearchParameters, x_source

load_dotenv()

class TwitterUtil:
    def __init__(self):
        self.client = tweepy.Client(
            bearer_token=os.getenv('TWITTER_BEARER_TOKEN')
        )
        self.xai_client = Client(api_key=os.getenv('X_AI_API_KEY'))
        self.ui_cookie = os.getenv('GROK_COOKIE')
        self.grok_ui_endpoint = 'https://grok.com/rest/app-chat/conversations/new'
        
    def get_mention_count(self, query):
        start_time = datetime.now() - timedelta(days=1)
        response = self.client.get_recent_tweets_count(query=query, granularity="day", start_time=start_time)
        return response.data[0]['tweet_count']
    
    def get_mention_count_grok(self, query):
        chat = self.xai_client.chat.create(
            model="grok-4-fast-reasoning",
            search_parameters=SearchParameters(mode="auto", sources=[x_source()])
        )
        chat.append(user(f"Get me the number of tweets in the past 24 hours for this search term, with or without the ticker sign or hashtags: {query}\n\nPlease use the advanced search features to limit the results to tweets in the past 24 hours. Scroll as much as possible. Provide your reasoning."))
        response = chat.sample()
        print(response.content)
        # return {'count': int(response.content)}
    
    def get_mention_count_grok_ui(self, query):
        headers = {
            'Cookie': """x-anon-token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiZjAxZjA3YjAtMWNjYy00ZjQ4LWFmMTAtNTc4MjJlNGM4MTg5IiwidGVhbV9pZCI6bnVsbCwiZXhwIjoxNzkyMDAwOTI1LCJpc19hbm9uX3VzZXIiOnRydWV9.3IqnpyvHhk6bpV0uEK1dcyaExJz3XBwFQZR3nIQSSow; _ga=GA1.1.1644407465.1760464928; x-anonuserid=52085878-aff9-4717-a6f3-f4f582731c1e; i18nextLng=en; x-challenge=EwumdM3ld78O4bwBhNXRWdHJb3kiCNCbDI%2BoU7IO%2Bcn6m4LkOJ%2FMhOIOQVo0NV%2FzSXChNwEtAnT2LZMr%2Fn%2Fc5VOfgk%2BfauJg7t7z7KjcZvfHcdIngs4%2FEf2v9xHzLC7KfWJ1AZCzLwHLsKc76m%2BUrVXjUEcgl8LJ6SEiAzQwsV9ulpTLHec%3D; x-signature=C8%2B%2Bcsy7MsNEqtyZuqTXaeV2%2F6avwZpAmDIXjolrtwoxUBmozeEzEcUFXTO867BJbMG17oQwDXMep7WXpchJGA%3D%3D; sso-rw=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzZXNzaW9uX2lkIjoiZWZiYmIwNWMtZGM3MC00YzQ2LWFhNTctMDI3NmQ2N2IxYjA5In0.M5NTDgO_8da_WiPLQFqyrOZ6IJnyM_9azJhXo24h1dQ; sso=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzZXNzaW9uX2lkIjoiZWZiYmIwNWMtZGM3MC00YzQ2LWFhNTctMDI3NmQ2N2IxYjA5In0.M5NTDgO_8da_WiPLQFqyrOZ6IJnyM_9azJhXo24h1dQ; stblid=5e8eca24-1109-478f-b45c-596fa50af1eb; mp_ea93da913ddb66b6372b89d97b1029ac_mixpanel=%7B%22distinct_id%22%3A%2219ede697-044d-4042-9dbd-11ecaf30ae11%22%2C%22%24device_id%22%3A%2280eb2c1b-08de-482d-87ca-b4c1f2db3773%22%2C%22%24initial_referrer%22%3A%22https%3A%2F%2Fgrok.com%2F%3F__cf_chl_tk%3DbuqHYcmOswi6u4nZZac0T3TR8rGj.48pUtY7cSfLTB4-1760464920-1.0.1.1-8WbDSGyxz3fcfOauaVzHZM7Zm8ETRQMXIoLCuvzCiZ8%22%2C%22%24initial_referring_domain%22%3A%22grok.com%22%2C%22__mps%22%3A%7B%7D%2C%22__mpso%22%3A%7B%7D%2C%22__mpus%22%3A%7B%7D%2C%22__mpa%22%3A%7B%7D%2C%22__mpu%22%3A%7B%7D%2C%22__mpr%22%3A%5B%5D%2C%22__mpap%22%3A%5B%5D%2C%22%24user_id%22%3A%2219ede697-044d-4042-9dbd-11ecaf30ae11%22%7D; cf_clearance=kxEajJRgDIX3ZxyBuZDBN.uGsJ8t0q.5g_4ehE5DErs-1760538640-1.2.1.1-mrXb7YZpoMKsvO.WabkzkOR4N5trHAiU6bBSCIMGzLUm3Q.HVQ3iX50NW9paAsgO..r_fYI4t_ykCOerdlEobmV094miHM1H.w0Z1g4pWkpSgSpq05ldViKfBhaGzyiZ_kmzpsJlEHq40lgOgCqFCi4rsPK.foukaAARDudJ.W2xV2A5.j7oeJyMIsrFBtLxmxc_eozRjUV.0GMyUcMK2o_hYTLye24cTlNH7WNGljiVZD3wtKcQMKnxv8V_dsFJ; _ga_8FEWB057YH=GS2.1.s1760538640$o2$g1$t1760539397$j56$l0$h0""",
            'Content-Type': 'application/json'
        }
        message = f"Get me the number of tweets in the past 24 hours for this search term, with or without the ticker sign or hashtags: {query}"
        payload = {"temporary":False,"modelName":"grok-4-mini-thinking-tahoe","message":message,"fileAttachments":[],"imageAttachments":[],"disableSearch":False,"enableImageGeneration":True,"returnImageBytes":False,"returnRawGrokInXaiRequest":False,"enableImageStreaming":True,"imageGenerationCount":2,"forceConcise":False,"toolOverrides":{},"enableSideBySide":True,"sendFinalMetadata":True,"isReasoning":False,"webpageUrls":[],"disableTextFollowUps":False,"responseMetadata":{"requestModelDetails":{"modelId":"grok-4-mini-thinking-tahoe"}},"disableMemory":False,"forceSideBySide":False,"modelMode":"MODEL_MODE_AUTO","isAsyncChat":False}
        response = requests.post(self.grok_ui_endpoint, headers=headers, json=payload)
        print(response)