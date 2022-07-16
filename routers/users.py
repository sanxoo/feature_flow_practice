from fastapi import APIRouter

router = APIRouter(prefix="/users")

@router.get("/")
def get_user_list():
    return [
        {"id": "sanxoo"},
        {"id": "emma"}
    ]

@router.get("/{user_id}")
def get_user(user_id: str):
    return {"id": user_id}

