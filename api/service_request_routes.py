from enum import Enum
from typing import List, Optional

from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, Field

from services.service_request_service import ServiceRequestService
from src.service_request import RequestCategory

router = APIRouter()


class RequestCategoryEnum(str, Enum):
    HOUSEKEEPING = "HOUSEKEEPING"
    ROOM_SERVICE = "ROOM_SERVICE"
    MAINTENANCE = "MAINTENANCE"


class ServiceRequestCreateRequest(BaseModel):
    guestId: str = Field(..., min_length=1)
    roomNumber: str = Field(..., min_length=1)
    category: RequestCategoryEnum
    specialInstructions: Optional[str] = ""


class ServiceRequestResponse(BaseModel):
    id: str
    guestId: str
    roomNumber: str
    category: str
    specialInstructions: str
    status: str
    estimatedCompletionMinutes: int
    staffNotification: str


def _notification_for(service_request) -> str:
    return (
        f"New {service_request.get_category().value} request "
        f"for room {service_request.get_room_number()}"
    )


def _to_response(service_request) -> dict:
    return {
        "id": service_request.get_request_id(),
        "guestId": service_request.get_guest_id(),
        "roomNumber": service_request.get_room_number(),
        "category": service_request.get_category().value,
        "specialInstructions": service_request.get_special_instructions(),
        "status": service_request.get_status().value,
        "estimatedCompletionMinutes": service_request.get_estimated_completion_minutes(),
        "staffNotification": _notification_for(service_request),
    }


@router.post("/", response_model=ServiceRequestResponse, status_code=status.HTTP_201_CREATED)
async def create_service_request(request: ServiceRequestCreateRequest):
    """Create a guest service request and notify staff internally."""
    from api.main import get_service_request_service

    service_request_service: ServiceRequestService = get_service_request_service()
    try:
        service_request = service_request_service.create_service_request(
            guest_id=request.guestId,
            room_number=request.roomNumber,
            category=RequestCategory[request.category.value],
            special_instructions=request.specialInstructions or "",
        )
        return _to_response(service_request)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/", response_model=List[ServiceRequestResponse])
async def get_all_service_requests():
    """Get all guest service requests."""
    from api.main import get_service_request_service

    service_request_service: ServiceRequestService = get_service_request_service()
    return [_to_response(r) for r in service_request_service.get_all_service_requests()]


@router.get("/{request_id}", response_model=ServiceRequestResponse)
async def get_service_request(request_id: str):
    """Get a guest service request by ID."""
    from api.main import get_service_request_service

    service_request_service: ServiceRequestService = get_service_request_service()
    try:
        return _to_response(service_request_service.get_service_request(request_id))
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))