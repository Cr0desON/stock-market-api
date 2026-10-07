from fastapi import APIRouter
from app.schemas.all import TransactionSchema, InstrumentSchema
from app.schemas.user import UserSchema

router = APIRouter(
    prefix="/api/v1/public",
    tags=["public"],
)

@router.post(
    "/register",
    summary="Register",
)
async def register_user(user: UserSchema) -> list[UserSchema]:
    ...

@router.get(
    "/instrument",
    summary="List Instruments",
)
async def get_instruments(instrument: InstrumentSchema) -> list[InstrumentSchema]:
    ...

@router.get(
    "/orderbook/{ticker}",
    summary="Get Orderbook",
)
async def get_orderbook():
    ...

@router.get(
    "/transaction/{ticker}",
    summary="Get Transaction History",
)
async def get_transaction_history(transaction: TransactionSchema) -> list[TransactionSchema]:
    ...