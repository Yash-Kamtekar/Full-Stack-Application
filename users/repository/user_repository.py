from fastapi import status, HTTPException
from .. import schemas, models
from sqlalchemy.orm import Session
from ..hashing import Hash


def register(request: schemas.RegisterUser, db: Session):

    hashed_pwd = Hash.bcrypt(request.password)

    new_user = models.User(
        username=request.username,
        email=request.email,
        password=hashed_pwd,
        phone=request.phone,
        rewards=1000,
        role="Customer",
        member_type="Silver",
        hotel_id=None
    )


    try:
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
    except Exception:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Email Address already registered")

    return {"details": "Successfully Registered"}