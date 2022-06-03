from fastapi import APIRouter, status, Depends
from .. import database
from ..repository import auth_repository
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm


router = APIRouter(
    tags=["Authentication"],
)


@router.post("/signin", status_code=status.HTTP_200_OK)
def signIn(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    return auth_repository.logIn(request, db)