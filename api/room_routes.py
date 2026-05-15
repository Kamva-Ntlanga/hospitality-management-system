from fastapi import APIRouter, HTTPException, Depends, status
from typing import List
from pydantic import BaseModel
from enum import Enum

from services.room_service import RoomService
from api.main import get_room_service
from src.room import RoomType, RoomStatus

router = APIRouter()

# Pydantic models for request/response
class RoomTypeEnum(str, Enum):
    STANDARD = "Standard"
    DELUXE = "Deluxe"
    SUITE = "Suite"

class RoomStatusEnum(str, Enum):
    AVAILABLE = "Available"
    BOOKED = "Booked"
    OCCUPIED = "Occupied"
    MAINTENANCE = "Maintenance"

class RoomCreateRequest(BaseModel):
    room_id: str
    room_number: str
    room_type: RoomTypeEnum
    price_per_night: float
    floor: int
    max_guests: int

class RoomUpdateStatusRequest(BaseModel):
    status: RoomStatusEnum

class RoomResponse(BaseModel):
    room_id: str
    room_number: str
    room_type: str
    price_per_night: float
    status: str
    floor: int
    max_guests: int

@router.get("/", response_model=List[RoomResponse])
async def get_all_rooms(room_service: RoomService = Depends(get_room_service)):
    """Get all rooms"""
    rooms = room_service.get_all_rooms()
    return [
        {
            "room_id": r.get_room_id(),
            "room_number": r.get_room_number(),
            "room_type": r.get_room_type().value,
            "price_per_night": r.get_price_per_night(),
            "status": r.get_status().value,
            "floor": r.get_floor(),
            "max_guests": r.get_max_guests()
        }
        for r in rooms
    ]

@router.get("/available", response_model=List[RoomResponse])
async def get_available_rooms(room_service: RoomService = Depends(get_room_service)):
    """Get all available rooms"""
    rooms = room_service.get_available_rooms()
    return [
        {
            "room_id": r.get_room_id(),
            "room_number": r.get_room_number(),
            "room_type": r.get_room_type().value,
            "price_per_night": r.get_price_per_night(),
            "status": r.get_status().value,
            "floor": r.get_floor(),
            "max_guests": r.get_max_guests()
        }
        for r in rooms
    ]

@router.get("/{room_id}", response_model=RoomResponse)
async def get_room(room_id: str, room_service: RoomService = Depends(get_room_service)):
    """Get room by ID"""
    try:
        room = room_service.get_room(room_id)
        return {
            "room_id": room.get_room_id(),
            "room_number": room.get_room_number(),
            "room_type": room.get_room_type().value,
            "price_per_night": room.get_price_per_night(),
            "status": room.get_status().value,
            "floor": room.get_floor(),
            "max_guests": room.get_max_guests()
        }
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.post("/", response_model=RoomResponse, status_code=status.HTTP_201_CREATED)
async def create_room(request: RoomCreateRequest, room_service: RoomService = Depends(get_room_service)):
    """Create a new room"""
    try:
        room_type = RoomType(request.room_type.value)
        room = room_service.create_room(
            request.room_id, request.room_number, room_type,
            request.price_per_night, request.floor, request.max_guests
        )
        return {
            "room_id": room.get_room_id(),
            "room_number": room.get_room_number(),
            "room_type": room.get_room_type().value,
            "price_per_night": room.get_price_per_night(),
            "status": room.get_status().value,
            "floor": room.get_floor(),
            "max_guests": room.get_max_guests()
        }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.put("/{room_id}/status", response_model=RoomResponse)
async def update_room_status(room_id: str, request: RoomUpdateStatusRequest,
                              room_service: RoomService = Depends(get_room_service)):
    """Update room status"""
    try:
        new_status = RoomStatus(request.status.value)
        room = room_service.update_room_status(room_id, new_status)
        return {
            "room_id": room.get_room_id(),
            "room_number": room.get_room_number(),
            "room_type": room.get_room_type().value,
            "price_per_night": room.get_price_per_night(),
            "status": room.get_status().value,
            "floor": room.get_floor(),
            "max_guests": room.get_max_guests()
        }
    except ValueError as e:
        raise HTTPException(status_code=404 if "not found" in str(e) else 400, detail=str(e))

@router.delete("/{room_id}")
async def delete_room(room_id: str, room_service: RoomService = Depends(get_room_service)):
    """Delete a room"""
    try:
        room_service.delete_room(room_id)
        return {"message": f"Room {room_id} deleted successfully"}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
