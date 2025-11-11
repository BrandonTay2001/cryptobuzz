class SocialScoreFormatter:
    def format_social_score_data(self, data_list):
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
                        'social_scores': []
                    }
                cache[item['ticker']]['social_scores'].append(item['socialScore'])
        
        # Calculate average socialScore and absoluteSocialScore for each ticker
        formatted_data = []
        for ticker, info in cache.items():
            scores = info['social_scores']
            avg_social_scores = sum(scores) / len(scores)
            abs_social_score = sum([abs(score) for score in scores]) / len(scores)
            formatted_data.append({
                'ticker': info['ticker'],
                'name': info['name'],
                'logoUrl': info['logoUrl'],
                'coinmarketcapLink': info['coinmarketcapLink'],
                'socialScore': avg_social_scores,
                'absoluteSocialScore': abs_social_score
            })

        formatted_data.sort(key=lambda x: x['absoluteSocialScore'], reverse=True)
        formatted_data = formatted_data[:100]
        total_absolute_sentiment = sum([item['absoluteSocialScore'] for item in formatted_data])

        return (formatted_data, len(formatted_data), total_absolute_sentiment)