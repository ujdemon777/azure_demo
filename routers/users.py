from fastapi import APIRouter,HTTPException
from pymongo import MongoClient
import os
from bson import ObjectId

users = APIRouter()

MONGODB_URI = os.getenv("MONGODB_URI")
client = MongoClient(MONGODB_URI)
db = client['lead_compass']
users_collection = db['user']



@users.get("/{user_id}")
async def read_user(user_id: str):
    user = users_collection.find_one({"_id": ObjectId(user_id)})
    print(user)
    if user:
        return {"user": user.get('name')}
    raise HTTPException(status_code=404, detail="User not found")
