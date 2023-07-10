from typing import Optional

from pydantic import BaseModel

from app.clients.mozio.schemas.common import MozioFlightTypes


class StartSearchProcessRequest(BaseModel):
    mode: str
    start_address: str
    end_address: str
    pickup_datetime: str
    num_passengers: int
    currency: str
    campaign: Optional[str]


class StartSearchProcessResponseCurrencyInfo(BaseModel):
    code: Optional[str]
    prefix_symbol: Optional[str]
    suffix_symbol: Optional[str]


class StartSearchProcessResponseLocation(BaseModel):
    formatted_address: str
    full_address: str
    iata_code: Optional[str]
    icao_code: Optional[str]
    lat: float
    lng: float
    place_id: Optional[str]
    timezone: str


class SearchProcessResponseBase(BaseModel):
    created_at: int
    currency_info: StartSearchProcessResponseCurrencyInfo
    end_location: StartSearchProcessResponseLocation
    start_location: StartSearchProcessResponseLocation
    more_coming: bool
    allow_delayed_flight_info: Optional[bool]
    expires_at: int
    expires_in: int
    search_id: Optional[str]
    num_passengers: Optional[int]
    hourly_booking_duration: Optional[int] = 0
    flight_datetime: Optional[str]
    flight_type: Optional[MozioFlightTypes]
    pickup_datetime: Optional[str]


class SearchResultTotalPrice(BaseModel):
    value: str
    display: str
    compact: str


class SearchResultTotalPriceBase(BaseModel):
    total_price: Optional[SearchResultTotalPrice]


class SearchResultStepsDetailsVehicle(BaseModel):
    image: Optional[str]
    vehicle_type: Optional[dict]
    max_bags: Optional[int]
    is_max_bags_per_person: Optional[bool]
    max_passengers: Optional[int]
    category: Optional[dict]
    num_vehicles: Optional[int]
    total_bags: Optional[int]
    model: Optional[str]
    make: Optional[str]
    vehicle_class: Optional[int]
    vehicle_class_detail: Optional[dict]


class SearchResultStepsDetailsProvider(BaseModel):
    name: str
    display_name: str
    logo_url: str
    rating: int
    rating_count: int
    rating_with_decimals: str


class SearchResultStepsDetailsCancellation(BaseModel):
    cancellable_online: Optional[bool]
    cancellable_offline: Optional[bool]
    amendable: Optional[bool]
    policy: Optional[list]


class SearchResultStepsDetails(BaseModel):
    description: Optional[str]
    vehicle: Optional[SearchResultStepsDetailsVehicle]
    time: Optional[int]
    provider: Optional[SearchResultStepsDetailsProvider]
    provider_name: Optional[str]
    price: Optional[SearchResultTotalPriceBase]
    cancellation: Optional[SearchResultStepsDetailsCancellation]
    departure_datetime: Optional[str]
    wait_time: Optional[dict]
    amenities: Optional[list]
    ticket_types: Optional[list]
    flight_info_required: Optional[bool]
    extra_pax_required: Optional[bool]
    notes: Optional[str]
    terms_url: Optional[str]
    bookable: Optional[bool]
    alternative_times: Optional[dict]


class SearchResultSteps(BaseModel):
    main: bool
    step_type: str
    details: SearchResultStepsDetails


class SearchResult(BaseModel):
    result_id: str
    vehicle_id: str
    good_to_know_info: str
    total_price: SearchResultTotalPriceBase
    tags: Optional[list]
    steps: list[SearchResultSteps]


class StartSearchProcessResponse(SearchProcessResponseBase):
    results: Optional[list]


class PollSearchResponse(SearchProcessResponseBase):
    results: list[SearchResult]
