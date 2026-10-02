from fastapi import APIRouter
from app.schemas.instruments import InstrumentSchema

router = APIRouter(
    prefix="/instruments",
    tags=["instruments"],
)

# Действия с инструментами (список инструментов, добалвение инструмента, удаление инструмента)
@router.get(
    "/"
)
async def get_instruments() -> list[InstrumentSchema]:
    ...

@router.post(
    "/add"
)
async def add_instrument(instrument : InstrumentSchema):
    ...

@router.post(
    "/delete"
)
async def delete_instrument():
    ...