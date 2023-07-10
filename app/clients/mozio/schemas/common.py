import enum


class MozioFlightTypes(enum.Enum):
    DOMESTIC = "domestic"
    INTERNATIONAL = "international"


class MozioReservationStatus(enum.Enum):
    PENDING = "pending"
    COMPLETED = "completed"
    FAILED = "failed"
