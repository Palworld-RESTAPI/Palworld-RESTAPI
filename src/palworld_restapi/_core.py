from typing import Any
import httpx

from .errors import PalworldApiError


def build_url(base_url: str, path: str) -> str:
    """Build a full URL for the Palworld API."""
    base = base_url.rstrip("/")
    if not base.endswith("/v1/api"):
        base = f"{base}/v1/api"
    return f"{base}/{path.lstrip('/')}"


def handle_response(response: httpx.Response) -> Any:
    """
    Handle the HTTP response, parsing JSON if successful, or raising PalworldApiError.
    """
    if response.status_code >= 400:
        raise PalworldApiError(
            status_code=response.status_code,
            method=response.request.method,
            path=str(response.request.url),
            response_body=response.text,
        )

    if not response.content:
        return None

    try:
        return response.json()
    except ValueError:
        return response.text
