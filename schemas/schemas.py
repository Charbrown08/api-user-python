from pydantic import BaseModel

class AddressM(BaseModel):
    id:int
    address_1:str
    address_2:str 
    city:str
    state:str
    zip: int
    country:str 

    class Config:
        orm_mode = True

class UserM(BaseModel):
    id:int
    name: str 
    lastname: str 
    age: int 
    email: str 
    password: str 
    address: list[AddressM]= []

    class Config:
        orm_mode = True


