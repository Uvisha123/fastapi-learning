from fastapi import FastAPI

app = FastAPI(title="FastAPI Fundamentals")

@app.get("/")
def root():
    return {"message": "FastAPI Fundamentals running"}

@app.get("/hello")
def say_hello():
    return {"message": "Hello FastAPI"}

@app.post("/items")
def create_item(item: dict):
    return {"item_created": item}

@app.put("/items/1")
def update_item():
    return {"status": "updated"}

