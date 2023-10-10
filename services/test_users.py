from unittest.mock import Mock
from models.models import User, Address
from services.users import UserService


class TestUserService:
    def test_get_users(self):
        db_mock = Mock()
        user_service = UserService(db_mock)
        db_mock.query().options().all.return_value = [
            User(),
            User(),
        ]
        users = user_service.get_users()
        assert isinstance(users, list)
        assert len(users) == 2

    def test_get_user_id(self):
        db_mock = Mock()
        user_service = UserService(db_mock)
        db_mock.query().options().get.return_value = User()
        user = user_service.get_user_id(1)
        assert isinstance(user, User)

    def test_get_user_country(self):
        db_mock = Mock()
        user_service = UserService(db_mock)
        db_mock.query().filter().options().all.return_value = [
            User(),
            User(),
        ]
        users = user_service.get_user_country("Country")
        assert isinstance(users, list)
        assert len(users) == 2
