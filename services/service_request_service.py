from typing import List, Optional
from uuid import uuid4

from repositories.service_request_repository import ServiceRequestRepository
from src.service_request import RequestCategory, ServiceRequest


class StaffNotificationService:
    """Lightweight internal notification placeholder for staff-facing alerts."""

    def __init__(self):
        self._notifications: List[str] = []

    def notify_new_request(self, service_request: ServiceRequest) -> str:
        message = (
            f"New {service_request.get_category().value} request "
            f"for room {service_request.get_room_number()}"
        )
        self._notifications.append(message)
        return message

    def get_notifications(self) -> List[str]:
        return list(self._notifications)


class ServiceRequestService:
    """Business logic for guest service request operations."""

    def __init__(
        self,
        service_request_repository: ServiceRequestRepository,
        notification_service: Optional[StaffNotificationService] = None,
    ):
        self.service_request_repo = service_request_repository
        self.notification_service = notification_service or StaffNotificationService()

    def create_service_request(
        self,
        guest_id: str,
        room_number: str,
        category: RequestCategory,
        special_instructions: str = "",
        request_id: Optional[str] = None,
    ) -> ServiceRequest:
        if not guest_id or not guest_id.strip():
            raise ValueError("guestId is required")

        if not room_number or not room_number.strip():
            raise ValueError("roomNumber is required")

        if not isinstance(category, RequestCategory):
            raise ValueError("category must be a valid service request category")

        service_request = ServiceRequest(
            request_id=request_id or str(uuid4()),
            guest_id=guest_id.strip(),
            room_number=room_number.strip(),
            category=category,
            special_instructions=special_instructions,
        )
        self.service_request_repo.save(service_request)
        self.notification_service.notify_new_request(service_request)
        return service_request

    def get_service_request(self, request_id: str) -> ServiceRequest:
        service_request = self.service_request_repo.find_by_id(request_id)
        if not service_request:
            raise ValueError(f"Service request with ID {request_id} not found")
        return service_request

    def get_all_service_requests(self) -> List[ServiceRequest]:
        return self.service_request_repo.find_all()

    def get_staff_notifications(self) -> List[str]:
        return self.notification_service.get_notifications()
