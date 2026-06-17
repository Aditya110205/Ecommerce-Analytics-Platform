from fastapi.testclient import TestClient

from api.main import app

client = TestClient(app)


def test_health():

    response = client.get("/health")

    assert response.status_code == 200

    assert response.json() == {
        "status": "healthy"
    }
    
def test_daily_revenue():

    response = client.get(
        "/daily-revenue"
    )

    assert response.status_code == 200

    assert isinstance(
        response.json(),
        list
    )