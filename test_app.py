from app import add, app


def test_add():
    assert add(2, 3) == 6


def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
