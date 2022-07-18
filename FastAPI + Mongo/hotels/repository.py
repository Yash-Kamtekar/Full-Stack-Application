from fastapi import HTTPException, status

from ..database import hotel_collection, hotel_helper

async def add_hotel(request_body: dict) -> dict:

    if await hotel_collection.find_one({"hotel_name": request_body["hotel_name"]}):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Whoops ! This hotel already exists")

    hotel = await hotel_collection.insert_one(request_body)
    new_hotel = await hotel_collection.find_one({"_id": hotel.inserted_id})

    return hotel_helper(new_hotel)
