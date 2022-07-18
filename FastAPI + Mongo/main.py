from fastapi import FastAPI

from .hotels import main as hotel_route
from .users import main as user_route


app = FastAPI()

app.include_router(hotel_route.router)
app.include_router(user_route.router)