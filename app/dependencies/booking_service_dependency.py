from fastapi import Depends

from app import settings
from app.clients.client import MozioClient
from app.services.booking_service import BookingService


@Depends
def get_booking_service() -> BookingService:
    return BookingService(
        transportation_client=MozioClient(
            settings.MOZIO_BASE_URL, settings.MOZIO_ACCESS_TOKEN
        )
    )
