from app import app


def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert response.data == b"Hello from my Jenkins CI/CD demo application!, this is my demo to community rev from Cornel Earle test2 auto"
