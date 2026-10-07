from fastapi import APIRouter

router = APIRouter(
    prefix="/api/v1/order",
    tags=["order"],
)

@router.post(
    "/",
    summary="Create Order",
)
async def create_order():
    ...

@router.get(
    "/",
    summary="List Order",
)
async def list_order():
    ...

@router.get(
    '/{order_id}',
    summary="Get Order",
)
async def get_order(order_id: int):
    ...

@router.delete(
    '/{order_id}',
    summary="Cancel Order",
)
async def cancel_order(order_id: int):
    ...