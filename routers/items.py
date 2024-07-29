from fastapi import APIRouter

items = APIRouter()

@items.get("/demo")
async def read_item():
    return {"item_id": "testing item"}

@items.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id, "name": f"Item {item_id}"}
