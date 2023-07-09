from app.clients.client import TransporationClient
from app.clients.mozio.schemas import CancelReservationResponse, PollReservationResponse, PollSearchResponse, StartReservationResponse, StartSearchProcessRequest, StartSearchProcessResponse
import requests
import enum
from app import settings


class HTTPMethod(enum.Enum):
    POST = "POST"
    GET = "GET"
    DELETE = "DELETE"


class MozioClient(TransporationClient):

    def __init__(self, base_url, access_token) -> None:
        self.base_url = base_url
        self.access_token = access_token

    def _make_request(self, method: HTTPMethod, url: str, data=None) -> requests.Response:
        headers = {"API-KEY": f"{self.access_token}",
                   "Content-Type": "application/json"}
        url = f"{self.base_url}{url}"

        return self.make_request(method, url, data, headers)

    def start_search(self, request: StartSearchProcessRequest) -> StartSearchProcessResponse:
        method = "POST"
        url = "search/"
        response = self._make_request(method, url, request)
        print(response)
        return StartSearchProcessResponse(**response.json())

    def poll_search(self, search_id: str) -> PollSearchResponse:
        method = "GET"
        url = f"search/{search_id}/poll"
        response = self._make_request(method, url)
        return PollSearchResponse(**response.json())

    def start_reservation(self, request) -> StartReservationResponse:
        method = "POST"
        url = "reservations/"
        response = self._make_request(method, url, request)
        return StartReservationResponse(**response.json())

    def poll_reservation(self, search_id: str) -> PollReservationResponse:
        method = "GET"
        url = f"reservations/{search_id}/poll"
        response = self._make_request(method, url)
        return PollReservationResponse(**response.json())

    def cancel_reservation(self, confirmation_number: str) -> CancelReservationResponse:
        method = "DELETE"
        url = f"reservations/{confirmation_number}"
        response = self._make_request(method, url)
        return CancelReservationResponse(**response.json())
