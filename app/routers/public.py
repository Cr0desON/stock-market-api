from fastapi import APIRouter

from app.schemas.other import TransactionSchema, InstrumentSchema
from app.schemas.user import UserSchema, NewUserSchema
from app.schemas.order import OrderBook

router = APIRouter(
    prefix="/api/v1/public",
    tags=["public"],
)

@router.post(
    "/register",
    summary="Register",
)
async def register_user(newUser: NewUserSchema) -> list[UserSchema]:
    ...

@router.get(
    "/instrument",
    summary="List Instruments",
    description="Список доступных инструментов",
)
async def get_instruments() -> list[InstrumentSchema]:
    ...

@router.get(
    "/orderbook/{ticker}",
    summary="Get Orderbook",
    description="Текущие заявки",
)
async def get_orderbook(ticker: str, limit: int) -> list[OrderBook]:
    ...

@router.get(
    "/transaction/{ticker}",
    summary="Get Transaction History",
    description="История сделок",
)
async def get_transaction_history(ticker: str, limit: int) -> list[TransactionSchema]:
    ...