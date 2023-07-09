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
