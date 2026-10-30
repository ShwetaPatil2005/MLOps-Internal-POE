from hello import app

def test_home_returns_200_and_greeting():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"Hello, MLOps UAT!" in response.data

def test_health_endpoint_returns_healthy():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json() == {"status": "healthy"}
