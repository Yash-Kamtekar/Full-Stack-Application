from fastapi import HTTPException, status

from ..auth.hashing import Hash
from ..auth.token import create_access_token
from ..database import user_collection, user_helper


async def add_user(user_data: dict) -> dict:

    user_data["password"] = Hash.bcrypt(user_data["password"])

    if await user_collection.find_one({"email": user_data["email"]}):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="User already exists")

    user = await user_collection.insert_one(user_data)
    new_user = await user_collection.find_one({"_id": user.inserted_id})

    return user_helper(new_user)

async def login_user(user_data: dict) -> dict:

    user = await user_collection.find_one({"email": user_data["email"]})

    if not user or not Hash.verify(user["password"], user_data["password"]):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Username/Password incorrect")

    access_token = create_access_token(
        data={"sub": user["email"]}
    )

    response = {
        "access_token": access_token,
        "user_details": user_helper(user)
    }

    return response