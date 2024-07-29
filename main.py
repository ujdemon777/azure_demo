from fastapi import FastAPI, HTTPException
from routers import items, users


app = FastAPI()

app.include_router(items, prefix="/api/v1/items", tags=["items"])
app.include_router(users, prefix="/api/v1/users", tags=["users"])


@app.get("/")
async def read_root():
    return {"message": "Welcome to the API"}



