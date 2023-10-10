from fastapi.testclient import TestClient
from main import app
import pytest

client = TestClient(app)


@pytest.fixture
def sample_user():
    return {
        "name": "John Doe",
        "email": "john.doe@example.com",
        "address": {
            "street": "123 Main St",
            "city": "Sample City",
            "country": "Sample Country",
        },
    }


def test_create_user():
    response = client.post("/users", json=sample_user())
    assert response.status_code == 200
    assert "User con ID" in response.json()["mensaje"]


def test_get_users():
    response = client.get("/users")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_user_by_id():
    response = client.get("/users/1")
    assert response.status_code == 404
    assert "name" in response.json()
