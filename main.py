# pip install "fastapi[standard]" --> Comes with optional dependencies installed
from fastapi import FastAPI #Python class that provides all the functionality for the API
from recommendations import router as recommendations_router
from portfolio import router as portfolio_router

app = FastAPI() #app variable will be an "instance" of the class FastAPI

# Include the recommendations router
app.include_router(recommendations_router)
# Include the portfolio router
app.include_router(portfolio_router)

#Other types of actions (Listed below in case need to use)
#@app.post()
#@app.put()
#@app.delete()
@app.get("/")
def root(): #Put async in front of def if await is needed
    return {"message": "We are in main"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host = "127.0.0.1", port = 8000)