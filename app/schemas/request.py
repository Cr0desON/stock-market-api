from pydantic import BaseModel, Field, ConfigDict
import decimal

class RequestSchema(BaseModel):
    userid: str
    item: str
    status: str = Field(default="created")

    model_config = ConfigDict(extra='forbid')
