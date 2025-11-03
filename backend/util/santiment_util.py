import san
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()
san.ApiConfig.api_key = os.getenv('SANTIMENT_API_KEY')

class SantimentUtil:
    def __init__(self):
        pass

    def execute_query_by_path(self, path, queryType):
        with open(path, 'r') as file:
            query = file.read()
        return self.execute_query(query, queryType)

    def execute_query(self, query, queryType):
        result = san.graphql.execute_gql(query)
        jsonList = result[queryType]
        return jsonList

    def get_sentiment_weighted_negatives(self):
        return self.execute_query_by_path('./graphql/sentimentWeightedNegatives.graphql', 'allProjects')
    
    def get_sentiment_weighted_positives(self):
        return self.execute_query_by_path('./graphql/sentimentWeightedPositives.graphql', 'allProjects')
    
    def get_social_volume_and_price_change(self):
        return self.execute_query_by_path('./graphql/socialVolumeAndPriceChange.graphql', 'allProjects')

    def get_social_dominance(self):
        return self.execute_query_by_path('./graphql/socialDominance.graphql', 'allProjects')