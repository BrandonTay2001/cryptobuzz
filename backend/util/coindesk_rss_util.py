import feedparser
from openai import OpenAI
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta
import time

load_dotenv()

class CoindeskRSSUtil:
    def __init__(self):
        self.rss_url = "https://www.coindesk.com/arc/outboundfeeds/rss"
        self.openai_client = OpenAI(base_url="https://api.deepseek.com/v1", api_key=os.getenv('DEEPSEEK_API_KEY'))
        self.model = "deepseek-chat"
        
    def parse_rss_feed(self):
        """Parse the RSS feed and extract article details"""
        feed = feedparser.parse(self.rss_url)
        articles = []
        
        for entry in feed.entries:
            # Check for categories to filter out Opinion and week ahead articles
            if hasattr(entry, 'tags'):
                categories = []
                for tag in entry.tags:
                    if hasattr(tag, 'term'):
                        categories.append(tag.term.lower().strip())
                
                # Skip articles with 'opinion' or 'week ahead' categories
                if 'opinion' in categories or 'week ahead' in categories:
                    continue
            
            article = {
                'title': entry.title,
                'link': entry.link,
                'published': entry.published,
                'summary': getattr(entry, 'summary', ''),
                'published_parsed': entry.published_parsed
            }
            articles.append(article)
        
        return articles
    
    def filter_recent_articles(self, articles):
        """Filter articles from the past 24 hours"""
        recent_articles = []
        now = datetime.now()
        
        for article in articles:
            if article['published_parsed']:
                # Convert published_parsed tuple to datetime
                published_time = datetime(*article['published_parsed'][:6])
                
                # Check if article is within the last 24 hours
                if now - published_time <= timedelta(days=1):
                    recent_articles.append(article)
        
        return recent_articles
    
    def rank_articles_with_openai(self, articles):
        """Rank articles using OpenAI based on importance"""
        ranked_articles = []
        
        for article in articles:
            try:
                prompt = f"""Rank the importance of the following cryptocurrency news article on a scale of 1-10, where 10 is the most important:

Title: {article['title']}
Summary: {article['summary']}

Consider factors like:
- Market impact potential
- Regulatory significance
- Technology breakthroughs
- Major partnerships or acquisitions
- Security incidents
- Market volatility implications

Any article that is not about cryptocurrency should be ranked as 0. Any article that invokes a question, provides a prediction or an opinion should also be ranked as 0.
Any article that does not purely provide facts should be ranked as 0.

Provide only a single number between 1-10 as your response."""

                response = self.openai_client.chat.completions.create(
                    model=self.model,
                    messages=[{"role": "user", "content": prompt}],
                    max_tokens=10,
                    temperature=0.1
                )
                
                score_text = response.choices[0].message.content.strip()
                # Extract number from response
                score = int(''.join(filter(str.isdigit, score_text)))
                article['importance_score'] = score
                ranked_articles.append(article)
                
                # Small delay to avoid rate limiting
                time.sleep(0.5)
                
            except Exception as e:
                print(f"Error ranking article '{article['title']}': {e}")
                # Default score if ranking fails
                article['importance_score'] = 5
                ranked_articles.append(article)
        
        # Sort by importance score in descending order
        return sorted(ranked_articles, key=lambda x: x['importance_score'], reverse=True)
    
    def paraphrase_headlines_with_openai(self, articles):
        """Paraphrase headlines using OpenAI"""
        paraphrased_articles = []
        
        for article in articles:
            try:
                prompt = f"""Paraphrase the following cryptocurrency news headline to make it more engaging and clear while maintaining the same meaning:

Original headline: {article['title']}

Provide a paraphrased version that provides all the necessary information in the original headline as a short sentence.

Provide only the paraphrased headline, nothing else. Limit the paraphrased headline to 7 words or less."""

                response = self.openai_client.chat.completions.create(
                    model=self.model,
                    messages=[{"role": "user", "content": prompt}],
                    max_tokens=100,
                    temperature=0.7
                )
                
                paraphrased_title = response.choices[0].message.content.strip()
                article['paraphrased_title'] = paraphrased_title
                paraphrased_articles.append(article)
                
                # Small delay to avoid rate limiting
                time.sleep(0.5)
                
            except Exception as e:
                print(f"Error paraphrasing headline '{article['title']}': {e}")
                # Use original title if paraphrasing fails
                article['paraphrased_title'] = article['title']
                paraphrased_articles.append(article)
        
        return paraphrased_articles
    
    def get_top_news_articles(self, limit=10):
        """Main method to get top news articles with paraphrased headlines"""
        try:
            # Parse RSS feed
            articles = self.parse_rss_feed()
            print(f"Found {len(articles)} total articles")
            
            # Filter for recent articles (past 24 hours)
            recent_articles = self.filter_recent_articles(articles)
            print(f"Found {len(recent_articles)} articles from past 24 hours")
            
            if not recent_articles:
                return []
            
            # Rank articles by importance
            ranked_articles = self.rank_articles_with_openai(recent_articles)
            
            # Get top articles
            top_articles = ranked_articles[:limit]
            
            # Paraphrase headlines
            final_articles = self.paraphrase_headlines_with_openai(top_articles)
            
            return final_articles
            
        except Exception as e:
            print(f"Error in get_top_news_articles: {e}")
            return []

test = CoindeskRSSUtil()
articles = test.get_top_news_articles()
for article in articles:
    print(f"Original: {article['title']}")
    print(f"Paraphrased: {article['paraphrased_title']}")
    print(f"Score: {article['importance_score']}")
    print(f"Link: {article['link']}")
    print("---")