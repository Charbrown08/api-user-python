from fastapi import HTTPException
from models.models import User as UserModel
from models.models import Address as AddressModel
from sqlalchemy.orm import joinedload


class UserService:
    def __init__(self, db) -> None:
        self.db = db

    def get_users(self):
        result = self.db.query(UserModel).options(joinedload(UserModel.address)).all()
        return result

    def get_user_id(self, id):
        result = self.db.query(UserModel).options(joinedload(UserModel.address)).get(id)
        return result

    def get_user_country(self, country):
        result = (
            self.db.query(UserModel)
            .filter(UserModel.address.has(country=country))
            .options(joinedload(UserModel.address))
            .all()
        )
        return result

    def create_user(self, user: UserModel):
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

        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)
        self.db.refresh(new_address)

        return new_user.id

    def update_user(self, id: int, user_data: UserModel):
        existing_user = self.db.query(UserModel).filter(UserModel.id == id).first()

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
            address_data = user_data.address.dict(exclude_unset=True)
            existing_user.address = AddressModel(**address_data)

        self.db.commit()
        self.db.refresh(existing_user)
        return

    def delete_user(self, id: int):
        self.db.query(UserModel).filter(UserModel.id == id).delete()
        self.db.commit()
        return
