from enum import Enum
from datetime import datetime, timezone
from typing import Optional


class RequestCategory(Enum):
    HOUSEKEEPING = "HOUSEKEEPING"
    ROOM_SERVICE = "ROOM_SERVICE"
    MAINTENANCE = "MAINTENANCE"


class RequestStatus(Enum):
    PENDING = "PENDING"
    ASSIGNED = "ASSIGNED"
    ACKNOWLEDGED = "ASSIGNED"
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETED = "COMPLETED"
    CANCELLED = "CANCELLED"


class ServiceRequest:
    def __init__(
        self,
        request_id: str,
        guest=None,
        room=None,
        category: RequestCategory = None,
        special_instructions: str = "",
        guest_id: Optional[str] = None,
        room_number: Optional[str] = None,
    ):
        self._request_id = request_id
        self._guest = guest
        self._room = room
        self._guest_id = guest_id or self._extract_guest_id(guest)
        self._room_number = room_number or self._extract_room_number(room)
        self._category = category
        self._special_instructions = special_instructions or ""
        self._status = RequestStatus.PENDING
        self._estimated_completion_minutes = self.estimate_completion_minutes(category)
        self._created_at = datetime.now(timezone.utc)
        self._updated_at = self._created_at
        self._handled_by = None

    @staticmethod
    def estimate_completion_minutes(category: RequestCategory) -> int:
        estimates = {
            RequestCategory.HOUSEKEEPING: 15,
            RequestCategory.ROOM_SERVICE: 30,
            RequestCategory.MAINTENANCE: 45,
        }
        return estimates[category]

    @staticmethod
    def _extract_guest_id(guest) -> Optional[str]:
        if guest and hasattr(guest, "get_guest_id"):
            return guest.get_guest_id()
        return None

    @staticmethod
    def _extract_room_number(room) -> Optional[str]:
        if room and hasattr(room, "get_room_number"):
            return room.get_room_number()
        return None

    @staticmethod
    def _extract_room_id(room) -> Optional[str]:
        if room and hasattr(room, "get_room_id"):
            return room.get_room_id()
        return None

    def get_request_id(self) -> str:
        return self._request_id

    def get_guest(self):
        return self._guest

    def get_guest_id(self) -> Optional[str]:
        return self._guest_id

    def get_room(self):
        return self._room

    def get_room_id(self) -> Optional[str]:
        return self._extract_room_id(self._room) or self._room_number

    def get_room_number(self) -> Optional[str]:
        return self._room_number

    def get_category(self) -> RequestCategory:
        return self._category

    def get_special_instructions(self) -> str:
        return self._special_instructions

    def get_status(self) -> RequestStatus:
        return self._status

    def get_estimated_completion_minutes(self) -> int:
        return self._estimated_completion_minutes

    def get_created_at(self) -> datetime:
        return self._created_at

    def get_updated_at(self) -> datetime:
        return self._updated_at

    def acknowledge(self) -> None:
        if self._status == RequestStatus.PENDING:
            self._status = RequestStatus.ASSIGNED
            self._touch()

    def start(self) -> None:
        if self._status == RequestStatus.ASSIGNED:
            self._status = RequestStatus.IN_PROGRESS
            self._touch()

    def complete(self) -> None:
        if self._status == RequestStatus.IN_PROGRESS:
            self._status = RequestStatus.COMPLETED
            self._touch()

    def cancel(self) -> None:
        if self._status not in [RequestStatus.COMPLETED, RequestStatus.CANCELLED]:
            self._status = RequestStatus.CANCELLED
            self._touch()

    def assign_handler(self, staff):
        self._handled_by = staff
        self._touch()

    def _touch(self) -> None:
        self._updated_at = datetime.now(timezone.utc)

    def __str__(self) -> str:
        return f"ServiceRequest {self._request_id}: {self._category.value} - {self._status.value}"