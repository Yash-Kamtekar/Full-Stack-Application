from ..database import Base
from sqlalchemy import Column, Integer, String, Float, Boolean

class Hotel(Base):
    __tablename__ = "hotel"


    id = Column(Integer, primary_key=True, index=True)
    hotel_name = Column(String, unique=True, index=True)
    address = Column(String)
    country = Column(String)
    city = Column(Integer)
    state = Column(String)
    stars = Column(Float)
    active = Column(Boolean)