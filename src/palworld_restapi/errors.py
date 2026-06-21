class PalworldApiError(Exception):
    """Exception raised for errors returned by the Palworld REST API."""

    def __init__(
        self, status_code: int, method: str, path: str, response_body: str
    ) -> None:
        self.status_code = status_code
        self.method = method
        self.path = path
        self.response_body = response_body
        super().__init__(
            f"Palworld API Error {status_code} on {method} {path}: {response_body}"
        )
