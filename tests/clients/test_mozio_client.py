import pytest

from app.clients.mozio.mozio_client import MozioClient


@pytest.fixture(scope="session")
def client():
    return MozioClient("https://api-testing.mozio.com/v2/", "6bd1e15ab9e94bb190074b4209e6b6f9")


@pytest.mark.vcr
def test_start_search(client):
    request = {
        "start_address": "44 Tehama Street, San Francisco, CA, USA",
        "end_address": "SFO",
        "mode": "one_way",
        "pickup_datetime": "2023-12-01 15:30",
        "num_passengers": 2,
        "currency": "USD",
        "campaign": "Hashim Hashimov"
    }
    response = client.start_search(request)
    assert response
    assert response.currency_info.code == "USD"
    assert response.more_coming
    assert response.start_location.full_address == "44 Tehama Street, San Francisco, CA, USA"
    assert response.end_location.formatted_address == "San Francisco International Airport"
    assert response.num_passengers == 2


@pytest.mark.vcr
def test_poll_search(client):
    search_id = "d1e0c6e8526046d8b73d7ce3c44b5403"
    response = client.poll_search(search_id)
    assert response
    assert response.currency_info.code == "USD"
    assert not response.more_coming
    assert response.start_location.full_address == "44 Tehama Street, San Francisco, CA, USA"
    assert response.end_location.formatted_address == "San Francisco International Airport"
    assert response.num_passengers == 2
    assert len(response.results) > 1


@pytest.mark.vcr
def test_start_reservation(client):
    request = {
        "search_id": "d1e0c6e8526046d8b73d7ce3c44b5403",
        "result_id": "0065652958e49ffe698cca03fdf8c9e4",
        "email": "pytest@gmail.com",
        "country_code_name": "US",
        "phone_number": "8776665544",
        "first_name": "John",
        "last_name": "Doe",
        "airline": "AA",
        "flight_number": "123",
        "customer_special_instructions": "I am from VCR testing"
    }
    response = client.start_reservation(request)
    assert response
    assert response.status.value == "pending"
    assert response.reservations == []


@pytest.mark.vcr
def test_poll_reservation(client):
    search_id = "d1e0c6e8526046d8b73d7ce3c44b5403"
    response = client.poll_reservation(search_id)
    assert response
    assert response.status.value == "completed"
    assert len(response.reservations) > 0


@pytest.mark.vcr
def test_cancel_reservation(client):
    reservation_id = "2a0ca06bb2fa482c9d7fe56f0671fee8"
    response = client.cancel_reservation(reservation_id)
    assert response
    assert response.cancelled == 1
    assert response.refunded == 1
