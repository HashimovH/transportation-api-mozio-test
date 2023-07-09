from pydantic import BaseModel
from typing import Optional
import enum


class MozioModes(enum.Enum):
    ONE_WAY = "one_way"
    ROUND_TRIP = "round_trip"
    HOURLY = "hourly"
    DATELESS = "dateless"
    DATELESS_ROUND_TRIP = "dateless_round_trip"


class MozioFlightTypes(enum.Enum):
    DOMESTIC = "domestic"
    INTERNATIONAL = "international"


class MozioReservationStatus(enum.Enum):
    PENDING = "pending"
    COMPLETED = "completed"
    FAILED = "failed"


class StartSearchProcessRequest(BaseModel):
    mode: MozioModes
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
    allow_delayed_flight_info: bool
    expires_at: int
    expires_in: int
    search_id: Optional[str]
    num_passengers: Optional[int]  # TODO: Should be positive >=1
    hourly_booking_duration: Optional[int] = 0
    flight_datetime: Optional[str]
    flight_type: Optional[MozioFlightTypes]
    pickup_datetime: Optional[str]


class StartSearchProcessResponse(SearchProcessResponseBase):
    results: Optional[list]


class PollSearchResponse(SearchProcessResponseBase):
    results: list
    allow_delayed_flight_info: Optional[bool]


class StartReservationResponse(BaseModel):
    status: MozioReservationStatus
    reservations: list


class PollReservationResponse(StartReservationResponse):
    pass


class CancelReservationResponse(BaseModel):
    refunded: int
    cancelled: int
