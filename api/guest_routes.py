from fastapi import APIRouter, HTTPException, Depends, status
from typing import List
from pydantic import BaseModel

from services.guest_service import GuestService
from api.main import get_guest_service

router = APIRouter()

class GuestCreateRequest(BaseModel):
    guest_id: str
    first_name: str
    last_name: str
    email: str
    phone: str

class GuestUpdateRequest(BaseModel):
    first_name: str = None
    last_name: str = None
    phone: str = None

class GuestResponse(BaseModel):
    guest_id: str
    first_name: str
    last_name: str
    email: str
    phone: str
    loyalty_points: int

class AddPointsRequest(BaseModel):
    points: int

@router.get("/", response_model=List[GuestResponse])
async def get_all_guests(guest_service: GuestService = Depends(get_guest_service)):
    """Get all guests"""
    guests = guest_service.get_all_guests()
    return [
        {
            "guest_id": g.get_guest_id(),
            "first_name": g.get_first_name(),
            "last_name": g.get_last_name(),
            "email": g.get_email(),
            "phone": g.get_phone(),
            "loyalty_points": g.get_loyalty_points()
        }
        for g in guests
    ]

@router.get("/{guest_id}", response_model=GuestResponse)
async def get_guest(guest_id: str, guest_service: GuestService = Depends(get_guest_service)):
    """Get guest by ID"""
    try:
        guest = guest_service.get_guest(guest_id)
        return {
            "guest_id": guest.get_guest_id(),
            "first_name": guest.get_first_name(),
            "last_name": guest.get_last_name(),
            "email": guest.get_email(),
            "phone": guest.get_phone(),
            "loyalty_points": guest.get_loyalty_points()
        }
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.post("/", response_model=GuestResponse, status_code=status.HTTP_201_CREATED)
async def create_guest(request: GuestCreateRequest, guest_service: GuestService = Depends(get_guest_service)):
    """Create a new guest"""
    try:
        guest = guest_service.create_guest(
            request.guest_id, request.first_name, request.last_name,
            request.email, request.phone
        )
        return {
            "guest_id": guest.get_guest_id(),
            "first_name": guest.get_first_name(),
            "last_name": guest.get_last_name(),
            "email": guest.get_email(),
            "phone": guest.get_phone(),
            "loyalty_points": guest.get_loyalty_points()
        }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.put("/{guest_id}", response_model=GuestResponse)
async def update_guest(guest_id: str, request: GuestUpdateRequest,
                        guest_service: GuestService = Depends(get_guest_service)):
    """Update guest profile"""
    try:
        guest = guest_service.update_guest_profile(
            guest_id, request.first_name, request.last_name, request.phone
        )
        return {
            "guest_id": guest.get_guest_id(),
            "first_name": guest.get_first_name(),
            "last_name": guest.get_last_name(),
            "email": guest.get_email(),
            "phone": guest.get_phone(),
            "loyalty_points": guest.get_loyalty_points()
        }
    except ValueError as e:
        raise HTTPException(status_code=404 if "not found" in str(e) else 400, detail=str(e))

@router.post("/{guest_id}/points", response_model=GuestResponse)
async def add_loyalty_points(guest_id: str, request: AddPointsRequest,
                              guest_service: GuestService = Depends(get_guest_service)):
    """Add loyalty points to guest"""
    try:
        guest = guest_service.add_loyalty_points(guest_id, request.points)
        return {
            "guest_id": guest.get_guest_id(),
            "first_name": guest.get_first_name(),
            "last_name": guest.get_last_name(),
            "email": guest.get_email(),
            "phone": guest.get_phone(),
            "loyalty_points": guest.get_loyalty_points()
        }
    except ValueError as e:
        raise HTTPException(status_code=404 if "not found" in str(e) else 400, detail=str(e))

@router.delete("/{guest_id}")
async def delete_guest(guest_id: str, guest_service: GuestService = Depends(get_guest_service)):
    """Delete a guest"""
    try:
        guest_service.delete_guest(guest_id)
        return {"message": f"Guest {guest_id} deleted successfully"}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
