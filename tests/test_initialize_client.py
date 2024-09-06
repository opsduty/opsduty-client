from httpx import Client
from opsduty_client.client import AuthenticatedClient


def test_initialize_authenticated_client() -> None:
    client = AuthenticatedClient(base_url="http://localhost:8000", token="access-token")

    httpx: Client = client.get_httpx_client()

    authorization = httpx.headers["authorization"]

    assert authorization == "Bearer access-token"
