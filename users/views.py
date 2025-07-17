from fastapi import APIRouter
from .schemas import CreateUser
from users import crud

router = APIRouter(prefix="/users", tags=["users"])


@router.post("/")
def crete_user(user: CreateUser):
    return crud.create_user(user_in=user)
