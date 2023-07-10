import pytest

from app.clients.mozio.mozio_client import MozioClient
from app.clients.mozio.schemas.search import StartSearchProcessRequest
from app.routers.schemas import StartReservationAPIRequest
from app.services.booking_service import BookingService


@pytest.fixture(scope="session")
def client():
    return MozioClient(
        "https://api-testing.mozio.com/v2/", "6bd1e15ab9e94bb190074b4209e6b6f9"
    )


@pytest.fixture(scope="session")
def service(client):
    return BookingService(client)


@pytest.mark.vcr
def test_service_start_search(service):
    request = StartSearchProcessRequest(
        start_address="44 Tehama Street, San Francisco, CA, USA",
        end_address="SFO",
        mode="one_way",
        pickup_datetime="2023-12-01 15:30",
        num_passengers=2,
        currency="USD",
        campaign="Hashim Hashimov",
    )
    response = service.start_search_process(request)
    assert response.is_loading


@pytest.mark.vcr
def test_poll_search_in_service(service):
    response = service.poll_search_process("187003663b8f4a5ca7c079e6df057cd3")
    assert response
    assert len(response.results) > 0


@pytest.mark.vcr
def test_start_reservation(service):
    request = StartReservationAPIRequest(
        search_id="187003663b8f4a5ca7c079e6df057cd3",
        result_id="0065652958e49ffe698cca03fdf8c9e4",
        email="pytest@gmail.com",
        country_code_name="US",
        phone_number="8776665544",
        first_name="John",
        last_name="Doe",
        airline="AA",
        flight_number="123",
        customer_special_instructions="I am from VCR testing",
    )
    response = service.start_reservation(request)
    assert response
    assert response.is_loading


@pytest.mark.vcr
def test_poll_reservation(service):
    response, more_coming = service.poll_reservation("187003663b8f4a5ca7c079e6df057cd3")
    assert response
    assert not more_coming
