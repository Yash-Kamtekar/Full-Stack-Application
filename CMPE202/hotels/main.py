from fastapi import APIRouter, Depends, status
from ..users import oauth2, schemas


router = APIRouter(
    tags=["Hotel"],
    prefix="/hotels"
)


@router.get("/", status_code=status.HTTP_200_OK)
def getAllHotels(limit: int = 10, current_user: schemas.UserDetail = Depends(oauth2.get_current_user) ):


    return f"{limit} hotels {current_user}"


# @router.get("/", status_code=status.HTTP_200_OK)
# def getAllHotels(location: str, start_date: str, end_date: str):


#     return f"Hotels available from {start_date} to {end_date} around this {location} are"