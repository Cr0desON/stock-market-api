from fastapi import APIRouter

from app.schemas.other import CreateOrderResponse
from app.schemas.order import LimitOrderBody, MarketOrder, LimitOrder

router = APIRouter(
    prefix="/api/v1/order",
    tags=["order"],
)

@router.post(
    "/",
    summary="Create Order",
)
async def create_order(authorization: str, order: LimitOrderBody) -> CreateOrderResponse:
    ...

@router.get(
    "/",
    summary="List Order",
)
async def list_order(authorization: str) -> list[LimitOrder]:
    ...

@router.get(
    '/{order_id}',
    summary="Get Order",
)
async def get_order(order_id: int, authorization: str) -> MarketOrder:
    ...

@router.delete(
    '/{order_id}',
    summary="Cancel Order",
)
async def cancel_order(order_id: int, authorization: str):
    ...