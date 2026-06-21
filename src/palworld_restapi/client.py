from typing import Any, Self
import httpx

from ._core import build_url, handle_response
from .models import ServerInfo, PlayersResponse, ServerSettings, ServerMetrics


class PalworldClient:
    def __init__(
        self,
        base_url: str,
        password: str,
        username: str = "admin",
        timeout: float = 10.0,
    ) -> None:
        self.base_url = base_url
        auth = (username, password)
        self._client = httpx.Client(auth=auth, timeout=timeout)

    def __enter__(self) -> Self:
        self._client.__enter__()
        return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        self._client.__exit__(exc_type, exc_val, exc_tb)

    def close(self) -> None:
        self._client.close()

    def get_info(self) -> ServerInfo:
        url = build_url(self.base_url, "info")
        response = self._client.get(url)
        data = handle_response(response)
        return ServerInfo.from_dict(data)

    def get_players(self) -> PlayersResponse:
        url = build_url(self.base_url, "players")
        response = self._client.get(url)
        data = handle_response(response)
        return PlayersResponse.from_dict(data)

    def get_settings(self) -> ServerSettings:
        url = build_url(self.base_url, "settings")
        response = self._client.get(url)
        data = handle_response(response)
        return ServerSettings.from_dict(data)

    def get_metrics(self) -> ServerMetrics:
        url = build_url(self.base_url, "metrics")
        response = self._client.get(url)
        data = handle_response(response)
        return ServerMetrics.from_dict(data)

    def announce(self, message: str) -> None:
        url = build_url(self.base_url, "announce")
        response = self._client.post(url, json={"message": message})
        handle_response(response)

    def kick_player(self, userid: str, message: str | None = None) -> None:
        url = build_url(self.base_url, "kick")
        payload = {"userid": userid}
        if message is not None:
            payload["message"] = message
        response = self._client.post(url, json=payload)
        handle_response(response)

    def ban_player(self, userid: str, message: str | None = None) -> None:
        url = build_url(self.base_url, "ban")
        payload = {"userid": userid}
        if message is not None:
            payload["message"] = message
        response = self._client.post(url, json=payload)
        handle_response(response)

    def unban_player(self, userid: str) -> None:
        url = build_url(self.base_url, "unban")
        response = self._client.post(url, json={"userid": userid})
        handle_response(response)

    def save(self) -> None:
        url = build_url(self.base_url, "save")
        response = self._client.post(url)
        handle_response(response)

    def shutdown(self, waittime: int, message: str | None = None) -> None:
        url = build_url(self.base_url, "shutdown")
        payload: dict[str, Any] = {"waittime": waittime}
        if message is not None:
            payload["message"] = message
        response = self._client.post(url, json=payload)
        handle_response(response)

    def stop(self) -> None:
        url = build_url(self.base_url, "stop")
        response = self._client.post(url)
        handle_response(response)
