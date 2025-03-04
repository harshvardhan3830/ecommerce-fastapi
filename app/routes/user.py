from fastapi import HTTPException, APIRouter

from ..schemas.user import CreateUserSchema, LoginSchema
from ..utils.auth import create_access_token, get_hashed_password, verify_password
from ..database import user_collection

router = APIRouter()


@router.post("/register")
async def register(user: CreateUserSchema):
    if await user_collection.find_one({"email": user.email}):
        raise HTTPException(status_code=400, detail="Email already exists")

    user.password = get_hashed_password(user.password)
    await user_collection.insert_one(user.model_dump())
    return {"message": "User registered Successfully"}


@router.post("/login")
async def login(data: LoginSchema):
    user = await user_collection.find_one({"username": data.username})
    if not user or not verify_password(data.password, user["password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    # Convert ObjectId to string
    user["_id"] = str(user["_id"])

    token = create_access_token({"sub": user["username"]})
    user.pop("password", None)  # Remove password before returning user data
    user["access_token"] = token
    return user
