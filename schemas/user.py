from typing import Optional
from pydantic import BaseModel
from schemas.address import AddressM


class UserM(BaseModel):
    name: str
    lastname: str
    age: int
    email: str
    password: str
    address: AddressM

    class Config:
        orm_mode = True


class UpdateUserM(BaseModel):
    name: Optional[str] = None
    lastname: Optional[str] = None
    age: Optional[int] = None
    email: Optional[str] = None
    password: Optional[str] = None
    address: Optional[AddressM] = None

    class Config:
        orm_mode = True
