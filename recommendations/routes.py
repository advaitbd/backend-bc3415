from fastapi import APIRouter, HTTPException
# from news.services import NewsService --> If service is needed

router = APIRouter()

@router.get("/")
def main():
    return {"message": "We are in recommendations home"}

@router.get("/fetch-recommendations")
def fetch_recommendations():
    return {"message": "We are in fetch-recommendations"}