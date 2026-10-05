from fastapi import APIRouter

router = APIRouter(
    prefix="/api/v1/public",
    tags=["public"],
)

@router.post(
    "/register",
    summary="Register",
)
async def register_user():
    ...

@router.get(
    "/instrument",
    summary="List Instruments",
)
async def get_instruments():
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
async def get_transaction_history():
    ...