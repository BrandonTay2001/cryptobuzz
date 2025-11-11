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

    def get_sentiment_weighted_negatives(self, timespan='day'):
        if timespan == 'day':
            return self.execute_query_by_path('./graphql/sentimentWeightedNegatives.graphql', 'allProjects')
        elif timespan == 'week':
             return self.execute_query_by_path('./graphql/sentimentWeightedNegatives_sevenDays.graphql', 'allProjects')
        else:
            return self.execute_query_by_path('./graphql/sentimentWeightedNegatives_thirtyDays.graphql', 'allProjects')
    
    def get_sentiment_weighted_positives(self, timespan='day'):
        if timespan == 'day':
            return self.execute_query_by_path('./graphql/sentimentWeightedPositives.graphql', 'allProjects')
        elif timespan == 'week':
             return self.execute_query_by_path('./graphql/sentimentWeightedPositives_sevenDays.graphql', 'allProjects')
        else:
            return self.execute_query_by_path('./graphql/sentimentWeightedPositives_thirtyDays.graphql', 'allProjects')
    
    def get_social_volume_and_price_change(self, timespan='day'):
        if timespan == 'day':
            return self.execute_query_by_path('./graphql/socialVolumeAndPriceChange.graphql', 'allProjects')
        elif timespan == 'week':
             return self.execute_query_by_path('./graphql/socialVolumeAndPriceChange_sevenDays.graphql', 'allProjects')
        else:
            return self.execute_query_by_path('./graphql/socialVolumeAndPriceChange_thirtyDays.graphql', 'allProjects')

    def get_social_dominance(self, timespan='day'):
        if timespan == 'day':
            return self.execute_query_by_path('./graphql/socialDominance.graphql', 'allProjects')
        elif timespan == 'week':
            return self.execute_query_by_path('./graphql/socialDominance_sevenDays.graphql', 'allProjects')
        else:
            return self.execute_query_by_path('./graphql/socialDominance_thirtyDays.graphql', 'allProjects')