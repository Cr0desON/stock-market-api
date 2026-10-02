from pydantic import BaseModel, Field, EmailStr, ConfigDict
import decimal

class UserSchema(BaseModel):
    username: str
    email: EmailStr
    password: str = Field(min_length=8)

    model_config = ConfigDict(extra='forbid')

class BalanceSchema(BaseModel):
    userid: int
    currency: int = Field(default='RUB')
    balance: decimal = Field(ge=0, default=0.0)