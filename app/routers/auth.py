from fastapi import APIRouter
from app.schemas.user import UserSchema

router = APIRouter(
    prefix="/",
    tags=["auth"],
)

@router.post(
    "/login"
)
async def login(user: UserSchema):
    ...

@router.post(
    "/register"
)
async def register(user: UserSchema):
    ...

@router.post(
    "/logout"
)
async def logout():
    ...

