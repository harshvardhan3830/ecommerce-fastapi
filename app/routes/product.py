from fastapi import APIRouter
from ..database import product_collection
from ..schemas.product import CreateProductSchema
from ..utils.db_helpers import product_helper

router = APIRouter()


@router.post("/product-register")
async def create_product(product: CreateProductSchema):
    result = await product_collection.insert_one(product.dict())
    return {"id": str(result.inserted_id)}


@router.get("/get-products")
async def get_products():
    products = await product_collection.find().to_list(100)
    return [product_helper(product) for product in products]
