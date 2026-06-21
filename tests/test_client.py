import json
import pytest
import respx
import httpx
from palworld_restapi import PalworldClient, PalworldApiError, ServerInfo


@pytest.fixture
def client():
    with PalworldClient("http://127.0.0.1:8212", password="admin", timeout=1.0) as c:
        yield c


@respx.mock
def test_get_info(client):
    respx.get("http://127.0.0.1:8212/v1/api/info").mock(
        return_value=httpx.Response(
            200,
            json={
                "version": "v0.1.5.0",
                "servername": "Test Server",
                "description": "Test Desc",
                "worldguid": "1234",
            },
        )
    )

    info = client.get_info()
    assert isinstance(info, ServerInfo)
    assert info.version == "v0.1.5.0"
    assert info.servername == "Test Server"


@respx.mock
def test_error_handling(client):
    respx.get("http://127.0.0.1:8212/v1/api/info").mock(
        return_value=httpx.Response(401, text="Unauthorized")
    )

    with pytest.raises(PalworldApiError) as exc:
        client.get_info()

    assert exc.value.status_code == 401
    assert "Unauthorized" in str(exc.value)


@respx.mock
def test_post_endpoints(client):
    req = respx.post("http://127.0.0.1:8212/v1/api/announce").mock(
        return_value=httpx.Response(200)
    )
    client.announce("Hello")
    assert req.called
    assert json.loads(req.calls.last.request.content) == {"message": "Hello"}
