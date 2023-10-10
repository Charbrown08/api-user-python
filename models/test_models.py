from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.models import User, Address, Base

engine = create_engine("sqlite:///:memory:")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)


def test_create_user():
    user_data = {
        "name": "John",
        "lastname": "Doe",
        "age": 30,
        "email": "john.doe@example.com",
        "password": "password123",
    }
    db = SessionLocal()
    user = User(**user_data)
    db.add(user)
    db.commit()
    db.refresh(user)
    assert user.id is not None
    db.close()


def test_create_address():
    address_data = {
        "address_1": "123 Main St",
        "city": "Anytown",
        "state": "CA",
        "zip": 12345,
        "country": "USA",
    }
    db = SessionLocal()
    address = Address(**address_data)
    db.add(address)
    db.commit()
    db.refresh(address)
    assert address.id is not None
    db.close()


def test_user_address_relationship():
    user_data = {
        "name": "Jane",
        "lastname": "Smith",
        "age": 25,
        "email": "jane.smith@example.com",
        "password": "password456",
    }
    address_data = {
        "address_1": "456 Elm St",
        "city": "Sometown",
        "state": "NY",
        "zip": 67890,
        "country": "USA",
    }
    db = SessionLocal()
    user = User(**user_data)
    address = Address(**address_data)
    user.address = address
    db.add(user)
    db.commit()
    db.refresh(user)
    assert user.address is not None
    assert user.address.id == address.id
    db.close()
