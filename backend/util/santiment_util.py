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

# test = SantimentUtil()
# print(test.execute_query_by_path('graphql/sentimentWeighted.graphql', 'allProjects'))