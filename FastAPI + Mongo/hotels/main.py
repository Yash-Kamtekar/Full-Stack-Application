from fastapi import APIRouter, Body, status
from fastapi.encoders import jsonable_encoder

from .repository import add_hotel
from .scehmas import AddHotel


router = APIRouter(
    tags=["Hotels"],
    prefix="/hotels"
)

@router.post("/add", status_code=status.HTTP_201_CREATED)
async def register_hotel(request_body: AddHotel = Body(...)):
    request_body = jsonable_encoder(request_body)
    new_hotel = await add_hotel(request_body)

    return new_hotel