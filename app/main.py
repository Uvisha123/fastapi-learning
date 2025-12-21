from fastapi import FastAPI

app = FastAPI(title="FastAPI Fundamentals")

@app.get("/")
def root():
    return {"message": "FastAPI Fundamentals running"}
