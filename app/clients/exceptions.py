import requests


class MozioClientInvalidRequest(Exception):
    def __init__(self, response: requests.Response) -> None:
        self.response = response
        self.message = f"Invalid request to {response.url}: {response.status_code} {response.text}"
        super().__init__(self.message)


class MoziaClientTimeout(Exception):
    def __init__(self, response: requests.Response) -> None:
        self.response = response
        self.message = f"Request to {response.url} timed out"
        super().__init__(self.message)


class MoziaClientRequestFailed(Exception):
    def __init__(self, response: requests.Response) -> None:
        self.response = response
        self.message = f"Request to {response.url} failed"
        super().__init__(self.message)
