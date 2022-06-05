from fastapi import status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from .. import models, token
from sqlalchemy.orm import Session
from ..hashing import Hash


def logIn(request: OAuth2PasswordRequestForm, db: Session):

    user = db.query(models.User).filter(models.User.username == request.username).first()


    if not user or not Hash.verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Username/Password incorrect")


    # access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = token.create_access_token(
        data={"sub": user.username},
        # expires_delta=access_token_expires
    )

    response = {
        "access_token": access_token,
        "user_details": {
            "username": user.username,
            "phone": user.phone,
            "email": user.email,
            "rewards": user.rewards,
            "member_type": user.member_type,
            "role": user.role
        }
    }


    return response