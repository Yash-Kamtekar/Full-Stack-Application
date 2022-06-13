from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from . import database
from .users import models as user_model
from .users import main as user_main
from .hotels import models as hotel_model
from .hotels import main as hotel_main


user_model.Base.metadata.create_all(bind=database.engine)
hotel_model.Base.metadata.create_all(bind=database.engine)


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



app.include_router(hotel_main.router)
app.include_router(user_main.router)