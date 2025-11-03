class SocialDominanceFormatter:
    def format_single_social_dominance_data(self, data):
        formatted_data = []
        total_percentage = 0.0
        for item in data:
            formatted_data.append({
                'ticker': item['ticker'],
                'name': item['name'],
                'logoUrl': item['logoUrl'],
                'socialDominance': item['socialDominance']
            })
            total_percentage += item['socialDominance']
        
        # if the total_percentage is more than 100, normalize the values
        if total_percentage > 100:
            for item in formatted_data:
                item['socialDominance'] = (item['socialDominance'] / total_percentage) * 100
            total_percentage = 100.0

        formatted_data.sort(key=lambda x: x['socialDominance'], reverse=True)
        formatted_data = formatted_data[:100]
        return (formatted_data, len(formatted_data), total_percentage)