from fastapi import FastAPI

app = FastAPI(title="FastAPI Fundamentals")

@app.get("/")
def root():
    return {"message": "FastAPI Fundamentals running"}

@app.get("/hello")
def say_hello():
    return {"message": "Hello FastAPI"}

@app.get("/items/{item_id}")
def get_item(item_id: int):
    return {
        "item_id": item_id,
        "message": "Item fetched successfully"
    }

@app.post("/items")
def create_item(item: dict):
    return {"item_created": item}

@app.put("/items/{item_id}")
def update_item(item_id: int):
    return {
        "item_id": item_id,
        "status": "updated"
    }


@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    return {
        "item_id": item_id,
        "status": "deleted"
    }

@app.get("/items")
def get_items(limit: int = 10):
    return {
        "limit": limit,
        "items": []
    }

@app.get("/items")
def get_items(skip: int = 0, limit: int = 10):
    return {
        "skip": skip,
        "limit": limit,
        "items": []
    }

@app.get("/users")
def get_users(active: bool = True):
    return {
        "active": active,
        "users": []
    }


