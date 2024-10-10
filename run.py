from fastapi import FastAPI
from rewards import router as rewards_router
from news import router as news_router

app = FastAPI()

# Include the rewards router
app.include_router(rewards_router)
# Include the news router
app.include_router(news_router)

@app.get("/")
async def root():
    return {"message": "Welcome to the API!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)