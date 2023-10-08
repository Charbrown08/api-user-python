from config.database import Base
from sqlalchemy import Column, Integer, String

class Address(Base):

    __tablename__ = "address"

    id = Column(Integer, primary_key=True)
    address_1= Column(String)
    address_2= Column(String)
    city= Column(String)
    state= Column(String)
    zip= Column(Integer)
    country= Column(String)