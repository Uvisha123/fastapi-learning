from fastapi import APIRouter
from app.schemas.item import ItemCreate,ItemOut

router = APIRouter()

fake_db = []

@router.get("/items/{item_id}")
def get_item(item_id: int):
    return {
        "item_id": item_id,
        "message": "Item fetched successfully"
    }

@router.get("/items")
def get_items(skip: int = 0, limit: int = 10):
    return {
        "skip": skip,
        "limit": limit,
        "items": []
    }

@router.post("/items", response_model=ItemOut)
def create_item(item: ItemCreate):
    new_item = {"id": len(fake_db)+1, **item.dict()}
    fake_db.append(new_item)
    return new_item    

@router.put("/items/{item_id}")
def update_item(item_id: int, item: ItemCreate):
    return {
        "item_id": item_id,
        "updated_item": item
    }
    
@router.delete("/items/{item_id}")
def delete_item(item_id: int):
    return {
        "item_id": item_id,
        "status": "deleted"
    }
    
