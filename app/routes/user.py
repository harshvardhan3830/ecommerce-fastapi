from fastapi import HTTPException, APIRouter
from bson import ObjectId

from ..schemas.user import CreateUserSchema, LoginSchema
from ..utils.auth import create_access_token, get_hashed_password, verify_password
from ..database import user_collection
from ..utils.db_helpers import users_helper
from ..utils.response_helper import response_helper

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


@router.get("/get-users")
async def getUsers():
    users = await user_collection.find().to_list(50)
    return [users_helper(user) for user in users]


@router.get("/get-by-id/{id}")
async def getUser(id: str):
    try:
        # Validate ObjectId
        if not ObjectId.is_valid(id):
            return response_helper(
                status="failed", message="Invalid user ID format", data=None
            )

        user = await user_collection.find_one({"_id": ObjectId(id)})

        if user is None:
            return response_helper(status="failed", message="User not found", data=None)

        # Use users_helper to format user data
        return response_helper(
            status="success",
            message="User fetched successfully!",
            data=users_helper(user),
        )

    except Exception as e:
        return response_helper(status="failed", message=str(e), data=None)


# Update user api
@router.put("/update/{id}")
async def updateUser(id: str, user: CreateUserSchema):
    try:
        # Validate ObjectId
        if not ObjectId.is_valid(id):
            return response_helper(
                status="failed", message="Invalid user ID format", data=None
            )

        # Check if user exists
        if await user_collection.find_one({"_id": ObjectId(id)}) is None:
            return response_helper(status="failed", message="User not found", data=None)

        # Update user data
        await user_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": user.model_dump()}
        )
        return response_helper(
            status="success", message="User updated successfully", data=None
        )
    except Exception as e:
        return response_helper(status="failed", message=str(e), data=None)
