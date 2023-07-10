import abc
import enum

import requests

from app.clients.exceptions import (
    TransportationClientInvalidRequest,
    TransportationClientRequestFailed,
    TransportationClientTimeout,
)


class HTTPMethod(enum.Enum):
    POST = "POST"
    GET = "GET"
    DELETE = "DELETE"


class TransporationClient(abc.ABC):
    requires_polling = False

    def make_request(
        self, method: HTTPMethod, url: str, data=None, headers: dict = dict({})
    ) -> requests.Response:
        try:
            response: requests.Response = requests.request(
                method=method, url=url, headers=headers, json=data
            )
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            raise TransportationClientInvalidRequest(e.response)
        except requests.exceptions.Timeout as e:
            raise TransportationClientTimeout(e.response)
        except requests.exceptions.RequestException as e:
            raise TransportationClientRequestFailed(e.response)

        return response

    @abc.abstractmethod
    def start_search(self, request):
        pass

    @abc.abstractmethod
    def poll_search(self, search_id: str):
        pass

    @abc.abstractmethod
    def start_reservation(self, request):
        pass

    @abc.abstractmethod
    def poll_reservation(self, search_id: str):
        pass

    @abc.abstractmethod
    def cancel_reservation(self, confirmation_number: str):
        pass

    @abc.abstractmethod
    def convert_search_result(self, search_result):
        pass
