from fastapi import FastAPI
from app.auth import routes as auth_routes  # Import auth routes
from app.user_profile import routes as user_profile_routes  # Import user_profile routes
from app.common.database import database

app = FastAPI()

# Include routers
app.include_router(auth_routes.router, prefix="/api/auth", tags=["auth"])
app.include_router(user_profile_routes.router, prefix="/api/user_profile", tags=["user_profile"])
app.include_router(chat_routes.router, prefix="/api/chat", tags=["chat"])

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
