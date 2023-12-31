class ReservationFailed(Exception):
    def __init__(self) -> None:
        self.message = "Reservation failed. Please try again later or contact support."
        super().__init__(self.message)
