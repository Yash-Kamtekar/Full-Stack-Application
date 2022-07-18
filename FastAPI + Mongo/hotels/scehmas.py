from pydantic import BaseModel, Field


class AddHotel(BaseModel):
    hotel_name: str = Field(...)
    address: str = Field(...)
    country: str = Field(...)
    city: str = Field(...)
    state: str = Field(...)
    stars: float = Field(...)
    active: bool = Field(...)