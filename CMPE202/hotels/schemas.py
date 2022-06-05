from pydantic import BaseModel


class AddHotel(BaseModel):
    hotel_name: str
    address: str
    city: str
    state: str
    country: str