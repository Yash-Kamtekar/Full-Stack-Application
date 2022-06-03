from pydantic import BaseModel

class RegisterUser(BaseModel):
    username: str
    email: str
    phone: str
    password: str


# class ShowUser(User):
#     class Config:
#         orm_mode = True


class Login(BaseModel):
    username: str
    password: str


# class UserDetail(User):
#     username: str
#     email: str
#     phone: str
#     rewards: int
#     role: str
#     member_type: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None