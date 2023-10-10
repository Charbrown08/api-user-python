from fastapi import APIRouter
from fastapi import HTTPException
from config.database import Session
from models.models import User as UserModel
from models.models import Address as AddressModel
from sqlalchemy.orm import joinedload
from services.users import UserService
from schemas.user import UserM
from schemas.address import AddressM
from schemas.user import UpdateUserM


user_router = APIRouter()


@user_router.post("/users", tags=["Users"])
def crear_usuario(user: UserM):
    db = Session()
    userId = UserService(db).create_user(user)
    return {f"User con ID {userId} created successfully"}


# crea un enpoint que permita obtner todos los usuarios con sus direccione


@user_router.get("/users", tags=["Users"])
def obtener_usuarios():
    db = Session()
    users = UserService(db).get_users()
    if not users:
        raise HTTPException(status_code=404, detail="users not found")
    return users


# crea un enpoint que permita obtner un usuario con sus direcciones


@user_router.get("/users/{id}", tags=["Users"])
def obtener_usuario(id: int):
    db = Session()
    user = UserService(db).get_user_id(id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


# crea un usuario que permita actualizar un usuario con sus direcciones


@user_router.put("/users/{id}", tags=["Users"])
def actualizar_usuario(id: int, user_data: UpdateUserM):
    db = Session()
    result = UserService(db).get_user_id(id)
    if not result:
        raise HTTPException(status_code=404, detail="User not found")
    UserService(db).update_user(id, user_data)
    return {"mensaje": "Usuario actualizado correctamente"}


# create un endpoint que permita eliminar un usuario con sus direcciones


@user_router.delete("/users/{id}", tags=["Users"])
def eliminar_usuario(id: int):
    db = Session()
    user = db.query(UserModel).get(id)
    if user is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    UserService(db).delete_user(id)
    return {"mensaje": "Usuario eliminado correctamente"}


# crear un enpoint que permita obtner todos los usuarios  por el nombre de su pais en la direccion


@user_router.get("/users/country/{country}", tags=["Users"])
def get_users_by_country(country: str):
    country = country.lower()
    db = Session()
    users = UserService(db).get_user_country(country)
    if not users:
        raise HTTPException(status_code=404, detail="users not found with this country")
    return users
