from fastapi import APIRouter, HTTPException
from news.services import NewsService

router = APIRouter()

# Route to fetch and store news from MarketAux API to Supabase
@router.get("/fetch-news")
def fetch_news():
    try:
        NewsService.fetch_and_store_news()
        return {"status": "success", "message": "News fetched and stored successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching news: {str(e)}")

# Route to get the news stored in Supabase
@router.get("/")
def get_news():
    try:
        news = NewsService.get_news()
        return {"status": "success", "data": news}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving news: {str(e)}")
