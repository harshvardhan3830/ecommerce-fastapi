from motor.motor_asyncio import AsyncIOMotorClient
from .config import MONGO_URL, DATABASE_NAME

# Create a client object to connect to the database
# Asynchronous I/O is used to interact with the database
# The client object is used to interact with the database
client = AsyncIOMotorClient(MONGO_URL)

# The client object is used to interact with the database
database = client[DATABASE_NAME]


# collections

user_collection = database.get_collection("users")
product_collection = database.get_collection("products")
