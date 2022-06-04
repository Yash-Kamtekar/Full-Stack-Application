from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from .repository import user_repository, auth_repository
from . import schemas
from .. import database
from fastapi.security import OAuth2PasswordRequestForm


router = APIRouter(
    tags=["User"],
)


@router.post("/register", status_code=status.HTTP_200_OK)
def register(request: schemas.RegisterUser, db: Session = Depends(database.get_db)):
    return user_repository.register(request, db)


@router.post("/signin", status_code=status.HTTP_200_OK)
def signIn(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    return auth_repository.logIn(request, db)

# @app.delete("/unsubscribe/{id}", status_code=status.HTTP_204_NO_CONTENT)
# def unsubscribe(id, db: Session = Depends(get_db)):
#     db.query(models.User).filter(models.User.username=id).delete(synchronize_session=False)
#     db.commit()
#     return "Successfully Unsubscribed"

# @app.put("/user/update/{id}", status_code=status.HTTP_202_ACCEPTED, response_model=schemas.ShowUser)
# def updateUserData(id, request: schemas.User, db: Session = Depends(get_db)):
#     user = db.query(models.User).filter(models.User.id == id)

#     if not user.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid User")
    
#     user.update({
#         "username": request.username,
#         "email":request.email,
#         "phone":request.phone
#     })
#     db.commit()
#     return "Successfully Updated"