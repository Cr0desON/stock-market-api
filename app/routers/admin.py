from fastapi import APIRouter

router = APIRouter(
    prefix="/admin",
    tags=["admin"],
)

# Дейтисвия с пользователями (список пользовтелей, удаление пользователя)
@router.get(
    "/users",
    tags=["admin"],
)
async def get_users():
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

# Действия с инструментами (список инструментов, добалвение инструмента, удаление инструмента)
@router.get(
    "/instruments",
    tags=["instruments"],
)
async def get_instruments():
    ...

@router.post(
    "/add-instrument",
    tags=["instruments"],
)
async def add_instrument():
    ...

@router.post(
    "/delete-instrument",
    tags=["instruments"],
)
async def delete_instrument():
    ...