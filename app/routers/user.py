from fastapi import APIRouter
from app.schemas.user import UserSchema

router = APIRouter(
    prefix="/user",
    tags=["user"],
)

@router.get(
    "/balance"
)
async def get_balance(user: UserSchema):
    ...

@router.get(
    "/history"
)
async def get_history(user: UserSchema):
    ...