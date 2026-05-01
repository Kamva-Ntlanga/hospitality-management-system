from enum import Enum
from datetime import date
from src.room import RoomStatus

class BookingStatus(Enum):
    PENDING = "Pending"
    CONFIRMED = "Confirmed"
    CHECKED_IN = "CheckedIn"
    COMPLETED = "Completed"
    CANCELLED = "Cancelled"

class Booking:
    def __init__(self, booking_id: str, guest, room, check_in_date: date, 
                 check_out_date: date, number_of_guests: int, special_requests: str = ""):
        self._booking_id = booking_id
        self._guest = guest
        self._room = room
        self._check_in_date = check_in_date
        self._check_out_date = check_out_date
        self._total_price = 0.0
        self._status = BookingStatus.PENDING
        self._number_of_guests = number_of_guests
        self._special_requests = special_requests
        self._payment = None

    def get_booking_id(self) -> str:
        return self._booking_id

    def get_guest(self):
        return self._guest

    def get_room(self):
        return self._room

    def get_check_in_date(self) -> date:
        return self._check_in_date

    def get_check_out_date(self) -> date:
        return self._check_out_date

    def get_total_price(self) -> float:
        return self._total_price

    def get_status(self) -> BookingStatus:
        return self._status

    def get_payment(self):
        return self._payment

    def calculate_total(self) -> float:
        nights = (self._check_out_date - self._check_in_date).days
        self._total_price = nights * self._room.get_price_per_night()
        return self._total_price

    def confirm_booking(self) -> bool:
        if self._status == BookingStatus.PENDING and self._room.is_available():
            self._status = BookingStatus.CONFIRMED
            self._room.update_status(RoomStatus.BOOKED)
            return True
        return False

    def cancel_booking(self) -> bool:
        if self._status in [BookingStatus.PENDING, BookingStatus.CONFIRMED]:
            self._status = BookingStatus.CANCELLED
            self._room.update_status(RoomStatus.AVAILABLE)
            return True
        return False

    def check_in(self) -> bool:
        if self._status == BookingStatus.CONFIRMED:
            self._status = BookingStatus.CHECKED_IN
            self._room.update_status(RoomStatus.OCCUPIED)
            return True
        return False

    def check_out(self) -> bool:
        if self._status == BookingStatus.CHECKED_IN:
            self._status = BookingStatus.COMPLETED
            self._room.update_status(RoomStatus.AVAILABLE)
            nights = (self._check_out_date - self._check_in_date).days
            self._guest.add_loyalty_points(nights * 10)
            return True
        return False

    def set_payment(self, payment):
        self._payment = payment
        if payment and payment.get_status().value == "Captured":
            self._status = BookingStatus.CONFIRMED

    def __str__(self) -> str:
        return f"Booking {self._booking_id}: {self._check_in_date} to {self._check_out_date} - {self._status.value}"
