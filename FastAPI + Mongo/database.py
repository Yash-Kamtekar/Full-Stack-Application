from http import client
from motor.motor_asyncio import AsyncIOMotorClient


client = AsyncIOMotorClient('mongodb://localhost:27017')

db = client.fastapi


hotel_collection = db.hotels
user_collection = db.users


def hotel_helper(hotel) -> dict:
    return {
        "hotel_name": hotel["hotel_name"],
        "address":hotel["address"],
        "country":hotel["country"],
        "state":hotel["state"],
        "city":hotel["city"],
        "state":hotel["state"],
        "stars":hotel["stars"],
        "active":hotel["active"]
    }

def user_helper(user) -> dict:
    return {
        # "id": str(user["_id"]),
        "email": user["email"],
        # "password":user["password"],
        "phone":user["phone"],
        "rewards":user["rewards"],
        "role":user["role"],
        "member_type":user["member_type"]
    }