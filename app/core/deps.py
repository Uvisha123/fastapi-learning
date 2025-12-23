from app.db.session import FakeDBSession

def get_app_name():
    return "FastAPI Fundamentals"

def get_request_source():
    return "api"

def get_db():
    db = FakeDBSession()
    try:
        yield db
    finally:
        db.close()

def get_current_user():
    return {
        "username": "test_user",
        "role": "user"
    }
        