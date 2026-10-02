from fastapi import APIRouter
from app.schemas.request import RequestSchema
from app.schemas.user import UserSchema

router = APIRouter(
    prefix="/requests",
    tags=["requests"],
)

@router.post('/create')
async def create_user(request: RequestSchema):
    ...

@router.post('/cancel')
async def cancel_request():
    ...

@router.get('/status')
async def request_status(request: RequestSchema):
    ...

@router.get('/active')
async def active_requests(request: RequestSchema):
    ...

@router.get('/depth')
async def get_depth():
    ...