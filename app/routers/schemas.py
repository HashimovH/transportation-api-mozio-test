from typing import Optional

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


class Vehicle(BaseModel):
    image_url: Optional[str]
    vehicle_type: Optional[str]
    max_bags: Optional[int]
    max_bags_for_each_passenger: Optional[bool]
    max_passengers: Optional[int]
    category: Optional[str]
    num_vehicles: Optional[int]
    model: Optional[str]
    make: Optional[str]
    vehicle_class: Optional[str]


class SearchResultResponseProvider(BaseModel):
    name: str
    display_name: str
    logo_url: str
    rating: float
    rating_count: int


class SearchResultReponse(BaseModel):
    result_id: str
    vehicle_id: str
    good_to_know_into: str
    tags: Optional[list]
    price: str
    price_currency: str
    description: str
    vehicle: Optional[Vehicle]
    time: int
    provider: Optional[SearchResultResponseProvider]
    can_cancel_online: bool
    can_cancel_offline: bool
    can_amend: bool
    cancel_notice: int
    cancel_refund_percent: int
    departure_time: str
    wait_time_minutes: int
    amenities: list
    alternative_departure_time: Optional[str]
    alternative_arrival_time: Optional[str]
    needs_flight_info: bool
    notes: Optional[str]
    terms: Optional[str]
    can_booked: bool


class SearchResultsResponseList(BaseModel):
    results: list[SearchResultReponse]
    is_loading: bool
