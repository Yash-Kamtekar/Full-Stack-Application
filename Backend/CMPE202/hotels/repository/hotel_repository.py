from fastapi import status, HTTPException
from .. import schemas, models
from sqlalchemy.orm import Session


def addHotel(request: schemas.AddHotel, db: Session):
    
    new_hotel = models.Hotel(
        hotel_name = request.hotel_name,
        address = request.address,
        city = request.city,
        state = request.state,
        country = request.country,
        active = True,
        stars = 0
    )


    try:
        db.add(new_hotel)
        db.commit()
        db.refresh(new_hotel)
    except Exception:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Oops! Hotel Name already registered in our system")

    return {"details": "Successfully Registered"}


def getHotels(db: Session):

    hotels = db.query(models.Hotel).all()
    return hotels