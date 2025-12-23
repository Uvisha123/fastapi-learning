from fastapi import FastAPI
from app.routes import health,items,users

app = FastAPI(title="FastAPI Fundamentals")

app.include_router(health.router)

app.include_router(items.router)

app.include_router(users.router)
