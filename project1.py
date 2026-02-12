import requests
from datetime import datetime
import time

class NewsApp:
    def __init__(self):
        # Using GNews API - Better free tier with India support
        self.gnews_base = "https://gnews.io/api/v4"
        self.gnews_key = "015246f5c7460935aa7e4cf78f929af4"  # Get from https://gnews.io/
        
    def get_gnews_headlines(self, country='in', category=None, query=None):
        """Get news from GNews API - supports India well"""
        if query:
            endpoint = f"{self.gnews_base}/search"
            params = {
                'token': self.gnews_key,
                'q': query,
                'lang': 'en',
                'country': country,
                'max': 10
            }
        else:
            endpoint = f"{self.gnews_base}/top-headlines"
            params = {
                'token': self.gnews_key,
                'country': country,
                'lang': 'en',
                'max': 10
            }
            if category:
                params['topic'] = category
        
        try:
            response = requests.get(endpoint, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching news: {e}")
            return None
    
    def display_gnews_articles(self, news_data):
        """Display GNews articles"""
        if not news_data or not news_data.get('articles'):
            print("No news articles found.")
            return
        
        articles = news_data.get('articles', [])
        print("\n" + "="*80)
        print(f"Found {len(articles)} articles:")
        print("="*80 + "\n")
        
        for i, article in enumerate(articles, 1):
            title = article.get('title', 'No title')
            source = article.get('source', {}).get('name', 'Unknown')
            published = article.get('publishedAt', '')
            description = article.get('description', 'No description')
            url = article.get('url', '')
            
            if published:
                try:
                    dt = datetime.fromisoformat(published.replace('Z', '+00:00'))
                    published = dt.strftime('%B %d, %Y at %I:%M %p')
                except:
                    pass
            
            print(f"{i}. {title}")
            print(f"   Source: {source}")
            print(f"   Published: {published}")
            print(f"   {description}")
            print(f"   Read more: {url}")
            print("-" * 80 + "\n")


def main():
    print("\n" + "="*80)
    print("🌍 LIVE NEWS APPLICATION - INDIA & WORLD 🌍")
    print("="*80)
    print("\n✅ API Key loaded successfully!")
    print("="*80)
    print("\nPress Enter to continue...")
    input()
    
    news_app = NewsApp()
    
    while True:
        print("\n" + "="*80)
        print("🌍 LIVE NEWS APPLICATION 🌍")
        print("="*80)
        print("\n1. Top Headlines - India 🇮🇳")
        print("2. Top Headlines - World 🌎")
        print("3. News by Category (India)")
        print("4. Search News (India)")
        print("5. Search Global News")
        print("6. Exit")
        print("\nChoose an option (1-6): ", end='')
        
        choice = input().strip()
        
        if choice == '1':
            print("\nFetching top headlines from India...\n")
            news_data = news_app.get_gnews_headlines(country='in')
            news_app.display_gnews_articles(news_data)
        
        elif choice == '2':
            print("\nAvailable countries: us, gb, ca, au, in, de, fr, jp, cn, br, ru, za")
            print("Enter country code (or press Enter for US): ", end='')
            country = input().strip().lower() or 'us'
            print(f"\nFetching top headlines from {country.upper()}...\n")
            news_data = news_app.get_gnews_headlines(country=country)
            news_app.display_gnews_articles(news_data)
        
        elif choice == '3':
            print("\nCategories: general, business, entertainment, health, science, sports, technology")
            print("Enter category: ", end='')
            category = input().strip().lower()
            print(f"\nFetching {category} news from India...\n")
            news_data = news_app.get_gnews_headlines(country='in', category=category)
            news_app.display_gnews_articles(news_data)
        
        elif choice == '4':
            print("\nEnter search keyword (e.g., 'cricket', 'bollywood', 'tech'): ", end='')
            query = input().strip()
            print(f"\nSearching Indian news for '{query}'...\n")
            news_data = news_app.get_gnews_headlines(country='in', query=query)
            news_app.display_gnews_articles(news_data)
        
        elif choice == '5':
            print("\nEnter search keyword: ", end='')
            query = input().strip()
            print("\nEnter country code (or press Enter for global): ", end='')
            country = input().strip().lower() or 'us'
            print(f"\nSearching news for '{query}'...\n")
            news_data = news_app.get_gnews_headlines(country=country, query=query)
            news_app.display_gnews_articles(news_data)
        
        elif choice == '6':
            print("\n👋 Thanks for using the News App! Goodbye!")
            break
        
        else:
            print("\n❌ Invalid choice. Please select 1-6.")
        
        time.sleep(1)


if __name__ == "__main__":
    main()