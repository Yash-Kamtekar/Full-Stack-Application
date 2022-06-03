from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from . import token


oauth2_scheme = OAuth2PasswordBearer(token_url="login")


def get_current_user(token: str = Depends(oauth2_scheme)):


    return token.verify_token(token)