from fastapi.testclient import TestClient

from app.core.config import settings

class TestHealthEndpoint:
    """ Tests health endpoint
    """

    def test_health_endpoint(self, client: TestClient) -> None:
        """ Test of health endpoint
        """
        response = client.get("/")
        assert response.status_code == 200
