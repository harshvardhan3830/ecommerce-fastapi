from typing import Union
from fastapi import FastAPI

from .routes import user

app = FastAPI()

app.include_router(user.router, prefix="/users", tags=["Users"])


@app.get("/")
async def root():
    return {"message": "Welcome to ecommerce API !"}
