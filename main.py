from fastapi import Depends, FastAPI, Body, Path, Query, HTTPException, Request
from pydantic import BaseModel, Field
from typing import Optional, List
from fastapi.responses import HTMLResponse, JSONResponse
from config.database import Session, engine, Base
from models.models import User as UserModel
from models.models import Address as AddressModel
from sqlalchemy.orm import joinedload


from fastapi.encoders import jsonable_encoder
from middlewares.error_handler import ErrorHandler


app = FastAPI()
app.title = "Api Users"
app.version = "0.0.1"

app.add_middleware(ErrorHandler)

Base.metadata.create_all(bind=engine)


class AddressM(BaseModel):
    address_1: str
    address_2: str
    city: str
    state: str
    zip: int
    country: str

    class Config:
        orm_mode = True


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


# POST


@app.post("/users", tags=["Users"])
def crear_usuario(user: UserM):
    db = Session()
    new_address = AddressModel(
        address_1=user.address.address_1,
        address_2=user.address.address_2,
        city=user.address.city,
        state=user.address.state,
        zip=user.address.zip,
        country=user.address.country.lower(),
    )
    new_user = UserModel(
        name=user.name.lower(),
        lastname=user.lastname.lower(),
        age=user.age,
        email=user.email.lower(),
        password=user.password,
        address=new_address,
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    db.refresh(new_address)
    return {"usuario": new_user, "direccion": new_address}


# crea un enpoint que permita obtner todos los usuarios con sus direccione


@app.get("/users", tags=["Users"])
def obtener_usuarios():
    db = Session()
    users = db.query(UserModel).options(joinedload(UserModel.address)).all()
    if not users:
        raise HTTPException(status_code=404, detail="users not found")
    return users


# crea un enpoint que permita obtner un usuario con sus direcciones


@app.get("/users/{id}", tags=["Users"])
def obtener_usuario(id: int):
    db = Session()
    user = db.query(UserModel).options(joinedload(UserModel.address)).get(id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


# crea un usuario que permita actualizar un usuario con sus direcciones


@app.put("/users/{id}", tags=["Users"])
def actualizar_usuario(id: int, user_data: UpdateUserM):
    db = Session()
    existing_user = db.query(UserModel).filter(UserModel.id == id).first()

    if existing_user is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    if user_data.name is not None:
        existing_user.name = user_data.name
    if user_data.lastname is not None:
        existing_user.lastname = user_data.lastname
    if user_data.age is not None:
        existing_user.age = user_data.age
    if user_data.email is not None:
        existing_user.email = user_data.email.lower()
    if user_data.password is not None:
        existing_user.password = user_data.password
    if user_data.address is not None:
        address_data = user_data.address.dict(
            exclude_unset=True
        )  # Serializa la dirección actualizada sin campos no proporcionados
        existing_user.address = AddressModel(**address_data)

    db.commit()
    db.refresh(existing_user)
    return {"mensaje": "Usuario actualizado correctamente"}


# create un endpoint que permita eliminar un usuario con sus direcciones


@app.delete("/users/{id}", tags=["Users"])
def eliminar_usuario(id: int):
    db = Session()
    user = db.query(UserModel).get(id)
    if user is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    db.delete(user)
    db.commit()
    return {"mensaje": "Usuario eliminado correctamente"}


# crear un enpoint que permita obtner todos los usuarios  por el nombre de su pais en la direccion


@app.get("/users/country/{country}", tags=["Users"])
def get_users_by_country(country: str):
    country = country.lower()
    db = Session()
    users = (
        db.query(UserModel)
        .filter(UserModel.address.has(country=country))
        .options(joinedload(UserModel.address))
        .all()
    )
    if not users:
        raise HTTPException(status_code=404, detail="users not found with this country")
    return users
