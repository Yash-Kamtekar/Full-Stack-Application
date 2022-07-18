from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
# from . import token


# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

# def get_current_user(jwt_token: str = Depends(oauth2_scheme)):
#     return token.verify_token(jwt_token)