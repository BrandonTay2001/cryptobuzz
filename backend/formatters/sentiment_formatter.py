class SentimentFormatter:
    def __init__(self):
        pass

    def format_sentiment_data(self, data_list, num_days):
        if num_days == 1:
            data_list = [data_list[0]]    # use the latest data only for 1 day
        
        cache = {}
        for data in data_list:
            for item in data:
                if item['ticker'] not in cache:
                    coinmarketcap_id = item.get('coinmarketcapId')
                    coinmarketcap_link = (
                        f'https://coinmarketcap.com/currencies/{coinmarketcap_id}/'
                        if coinmarketcap_id else None
                    )
                    
                    cache[item['ticker']] = {
                        'ticker': item['ticker'],
                        'name': item['name'],
                        'logoUrl': item['logoUrl'],
                        'coinmarketcapLink': coinmarketcap_link,
                        'sentiment_scores': []
                    }
                cache[item['ticker']]['sentiment_scores'].append(item['sentimentWeighted'])
        
        # Calculate average sentimentWeighted and absoluteSentiment for each ticker
        formatted_data = []
        for ticker, info in cache.items():
            scores = info['sentiment_scores']
            avg_sentiment_weighted = sum(scores) / len(scores)
            abs_sentiment = sum([abs(score) for score in scores]) / len(scores)
            formatted_data.append({
                'ticker': info['ticker'],
                'name': info['name'],
                'logoUrl': info['logoUrl'],
                'coinmarketcapLink': info['coinmarketcapLink'],
                'sentiment': avg_sentiment_weighted,
                'absoluteSentiment': abs_sentiment
            })

        formatted_data.sort(key=lambda x: x['absoluteSentiment'], reverse=True)
        formatted_data = formatted_data[:100]
        total_absolute_sentiment = sum([item['absoluteSentiment'] for item in formatted_data])

        return (formatted_data, len(formatted_data), total_absolute_sentiment)