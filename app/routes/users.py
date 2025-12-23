from fastapi import APIRouter

router = APIRouter()

@router.get("/users")
def get_users(active: bool = True):
    return {
        "active": active,
        "users": []
    }
