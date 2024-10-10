import requests
from supabase import create_client, Client
from core.config import settings

# Initialize Supabase client
supabase: Client = create_client(settings.SUPABASE_URL, settings.SUPABASE_KEY)

class NewsService:
    @staticmethod
    def fetch_and_store_news():
        url = "https://api.marketaux.com/v1/news/all"
        params = {
            "api_token": settings.MARKETAUX_API_KEY,  # Use from .env
            "language": "en",
            "limit": 10
        }

        try:
            # Fetch news from the MarketAux API
            response = requests.get(url, params=params)
            response.raise_for_status()  # Raise error for bad status codes
            news_data = response.json()

            for article in news_data.get("data", []):
                # Handle source field, check if it's a string or a dictionary
                source = article.get("source", "Unknown Source")
                if isinstance(source, dict):
                    source_name = source.get("name", "Unknown Source")
                else:
                    source_name = source

                # Insert article into the 'news_articles' table in Supabase
                supabase.table('news_articles').insert({
                    "title": article.get("title", "No Title"),
                    "content": article.get("description", "No Content"),
                    "source": source_name,
                    "published_at": article.get("published_at", "1970-01-01T00:00:00Z"),
                    "category": "general"  # Default category for now
                }).execute()

        except requests.RequestException as e:
            print(f"Error fetching news: {e}")
        except Exception as e:
            print(f"Error inserting into Supabase: {e}")

    @staticmethod
    def get_news():
        try:
            # Fetch news from Supabase
            response = supabase.table('news_articles').select("*").execute()
            return response.data
        except Exception as e:
            print(f"Error fetching news from Supabase: {e}")
            return None
