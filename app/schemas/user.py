from enum import Enum
from pydantic import BaseModel, UUID4, Field

class UserRole(str, Enum):
    user = "USER"
    admin = "ADMIN"

class UserSchema(BaseModel):
    id: UUID4
    name: str
    role: UserRole
    api_key: str

class NewUserSchema(BaseModel):
    name: str = Field(min_length=3)
