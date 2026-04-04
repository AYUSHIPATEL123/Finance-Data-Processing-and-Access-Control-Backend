from fastapi import FastAPI
from routers import users,records

app = FastAPI()


app.include_router(users.router)
app.include_router(records.router)


@app.get('/')
async def home():
    return {"message":"HOME PAGE"}

