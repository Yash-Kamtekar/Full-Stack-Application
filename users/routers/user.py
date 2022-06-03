from fastapi import APIRouter, status, Depends
from .. import schemas, database
from ..repository import user_repository
from sqlalchemy.orm import Session


router = APIRouter(
    tags=["User"],
)


@router.post("/register", status_code=status.HTTP_200_OK)
def register(request: schemas.RegisterUser, db: Session = Depends(database.get_db)):
    return user_repository.register(request, db)

