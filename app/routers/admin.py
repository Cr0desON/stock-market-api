from fastapi import APIRouter
from app.schemas.user import UserSchema

router = APIRouter(
    prefix="/admin",
    tags=["admin"],
)

# Дейтисвия с пользователями (список пользовтелей, удаление пользователя)
@router.get(
    "/users",
    tags=["admin"],
)
async def get_users(user: UserSchema) -> list[UserSchema]:
    ...

@router.post(
    "/delete-user"
)
async def delete():
    ...

# Действия с балансом (список балансов, пополнение баланаса, списание с баланса)
@router.get(
    "/balances",
    tags=["balance"],
)
async def get_balances():
    ...

@router.post(
    "/deposit",
    tags=["balance"],
)
async def deposit():
    ...

@router.post(
    "/withdraw",
    tags=["balance"],
)
async def withdraw():
    ...