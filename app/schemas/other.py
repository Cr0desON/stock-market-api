from datetime import datetime

from pydantic import BaseModel, UUID4, Field

class InstrumentSchema(BaseModel):
    name: str
    ticker: str = Field(pattern=r"^[A-Z]{2,10}$")

class TransactionSchema(BaseModel):
    ticker: str
    amount: int
    price: int
    timestamp: datetime

class AdminBalanceActionBody(BaseModel):
    user_id: UUID4 = Field(examples=['#0="35b0884d-9a1d-47b0-91c7-eecf0ca56bc8"'])
    ticker: str = Field(examples=['#0"MEMCOIN"'])
    amount: int = Field(gt=0)

class CreateOrderResponse(BaseModel):
    success: bool = Field(default=True)
    order_id: UUID4