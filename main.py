from fastapi import FastAPI
from app.auth import routes as auth_routes
from app.user_profile import routes as user_profile_routes
from app.chat import routes as chat_routes
from app.recommendation import routes as recommendation_routes
from app.stocks import routes as stock_routes
from app.portfolios import routes as portfolio_routes
from app.transactions import routes as transaction_routes
from app.nfts import routes as nft_routes
from app.rewards import routes as reward_routes
from app.news_articles import routes as news_article_routes
from app.common.database import database

app = FastAPI()

# Include routers
app.include_router(auth_routes.router, prefix="/api/auth", tags=["auth"])
app.include_router(user_profile_routes.router, prefix="/api/user_profile", tags=["user_profile"])
app.include_router(chat_routes.router, prefix="/api/chat", tags=["chat"])
app.include_router(recommendation_routes.router, prefix="/api/recommendation", tags=["recommendation"])
app.include_router(stock_routes.router, prefix="/api/stock", tags=["stock"])
app.include_router(portfolio_routes.router, prefix="/api/portfolio", tags=["portfolio"])
app.include_router(transaction_routes.router, prefix="/api/transaction", tags=["transaction"])
app.include_router(nft_routes.router, prefix="/api/nft", tags=["nft"])
app.include_router(reward_routes.router, prefix="/api/reward", tags=["reward"])
app.include_router(news_article_routes.router, prefix="/api/news_article", tags=["news_article"])


@app.get("/")
def read_root():
    return {"message": "Welcome to the Investment App API"}

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
