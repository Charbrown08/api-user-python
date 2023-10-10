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


def test_get_users():
    response = client.get("/users")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
