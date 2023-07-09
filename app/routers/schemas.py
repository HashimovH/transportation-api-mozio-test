from pydantic import BaseModel


class StartSearchAPIRequest(BaseModel):
    start_address: str
    end_address: str
    mode: str
    pickup_datetime: str
    num_passengers: int
    currency: str
    campaign: str


class StartOperationsAPIResponse(BaseModel):
    is_loading: bool


class StartReservationAPIRequest(BaseModel):
    search_id: str
    result_id: str
    email: str
    country_code_name: str
    phone_number: str
    first_name: str
    last_name: str
    airline: str
    flight_number: str
    customer_special_instructions: str


class CancelReservationAPIResponse(BaseModel):
    refunded: bool
    cancelled: bool
