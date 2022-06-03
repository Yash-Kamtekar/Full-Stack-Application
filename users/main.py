from fastapi import FastAPI
from . import database, models
from .routers import user, auth


models.Base.metadata.create_all(bind=database.engine)


app = FastAPI()
app.include_router(user.router)
app.include_router(auth.router)


# @app.post("/signin", status_code=status.HTTP_200_OK)
# def signIn(response = Response, db: Session = Depends(get_db)):
#     print("here")

#     # hashed_pwd = pwd_cxt.hash(request.password)
#     # users = db.query(models.User).filter(models.User.username == request.username and models.User.password == hashed_pwd)

#     # if not users:
#     #     response.status_code = status.HTTP_401_UNAUTHORIZED
#     #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Username/Password incorrect")

#     # return users
#     pass


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