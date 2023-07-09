from app.routers.schemas import CancelReservationAPIResponse, SearchResultReponse, StartReservationAPIRequest, StartOperationsAPIResponse, StartSearchAPIRequest


class BookingService:
    def __init__(self, transportation_client) -> None:
        self.transportation_client = transportation_client

    def start_search_process(self, request: StartSearchAPIRequest) -> StartOperationsAPIResponse:
        response = self.transportation_client.start_search(request)
        return StartOperationsAPIResponse(is_loading=response.more_coming)

    def poll_search_process(self, search_id: str) -> tuple[SearchResultReponse, bool]:
        response = self.transportation_client.poll_search(search_id)
        converted_results = self.transportation_client.convert_search_result(
            response)
        return SearchResultReponse(**converted_results), response.more_coming

    def start_reservation(self, request: StartReservationAPIRequest) -> StartOperationsAPIResponse:
        response = self.transportation_client.start_reservation(request)
        if response.status == "failed":
            raise Exception("Reservation failed")  # TODO: Proper exception
        elif response.status == "pending":
            return StartOperationsAPIResponse(is_loading=True)
        elif response.status == "confirmed":
            return StartOperationsAPIResponse(is_loading=False)

    def poll_reservation(self, search_id: str) -> tuple[list, bool]:
        response = self.transportation_client.poll_reservation(search_id)
        return response.reservations, response.more_coming

    def cancel_reservation(self, search_id: str) -> CancelReservationAPIResponse:
        response = self.transportation_client.cancel_reservation(search_id)
        return CancelReservationAPIResponse(refunded=response.refunded, cancelled=response.cancelled)
