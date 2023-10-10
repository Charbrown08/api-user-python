from pydantic import BaseModel


class AddressM(BaseModel):
    address_1: str
    address_2: str
    city: str
    state: str
    zip: int
    country: str

    class Config:
        orm_mode = True
