from uuid import UUID

from fastapi import APIRouter

from app.schemas.other import AdminBalanceActionBody, InstrumentSchema
from app.schemas.user import UserSchema

router = APIRouter(
    prefix="/api/v1/admin",
    tags=["admin"],
)

@router.delete(
    "/user/{user_id}",
    tags=["user"],
    summary="Delete User",
)
async def delete_user(user_id: UUID, authorization: str) -> UserSchema:
    ...

@router.post(
    "/instrument",
    summary="Add Instrument",
)
async def add_instrument(authorization: str) -> InstrumentSchema:
    ...

@router.delete(
    "/instrument/{ticker}",
    description="Удаление инструмента",
)
async def delete_instrument(ticker: str, authorization: str):
    ...

@router.post(
    "/balance/deposit",
    summary="Deposit",
    tags=["balance"],
    description="Пополнение баланса",
)
async def balance_deposit(authorization: str) -> AdminBalanceActionBody:
    ...

@router.post(
    "/balance/withdraw",
    summary="Withdraw",
    tags=["balance"],
    description="Вывод доступных средств с баланса",
)
async def balance_withdraw(authorization: str) -> AdminBalanceActionBody:
    ...