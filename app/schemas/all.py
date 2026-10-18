from ast import List
from enum import StrEnum
from datetime import datetime

from pydantic import BaseModel, UUID4, Field

class InstrumentSchema(BaseModel):
    name: str
    ticker: str = Field(pattern=r"^[A-Z]{2,10}$")

class Status(StrEnum):
    new = "NEW"
    executed = "EXECUTED"
    partially_executed = "PARTIALLY_EXECUTED"
    CANCELLED = "CANCELLED"

class Direction(StrEnum):
    buy = "BUY"
    sell = "SELL"

class TransactionSchema(BaseModel):
    ticker: str
    amount: int
    price: int
    timestamp: datetime

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

class CreateOrderResponse(BaseModel):
    success: bool = Field(default=True)
    order_id: UUID4

class Level(BaseModel):
    price: int
    qty: int

class OrderBook(BaseModel):
    bid_levels: List[Level]
    ask_levels: List[Level]

class AdminBalanceActionBody(BaseModel):
    user_id: UUID4 = Field(examples=['#0="35b0884d-9a1d-47b0-91c7-eecf0ca56bc8"'])
    ticker: str = Field(examples=['#0"MEMCOIN"'])
    amount: int = Field(gt=0)