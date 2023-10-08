from fastapi import FastAPI,Body,Path,Query
from pydantic import BaseModel,EmailStr,Field
from typing import Optional,List
from fastapi.responses import JSONResponse

app = FastAPI()
app.title = "Api Users"
app.version = "0.0.1"


#Creamos nuestros modelos de direccion de usuarios 

class AddressModel(BaseModel):
    id:int
    address_1:str = Field(min_length=5,max_length=50)
    address_2: str = Field(max_length=50,min_length=5,ge=0,skip=True)
    city:str=Field(min_length=5,max_length=50)
    state:str=Field(min_length=5,max_length=50)
    zip:Optional[int] = None
    country: str= "Colombia"

    
# creamos nuestro modelo de usuario 

class UserModel(BaseModel):
    id:Optional[int]= None
    name:str
    lastname:str
    age:int
    email:EmailStr 
    password:str
    address:AddressModel




# simulamos datos en una base de datos para retornar  la direccion de un usuario 
address = [{
    "id":1,
    "address_1":"avenida 1° A",
    "address_2":"avenida 2° A",
    "city":"Bogota",
    "state":"Cundinamarca",
    "zip":"123456",
    "country":"Colombia"
},
{
    "id":2,
    "address_1":"avenida 1° B",
    "address_2":"avenida 2° B",
    "city":"Lima",
    "state":"Lima", 
    "zip":"123432",
    "country":"Peru"
},
{
    "id":3,
    "address_1":"avenida 1° c",
    "address_2":"avenida 2° c",
    "city":"Lima",
    "state":"Lima", 
    "zip":"123432",
    "country":"Peru"
}
]

#

# simulamos datos en una base de datos para retornar  el usuario  

users = [{
    "id":1,
    "name":"Juan",
    "lastname":"Perez",
    "age":21,
    "email":"email.com",
    "password":"password123",
    "address":address[0]

},{
    "id":2,
    "name":"Maria",
    "lastname":"Gomez",
    "age":25,
    "email":"email.com",
    "password":"password123",
    "address":address[1]
}
,{
    "id":3,
    "name":"Juan",
    "lastname":"Moreno",
    "age":45,
    "email":"email2.com",
    "password":"password123",
    "address":address[2]
}
]



# Creamos el metodo que nos permitira obtener todos los usuarios
@app.get("/users",tags=['Users'],response_model= List[UserModel])
def get_users()-> List[UserModel]:
    return JSONResponse(status_code=200,content=users)



# creamos el endpoint para obtener un usuario por su id en la ruta del endpoint
@app.get("/users/by/{id}",tags=['Users'],response_model= UserModel)
def get_user_by_id(id:int)-> UserModel:
    for user in users:
        if user["id"] == id:
            return JSONResponse(status_code=200,content=user)
    return JSONResponse(status_code=404,content={"message":"user not found"})

# Creamos el metodo que nos permitira obtener usuarios por su pais 

@app.get("/users/country/{country}",tags=['Users'],response_model=List[UserModel])
def get_users_by_country(country:str=Path(min_length=1,max_length=30))->List[UserModel]:
    userCountry=[user for user in users if user["address"]["country"].lower() == country.lower()]
    return JSONResponse(status_code=200,content=userCountry)



#cramos el endpoint que nos permitira crear usuarios 
@app.post("/users",tags=['Users'], response_model=dict,status_code=201)
def create_users(user: UserModel)-> dict:
    users.append(user)
    return JSONResponse(status_code=201,content={"message":"user created succesfully"})

# #creaamos el  endpoint que nos permitira actualizar un usuario por su id
@app.put("/users/{id}",tags=['Users'], response_model= dict,status_code=200)
def update_users(
    id:int,
    user: UserModel) -> dict:
    for user in users:
        if user["id"] == id:
            user["name"] = user.name
            user["lastname"] = user.lastname
            user["age"] = user.age
            user["email"] = user.email
            user["password"] = user.password
            user["address"] = user.address
            return JSONResponse(status_code=200,content={"message":"user updated"})
    
          
#creamos el endpoint que nos permitira eliminar un usuario por su id

@app.delete("/users/{id}", tags=["Users"], response_model=dict, status_code=200)
def delete_users(id: int) -> dict:
    for user in users:
        if user["id"] == id:
            users.remove(user)
            return JSONResponse(
                status_code=200, content={"message": "Delete user"}
            )
