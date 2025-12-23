from fastapi import FastAPI
from app.routes import health

app = FastAPI(title="FastAPI Fundamentals")

app.include_router(health.router)
