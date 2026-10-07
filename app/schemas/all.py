from pydantic import BaseModel, UUID4, Field
import datetime

# Схема транзакций
class TransactionSchema(BaseModel):
    ticker: str
    amount: int
    price: int
    timestamp: datetime.datetime

# Схема инструментов
class InstrumentSchema(BaseModel):
    name: str
    ticker: str = Field(pattern=r"^[A-Z]{2,10}$")