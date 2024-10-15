from fastapi import FastAPI
from app.auth import routes as auth_routes  # Import auth routes

app = FastAPI()

# Include routers
app.include_router(auth_routes.router, prefix="/auth", tags=["auth"])

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
