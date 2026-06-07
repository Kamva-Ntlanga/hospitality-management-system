from fastapi import APIRouter, HTTPException, Depends, status
from typing import List
from pydantic import BaseModel
from datetime import date

from services.booking_service import BookingService

router = APIRouter()

class BookingCreateRequest(BaseModel):
    booking_id: str
    guest_id: str
    room_id: str
    check_in_date: date
    check_out_date: date
    number_of_guests: int
    special_requests: str = ""

class BookingResponse(BaseModel):
    booking_id: str
    guest_id: str
    room_id: str
    check_in_date: date
    check_out_date: date
    total_price: float
    status: str
    number_of_guests: int

@router.get("/", response_model=List[BookingResponse])
async def get_all_bookings():
    """Get all bookings"""
    from api.main import get_booking_service
    booking_service: BookingService = get_booking_service()
    bookings = booking_service.get_all_bookings()
    return [
        {
            "booking_id": b.get_booking_id(),
            "guest_id": b.get_guest().get_guest_id(),
            "room_id": b.get_room().get_room_id(),
            "check_in_date": b.get_check_in_date(),
            "check_out_date": b.get_check_out_date(),
            "total_price": b.get_total_price(),
            "status": b.get_status().value,
            "number_of_guests": b._number_of_guests
        }
        for b in bookings
    ]

@router.post("/", response_model=BookingResponse, status_code=status.HTTP_201_CREATED)
async def create_booking(request: BookingCreateRequest):
    """Create a new booking"""
    from api.main import get_booking_service
    booking_service: BookingService = get_booking_service()
    try:
        booking = booking_service.create_booking(
            request.booking_id, request.guest_id, request.room_id,
            request.check_in_date, request.check_out_date,
            request.number_of_guests, request.special_requests
        )
        return {
            "booking_id": booking.get_booking_id(),
            "guest_id": booking.get_guest().get_guest_id(),
            "room_id": booking.get_room().get_room_id(),
            "check_in_date": booking.get_check_in_date(),
            "check_out_date": booking.get_check_out_date(),
            "total_price": booking.get_total_price(),
            "status": booking.get_status().value,
            "number_of_guests": booking._number_of_guests
        }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{booking_id}", response_model=BookingResponse)
async def get_booking(booking_id: str):
    """Get booking by ID"""
    from api.main import get_booking_service
    booking_service: BookingService = get_booking_service()
    try:
        booking = booking_service.get_booking(booking_id)
        return {
            "booking_id": booking.get_booking_id(),
            "guest_id": booking.get_guest().get_guest_id(),
            "room_id": booking.get_room().get_room_id(),
            "check_in_date": booking.get_check_in_date(),
            "check_out_date": booking.get_check_out_date(),
            "total_price": booking.get_total_price(),
            "status": booking.get_status().value,
            "number_of_guests": booking._number_of_guests
        }
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.post("/{booking_id}/confirm", response_model=BookingResponse)
async def confirm_booking(booking_id: str):
    """Confirm a booking"""
    from api.main import get_booking_service
    booking_service: BookingService = get_booking_service()
    try:
        booking = booking_service.confirm_booking(booking_id)
        return {
            "booking_id": booking.get_booking_id(),
            "guest_id": booking.get_guest().get_guest_id(),
            "room_id": booking.get_room().get_room_id(),
            "check_in_date": booking.get_check_in_date(),
            "check_out_date": booking.get_check_out_date(),
            "total_price": booking.get_total_price(),
            "status": booking.get_status().value,
            "number_of_guests": booking._number_of_guests
        }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/{booking_id}/cancel", response_model=BookingResponse)
async def cancel_booking(booking_id: str):
    """Cancel a booking"""
    from api.main import get_booking_service
    booking_service: BookingService = get_booking_service()
    try:
        booking = booking_service.cancel_booking(booking_id)
        return {
            "booking_id": booking.get_booking_id(),
            "guest_id": booking.get_guest().get_guest_id(),
            "room_id": booking.get_room().get_room_id(),
            "check_in_date": booking.get_check_in_date(),
            "check_out_date": booking.get_check_out_date(),
            "total_price": booking.get_total_price(),
            "status": booking.get_status().value,
            "number_of_guests": booking._number_of_guests
        }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/{booking_id}/checkin", response_model=BookingResponse)
async def check_in(booking_id: str):
    """Process check-in"""
    from api.main import get_booking_service
    booking_service: BookingService = get_booking_service()
    try:
        booking = booking_service.check_in(booking_id)
        return {
            "booking_id": booking.get_booking_id(),
            "guest_id": booking.get_guest().get_guest_id(),
            "room_id": booking.get_room().get_room_id(),
            "check_in_date": booking.get_check_in_date(),
            "check_out_date": booking.get_check_out_date(),
            "total_price": booking.get_total_price(),
            "status": booking.get_status().value,
            "number_of_guests": booking._number_of_guests
        }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/{booking_id}/checkout", response_model=BookingResponse)
async def check_out(booking_id: str):
    """Process check-out"""
    from api.main import get_booking_service
    booking_service: BookingService = get_booking_service()
    try:
        booking = booking_service.check_out(booking_id)
        return {
            "booking_id": booking.get_booking_id(),
            "guest_id": booking.get_guest().get_guest_id(),
            "room_id": booking.get_room().get_room_id(),
            "check_in_date": booking.get_check_in_date(),
            "check_out_date": booking.get_check_out_date(),
            "total_price": booking.get_total_price(),
            "status": booking.get_status().value,
            "number_of_guests": booking._number_of_guests
        }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))