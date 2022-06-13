from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from .repository import hotel_repository
from . import schemas as hotel_schemas
from .. import database
from ..users import schemas, oauth2


router = APIRouter(
    tags=["Hotel"],
    prefix="/hotels"
)


@router.get("/", status_code=status.HTTP_200_OK)
# def getAllHotels(current_user: schemas.UserDetail = Depends(oauth2.get_current_user)):
def getAllHotels():

    return f"hotels"


@router.post("/add", status_code=status.HTTP_200_OK)
# def addHotel(request: hotel_schemas.AddHotel, db: Session = Depends(database.get_db), current_user: schemas.UserDetail = Depends(oauth2.get_current_user)):
def addHotel(request: hotel_schemas.AddHotel, db: Session = Depends(database.get_db)):
    return hotel_repository.addHotel(request, db)

# @router.get("/", status_code=status.HTTP_200_OK)
# def getAllHotels(location: str, start_date: str, end_date: str):


#     return f"Hotels available from {start_date} to {end_date} around this {location} are"