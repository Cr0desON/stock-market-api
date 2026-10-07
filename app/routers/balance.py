from fastapi import APIRouter

router = APIRouter(
    prefix="/api/v1",
    tags=["balance"],
)

@router.get(
    "/balance",
    summary="Get Balances"
)
async def get_balances():
    ...