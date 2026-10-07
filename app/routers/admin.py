from fastapi import APIRouter

router = APIRouter(
    prefix="/api/v1/admin",
    tags=["admin"],
)

@router.delete(
    "/user/{user_id}",
    summary="Delete User",
)
async def delete_user():
    ...

@router.post(
    "/instrument",
    summary="Add Instrument",
)
async def add_instrument():
    ...

@router.delete(
    "/instrument/{ticker}",
)
async def delete_instrument():
    ...

@router.post(
    "/balance/deposit",
    summary="Deposit",
    tags=["balance"],
)
async def balance_deposit():
    ...

@router.post(
    "/balance/withdraw",
    summary="Withdraw",
    tags=["balance"],
)
async def balance_withdraw():
    ...

@router.delete(
    "/user/{user_id}",
    summary="Delete User",
    tags=["user"],
)
async def delete_user():
    ...
