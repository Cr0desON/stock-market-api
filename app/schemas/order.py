from enum import StrEnum
from datetime import datetime

from pydantic import BaseModel, UUID4, Field

class Status(StrEnum):
    new = "NEW"
    executed = "EXECUTED"
    partially_executed = "PARTIALLY_EXECUTED"
    CANCELLED = "CANCELLED"

class Direction(StrEnum):
    buy = "BUY"
    sell = "SELL"


class MarketOrderBody(BaseModel):
    direction: Direction
    ticker: str
    qty: int = Field(qe=1)

class MarketOrder(BaseModel):
    id: UUID4
    status: Status
    user_id: UUID4
    timestamp: datetime
    body: MarketOrderBody

class LimitOrder(MarketOrder):
    filled: int = Field(default=0)

class LimitOrderBody(MarketOrderBody):
    price: int = Field(gt=0)

class Level(BaseModel):
    price: int
    qty: int

class OrderBook(BaseModel):
    bid_levels: list[Level]
    ask_levels: list[Level]