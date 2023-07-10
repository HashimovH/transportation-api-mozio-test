from fastapi import APIRouter

from app.dependencies.booking_service_dependency import get_booking_service
from app.routers.schemas import (
    CancelReservationAPIResponse,
    SearchResultsResponseList,
    StartOperationsAPIResponse,
    StartReservationAPIRequest,
    StartSearchAPIRequest,
)
from app.services.booking_service import BookingService

router = APIRouter()


@router.post(
    "/api/v1/search",
    response_model=StartOperationsAPIResponse,
    description="""Starts a search process and returns status of loading parameter. 
    Send second request to /api/v1/search/{search_id}/more to get results.""",
    name="Start Search",
    tags=["search"],
)
def start_search(
    request: StartSearchAPIRequest,
    booking_service: BookingService = get_booking_service,
) -> StartOperationsAPIResponse:
    return booking_service.start_search_process(request)


@router.get(
    "/api/v1/search/{search_id}/more",
    response_model=SearchResultsResponseList,
    description="""Returns results of search process. 
    If loading is true, send another request to this endpoint to get more results.""",
    name="Get Search Results",
    tags=["search"],
)
def poll_search(
    search_id: str, booking_service: BookingService = get_booking_service
) -> SearchResultsResponseList:
    search_result = booking_service.poll_search_process(search_id)
    return search_result


@router.post("/api/v1/reservation")
def start_reservation(
    request: StartReservationAPIRequest,
    booking_service: BookingService = get_booking_service,
) -> StartOperationsAPIResponse:
    return booking_service.start_reservation(request)


@router.get("/api/v1/reservation/{reservation_id}/more")
def poll_reservation(
    reservation_id: str, booking_service: BookingService = get_booking_service
):
    reservation_result = booking_service.poll_reservation(reservation_id)
    return reservation_result


@router.delete("/api/v1/reservation/{reservation_id}")
def cancel_reservation(
    reservation_id: str, booking_service: BookingService = get_booking_service
) -> CancelReservationAPIResponse:
    return booking_service.cancel_reservation(reservation_id)
