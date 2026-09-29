from fastapi import FastAPI

app = FastAPI()

## ** Ручки всего auth для пользователя ** ##
@app.post(
    "/login",
    tags=["auth"],
)
async def login():
    ...

@app.post(
    "/register",
    tags=["auth"],
)
async def register():
    ...

@app.post(
    "/logout",
    tags=["auth"],
)
async def logout():
    ...

## ** Ручки информации о пользователе ** ##
@app.get(
    "/balance",
    tags=["user info"],
)
async def get_balance():
    ...

@app.get(
    "/history",
    tags=["user info"],
)
async def get_history():
    ...

## ** Ручки для администрирования ** ##

# Дейтисвия с пользователями (список пользовтелей, удаление пользователя)
@app.get(
    "/users",
    tags=["admin"],
)
async def get_users():
    ...

@app.post(
    "/delete-user",
    tags=["admin"],
)
async def delete():
    ...

# Действия с балансом (список балансов, пополнение баланаса, списание с баланса)
@app.get(
    "/balances",
    tags=["admin", "balance"],
)
async def get_balances():
    ...

@app.post(
    "/deposit",
    tags=["admin", "balance"],
)
async def deposit():
    ...

@app.post(
    "/withdraw",
    tags=["admin", "balance"],
)
async def withdraw():
    ...

# Действия с инструментами (список инструментов, добалвение инструмента, удаление инструмента)
@app.get(
    "/instruments",
    tags=["admin", "instruments"],
)
async def get_instruments():
    ...

@app.post(
    "/add-instrument",
    tags=["admin", "instruments"],
)
async def add_instrument():
    ...

@app.post(
    "/delete-instrument",
    tags=["admin", "instruments"],
)
async def delete_instrument():
    ...