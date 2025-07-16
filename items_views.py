from typing import Annotated

from fastapi import Path,APIRouter

router = APIRouter(prefix = "/items")

@router.get("/")
def list_items():
    return[
        "item1",
        "item1"]

@router.get("/latest/")
def get_latest():
    return {
        "item1": {
            "id": 1,
            "name": "latest",
        },
    }


@router.get("/{item_id}/")
def get_item(item_id: Annotated[int, Path(ge=1 ,lt = 1_000_000)]):
    return {
        "item":{
            "id" : item_id,
        },
    }