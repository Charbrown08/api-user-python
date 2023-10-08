from fastapi import Depends, FastAPI,Body,Path,Query,HTTPException,Request
from pydantic import BaseModel,Field
from typing import Optional,List
from fastapi.responses import HTMLResponse, JSONResponse
from config.database import Session,engine,Base
from models.user import User as UserModel
from models.address import Address as AddressModel
from fastapi.encoders import jsonable_encoder

app = FastAPI()
app.title = "Api Users"
app.version = "0.0.1"

Base.metadata.create_all(bind=engine)
  
# creamos nuestro modelo de usuario 

class UserM(BaseModel):
    id: Optional[int]= None
    name: str = Field(min_length=5,max_length=50)
    lastname: str = Field(min_length=5,max_length=50)
    age: int = Field(ge=1)
    email: str = Field(min_length=5,max_length=50)
    password: str = Field(min_length=5,max_length=50)
    address: str = Field(min_length=5,max_length=50)

   


# Creamos el metodo que nos permitira obtener todos los usuarios
@app.get("/users",tags=['Users'],response_model= List[UserM])
def get_users()-> List[UserM]:
    db= Session()
    result= db.query(UserModel).all() 
    if not result:
        JSONResponse(status_code=404,content={"message":"users not found"})
    return JSONResponse(status_code=200,content=jsonable_encoder(result))


# Creamos el endopoint que nos permitira obtener un usuario por su id

@app.get("/users/{id}",tags=['Users'],response_model= UserM)
def get_user_by_id(id: int)-> UserM:
    db = Session()
    result = db.query(UserModel).filter(UserModel.id == id).first()
    if not result:
       return JSONResponse(status_code=404,content={"message":"user not found"})
    return JSONResponse(status_code=200,content=jsonable_encoder(result))



#creamos que nos permitira buscar el usuario por  su direccion 

@app.get("/users/address/{address}",tags=['Users'],response_model= List[UserM])
def get_user_by_address(address: str)-> List[UserM]:
    db = Session()
    result = db.query(UserModel).filter(UserModel.address == address).all()
    if not result:
        return JSONResponse(status_code=404,content={"message":"user not found"})
    return JSONResponse(status_code=200,content=jsonable_encoder(result))




#cramos el endpoint que nos permitira crear usuarios 
@app.post("/users",tags=['Users'], response_model= UserM,status_code=201)
def create_users(user: UserM)-> UserM:
    db = Session()
    new_user = UserModel(**user.dict())
    db.add(new_user)
    db.commit()
    return JSONResponse(status_code=201,content={"message":"user created succesfully"})


# creamos el endpoint que nos permitira actualizar un usuario

@app.put("/users/{id}",tags=['Users'], response_model= UserM,status_code=201)
def update_user(id: int,user: UserM)-> UserM:
    db = Session()
    result = db.query(UserModel).where(UserModel.id == id).first()

    if result:
        result.name = user.name
        result.lastname = user.lastname
        result.age = user.age
        result.email = user.email
        result.password = user.password
        result.address = user.address
        db.commit()
        return JSONResponse(status_code=201,content={"message":"user updated succesfully"}) 
    if not result:
        return JSONResponse(status_code=404,content={"message":"user not found"})

#creamos el endpoint que nos permitira eliminar un usuario
@app.delete("/users/{id}",tags=['Users'],response_model= UserM,status_code=201)
def delete_user(id: int)-> UserM:
    db = Session()
    result = db.query(UserModel).where(UserModel.id == id).first()
    if result:
        db.delete(result)
        db.commit()
        return JSONResponse(status_code=201,content={"message":"user deleted succesfully"})
    if not result:
        return JSONResponse(status_code=404,content={"message":"user not found"})