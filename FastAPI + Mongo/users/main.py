from fastapi import APIRouter, Body, status
from fastapi.encoders import jsonable_encoder

from .repository import add_user, login_user
from .schemas import LoginUser, RegisterUser


router = APIRouter(
    tags=['User'],
    prefix='/users'
)

@router.post('/register', status_code=status.HTTP_201_CREATED)
async def register(request_body: RegisterUser = Body(...)):

    request_body = jsonable_encoder(request_body)
    new_user = await add_user(request_body)

    return {"data": new_user}


@router.post("/signin", status_code=status.HTTP_200_OK)
async def login(request_body: LoginUser = Body(...)):

    request_body = jsonable_encoder(request_body)
    user = await login_user(request_body)

    return user
