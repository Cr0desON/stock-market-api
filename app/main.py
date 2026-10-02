from fastapi import FastAPI
from app.routers import user, admin, auth
app = FastAPI()

app.include_router(user.router)
app.include_router(admin.router)
app.include_router(auth.router)

@app.get("/")
def root():
    return {"message": "it works!"}