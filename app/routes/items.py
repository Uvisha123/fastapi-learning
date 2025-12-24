from fastapi import APIRouter,Depends,HTTPException
from app.schemas.item import ItemCreate,ItemOut
from app.core.deps import get_request_source,get_db,get_current_user
import asyncio

router = APIRouter()

fake_db = []

@router.get("/item/{item_id}")
def get_item(item_id: int):
    return {
        "item_id": item_id,
        "message": "Item fetched successfully"
    }

@router.get("/items/{item_id}", response_model=ItemOut)
async def get_item(item_id: int):
    await asyncio.sleep(0.05)
    for i in fake_db:
        if i["id"] == item_id:
            return i
    raise HTTPException(status_code=404, detail=f"Item with id {item_id} not found")

    

@router.get("/item/source")
def get_items_source(source: str = Depends(get_request_source)):
    return {
        "source": source
    }   

@router.get("/items-async", response_model=list[ItemOut])
async def get_items_async():
    await asyncio.sleep(0.5) 
    return fake_db     

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
    
@router.get("/items1/db-test")
def db_test(db = Depends(get_db)):
    return {
        "db_connected": db.connected
    }

@router.get("/items2/protected")
def protected_items(current_user = Depends(get_current_user)):
    return {
        "message": "This is a protected route",
        "user": current_user
    }    