from enum import Enum
from datetime import datetime

class RequestCategory(Enum):
    HOUSEKEEPING = "Housekeeping"
    ROOM_SERVICE = "RoomService"
    MAINTENANCE = "Maintenance"
    CONCIERGE = "Concierge"

class RequestStatus(Enum):
    SUBMITTED = "Submitted"
    ACKNOWLEDGED = "Acknowledged"
    IN_PROGRESS = "InProgress"
    COMPLETED = "Completed"
    ESCALATED = "Escalated"

class ServiceRequest:
    def __init__(self, request_id: str, guest, room, category: RequestCategory, description: str):
        self._request_id = request_id
        self._guest = guest
        self._room = room
        self._category = category
        self._description = description
        self._status = RequestStatus.SUBMITTED
        self._request_time = datetime.now()
        self._estimated_completion = None
        self._handled_by = None

    def get_request_id(self) -> str:
        return self._request_id

    def get_guest(self):
        return self._guest

    def get_room(self):
        return self._room

    def get_category(self) -> RequestCategory:
        return self._category

    def get_status(self) -> RequestStatus:
        return self._status

    def acknowledge(self) -> None:
        if self._status == RequestStatus.SUBMITTED:
            self._status = RequestStatus.ACKNOWLEDGED

    def start(self) -> None:
        if self._status == RequestStatus.ACKNOWLEDGED:
            self._status = RequestStatus.IN_PROGRESS

    def complete(self) -> None:
        if self._status == RequestStatus.IN_PROGRESS:
            self._status = RequestStatus.COMPLETED
            self._estimated_completion = datetime.now()

    def escalate(self) -> None:
        if self._status in [RequestStatus.SUBMITTED, RequestStatus.ACKNOWLEDGED, RequestStatus.IN_PROGRESS]:
            self._status = RequestStatus.ESCALATED

    def assign_handler(self, staff):
        self._handled_by = staff

    def __str__(self) -> str:
        return f"ServiceRequest {self._request_id}: {self._category.value} - {self._status.value}"
