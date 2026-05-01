from enum import Enum
from datetime import date

class RoomStatus(Enum):
    AVAILABLE = "Available"
    BOOKED = "Booked"
    OCCUPIED = "Occupied"
    MAINTENANCE = "Maintenance"

class RoomType(Enum):
    STANDARD = "Standard"
    DELUXE = "Deluxe"
    SUITE = "Suite"

class Room:
    def __init__(self, room_id: str, room_number: str, room_type: RoomType, 
                 price_per_night: float, floor: int, max_guests: int):
        self._room_id = room_id
        self._room_number = room_number
        self._room_type = room_type
        self._price_per_night = price_per_night
        self._status = RoomStatus.AVAILABLE
        self._floor = floor
        self._max_guests = max_guests

    def get_room_id(self) -> str:
        return self._room_id

    def get_room_number(self) -> str:
        return self._room_number

    def get_room_type(self) -> RoomType:
        return self._room_type

    def get_price_per_night(self) -> float:
        return self._price_per_night

    def get_status(self) -> RoomStatus:
        return self._status

    def get_floor(self) -> int:
        return self._floor

    def get_max_guests(self) -> int:
        return self._max_guests

    def update_status(self, new_status: RoomStatus) -> None:
        self._status = new_status

    def is_available(self) -> bool:
        return self._status == RoomStatus.AVAILABLE

    def get_price_for_dates(self, check_in: date, check_out: date) -> float:
        nights = (check_out - check_in).days
        return nights * self._price_per_night

    def __str__(self) -> str:
        return f"Room {self._room_number} ({self._room_type.value}) - {self._status.value}"
