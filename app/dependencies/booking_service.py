from fastapi import Depends
from app.clients.client import MozioClient
from app.services.booking_service import BookingService
from app import settings


@Depends
def get_booking_service() -> BookingService:
    return BookingService(
        transportation_client=MozioClient(
            settings.MOZIO_BASE_URL, settings.MOZIO_ACCESS_TOKEN)
    )
