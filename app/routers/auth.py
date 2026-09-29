from fastapi import APIRouter

router = APIRouter(
    prefix="/",
    tags=["auth"],
)

@router.post(
    "/login"
)
async def login():
    ...

@router.post(
    "/register"
)
async def register():
    ...

@router.post(
    "/logout"
)
async def logout():
    ...

