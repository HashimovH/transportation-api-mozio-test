from app.clients.client import TransporationClient
import requests
import enum
from app import settings
from app.clients.mozio.schemas.reservation import CancelReservationResponse, PollReservationResponse, StartReservationResponse
from app.clients.mozio.schemas.search import PollSearchResponse, SearchResult, StartSearchProcessRequest, StartSearchProcessResponse


class HTTPMethod(enum.Enum):
    POST = "POST"
    GET = "GET"
    DELETE = "DELETE"


class MozioClient(TransporationClient):
    requires_polling = True

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

    def convert_search_result(self, search_results) -> list:
        currency = search_results.currency_info.code
        converted_results = []
        results = search_results.results
        for result in results:
            converted_results.append({
                "result_id": result.result_id,
                "vehicle_id": result.vehicle_id,
                "good_to_know_into": result.good_to_know_info,
                "tags": result.tags,
                "price": result.total_price.total_price.value,
                "price_currency": currency,
                "description": result.steps[0].details.description,
                "vehicle": {
                    "image_url": result.steps[0].details.vehicle.image,
                    "vehicle_type": result.steps[0].details.vehicle.vehicle_type.get('name'),
                    "max_bags": result.steps[0].details.vehicle.max_bags,
                    "max_bags_for_each_passenger": result.steps[0].details.vehicle.is_max_bags_per_person,
                    "max_passengers": result.steps[0].details.vehicle.max_passengers,
                    "category": result.steps[0].details.vehicle.category.get('name'),
                    "num_vehicles": result.steps[0].details.vehicle.num_vehicles,
                    "model": result.steps[0].details.vehicle.model,
                    "make": result.steps[0].details.vehicle.make,
                    "vehicle_class": result.steps[0].details.vehicle.vehicle_class_detail.get('display_name'),
                },
                "time": result.steps[0].details.time,
                "provider": {
                    "name": result.steps[0].details.provider.name,
                    "display_name": result.steps[0].details.provider.display_name,
                    "logo_url": result.steps[0].details.provider.logo_url,
                    "rating": result.steps[0].details.provider.rating,
                    "rating_count": result.steps[0].details.provider.rating_count,
                    "rating_with_decimal": result.steps[0].details.provider.rating_with_decimals,
                },
                "can_cancel_online": result.steps[0].details.cancellation.cancellable_online,
                "can_cancel_offline": result.steps[0].details.cancellation.cancellable_offline,
                "can_amend": result.steps[0].details.cancellation.amendable,
                "cancel_notice": result.steps[0].details.cancellation.policy[0].get("notice"),
                "cancel_refund_percent": result.steps[0].details.cancellation.policy[0].get("refund_percent"),
                "departure_time": result.steps[0].details.departure_datetime,
                "wait_time_minutes": result.steps[0].details.wait_time.get('minutes_included'),
                "amenities": result.steps[0].details.amenities,
                "alternative_departure_time": result.steps[0].details.alternative_times.get('options')[0].get("departure_datetime"),
                "alternative_arrival_time": result.steps[0].details.alternative_times.get('options')[0].get("arrival_datetime"),
                "needs_flight_info": result.steps[0].details.flight_info_required,
                "notes": result.steps[0].details.notes,
                "terms": result.steps[0].details.terms_url,
                "can_booked": result.steps[0].details.bookable,
            })

        return converted_results
