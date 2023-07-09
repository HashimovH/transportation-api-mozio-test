from pydantic import BaseModel
from typing import Any, Optional
from app.clients.mozio.schemas.common import MozioReservationStatus


class Provider(BaseModel):
    id: int
    uid: str
    name: str
    is_active: bool
    url: Optional[str]
    report_currency: Optional[str]
    email: str
    phone_number: str
    logo_url: str
    rating: int
    options: dict[str, Any]
    description: Optional[str]
    has_terms: bool


class Vehicle(BaseModel):
    type: str
    max_passengers: int
    max_bags: int
    is_max_bags_per_person: bool
    image_url: str
    category: str
    key: int
    num_vehicles: int
    make: str
    model: str
    vehicle_class: int
    vehicle_class_detail: dict
    total_bags: int


class StepDetailsProvider(BaseModel):
    id: int
    uid: str
    name: str
    is_active: bool
    url: Optional[str]
    report_currency: str
    email: str
    phone_number: str
    logo_url: str
    rating: int
    options: dict[str, Any]
    description: Optional[str]
    has_terms: bool
    rating_count: int
    rating_with_decimals: str
    display_name: str
    supplier_score: Optional[str]


class StepDetailsVehicleType(BaseModel):
    key: int
    name: str


class StepDetails(BaseModel):
    description: Optional[str]
    vehicle: Optional[Vehicle]
    time: Optional[int]
    departure_datetime: Optional[str]
    notes: Optional[str]
    provider: Optional[StepDetailsProvider]
    provider_name: Optional[str]
    price: Optional[dict[str, Any]]
    cancellation: Optional[dict]
    wait_time: Optional[dict[str, Any]]
    amenities: Optional[list[dict[str, Any]]]
    ticket_types: Optional[list[dict[str, Any]]]
    flight_info_required: Optional[bool]
    extra_pax_required: Optional[bool]
    terms_url: Optional[str]
    bookable: Optional[bool]


class Voyage(BaseModel):
    flight_datetime: str
    departure_datetime: str
    arrival_datetime: str
    alternative_times: list[str]
    alternative_time_index: int
    num_passengers: int
    service_type: int
    meet_and_greet_chosen: bool
    currency: str
    booking_details: Optional[dict[str, Any]]
    start_location: dict
    end_location: dict
    vehicle: Optional[Vehicle]
    provider_currency: str
    provider_phone: str
    provider_email: str
    start_difference: float
    end_difference: float
    steps: list[StepDetails]
    ticket_data: Optional[dict[str, Any]]
    ticket_types: Optional[list[dict[str, Any]]]
    pass_types: Optional[list[dict[str, Any]]]
    amenities: Optional[list[dict[str, Any]]]
    hourly_details: dict[str, Any]
    flt_support: bool


class ExtraTripOffer(BaseModel):
    extra_trip_search_link: str
    extra_trip_iata_code: str
    trip_direction: str
    extra_trip_coupon_percentage: int
    extra_trip_coupon_code: str


class Offers(BaseModel):
    extra_trip_offer: Optional[ExtraTripOffer]


class PollReservationResponseReservation(BaseModel):
    url: str
    id: str
    amount_paid: str
    gratuity: str
    pickup_instructions: str
    mobile_pickup_instructions: Optional[str]
    confirmation_number: str
    service_instructions: dict[str, Any]
    ticket_url: str
    voyage: Voyage
    can_cancel: bool
    mozio_profit_usd: str
    partner_profit_usd: str
    gross_revenue_usd: str
    mozio_profit: str
    partner_profit: str
    gross_revenue: str
    credit_card: dict[str, Any]
    campaign: str
    branch: str
    cancelled: bool
    timestamp: str
    cancelled_timestamp: str
    rebooked_id: Optional[str]
    total_price: dict[str, Any]
    vat_amount: Optional[dict[str, Any]]
    nonrefundable_amount: dict[str, Any]
    phone_number_national: int
    phone_number_country_code_name: str
    is_delayed_flight_info: bool
    offers: Offers
    has_passed: bool
    currency: str
    provider: Optional[Provider]
    email: Optional[str]
    phone_number: Optional[str]
    first_name: Optional[str]
    last_name: Optional[str]
    airline: Optional[str]
    flight_number: Optional[str]
    airport_terminal: Optional[str]
    pickup_time_buffer: Optional[dict[str, Any]]
    customer_special_instructions: Optional[str]
    partner_tracking_id: Optional[str]
    consent_for_contact: Optional[bool]
    extra_pax_info: Optional[list[dict[str, Any]]]
    cruise_line: Optional[str]
    ship_name: Optional[str]
    train_company: Optional[str]
    train_number: Optional[str]
    return_train_company: Optional[str]
    return_train_number: Optional[str]
    flight_type: Optional[str]
    google_analytics_client_id: Optional[str]
    loyalty: Optional[dict[str, Any]]


class StartReservationResponse(BaseModel):
    status: MozioReservationStatus
    reservations: Optional[list]


class PollReservationResponse(StartReservationResponse):
    reservations: list[PollReservationResponseReservation]


class CancelReservationResponse(BaseModel):
    refunded: int
    cancelled: int
