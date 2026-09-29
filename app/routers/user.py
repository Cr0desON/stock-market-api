from fastapi import APIRouter

router = APIRouter(
    prefix="/user",
    tags=["user"],
)

@router.get(
    "/balance"
)
async def get_balance():
    ...

@router.get(
    "/history"
)
async def get_history():
    ...