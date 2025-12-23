from fastapi import APIRouter,Depends
from app.core.deps import get_app_name,get_request_source

router = APIRouter()

@router.get("/health")
def health_check():
    return {"status": "ok"}

@router.get("/hello")
def say_hello():
    return {"message": "Hello FastAPI"}

@router.get("/health1")
def health_check(app_name: str = Depends(get_app_name),source:str=Depends(get_request_source)):
    return {
        "status": "ok",
        "app": app_name,
        "source":source
        
    }