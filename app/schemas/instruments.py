from pydantic import BaseModel, Field, ConfigDict
import decimal, datetime

class InstrumentSchema(BaseModel):
    id: int
    name: str

    model_config = ConfigDict(extra='forbid')

class SharesSchema(InstrumentSchema):
    company: str
    price: decimal.Decimal = Field(ge=0.0)
    count : decimal.Decimal = Field(ge=0.0)

class BondSchema(InstrumentSchema):
    issuer : str
    value : decimal.Decimal = Field(ge=0.0)
    profit : decimal.Decimal | None
    payday : datetime.date| None

class MemecoinsSchema(InstrumentSchema):
    name : str = Field(min_length=1, max_length=100)
    price: decimal.Decimal = Field(ge=0.0)
    token_count : decimal.Decimal = Field(ge=0.0)
