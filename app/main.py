from fastapi import FastAPI
from app.routers import public, balance, order, admin
import uvicorn
app = FastAPI()

app.include_router(public.router)
app.include_router(balance.router)
app.include_router(order.router)
app.include_router(admin.router)


@app.get("/")
def root():
    return {"message": "it works!"}

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)