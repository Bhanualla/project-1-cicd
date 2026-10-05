from app import app


def test_health_endpoint():
    client = app.test_client()

    response = client.get("/health")

    assert response.status_code == 204


def test_home_endpoint():
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 205


def test_info_endpoint():
    client = app.test_client()

    response = client.get("/info")

    assert response.status_code == 200