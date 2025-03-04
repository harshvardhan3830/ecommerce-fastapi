from typing import Union
from fastapi import FastAPI

from .routes import user, product

app = FastAPI()

app.include_router(user.router, prefix="/users", tags=["Users"])
app.include_router(product.router, prefix="/products", tags=["Products"])


@app.get("/")
async def root():
    return {"message": "Welcome to ecommerce API !"}
