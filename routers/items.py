from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/items")

fake_items_db = {
    "tomato": {"name": "tomato", "coler": "red"},
    "banana": {"name": "banana", "color": "yellow"}
}

@router.get("/")
def get_item_list():
    return list(fake_items_db.values())

@router.get("/{name}")
def get_item(name: str):
    if name not in fake_items_db:
        raise HTTPException(status_code=404, detail=f"{name} is not found")
    return fake_items_db[name]

