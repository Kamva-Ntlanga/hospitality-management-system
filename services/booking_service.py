from typing import List, Optional
from datetime import date, timedelta
from src.booking import Booking, BookingStatus
from src.room import RoomStatus
from src.payment import Payment, PaymentMethod
from repositories.booking_repository import BookingRepository
from repositories.room_repository import RoomRepository
from repositories.guest_repository import GuestRepository

class BookingService:
    """Business logic for Booking operations"""
    
    def __init__(self, booking_repository: BookingRepository,
                 room_repository: RoomRepository,
                 guest_repository: GuestRepository):
        self.booking_repo = booking_repository
        self.room_repo = room_repository
        self.guest_repo = guest_repository
    
    def create_booking(self, booking_id: str, guest_id: str, room_id: str,
                       check_in_date: date, check_out_date: date,
                       number_of_guests: int, special_requests: str = "") -> Booking:
        """Create a new booking"""
        # Business rule: Check-in must be before check-out
        if check_in_date >= check_out_date:
            raise ValueError("Check-in must be before check-out")
        
        # Business rule: Check-in cannot be in the past
        if check_in_date < date.today():
            raise ValueError("Check-in cannot be in the past")
        
        # Business rule: Max booking duration is 30 days
        if (check_out_date - check_in_date).days > 30:
            raise ValueError("Booking cannot exceed 30 days")
        
        # Get guest and room
        guest = self.guest_repo.find_by_id(guest_id)
        if not guest:
            raise ValueError(f"Guest with ID {guest_id} not found")
        
        room = self.room_repo.find_by_id(room_id)
        if not room:
            raise ValueError(f"Room with ID {room_id} not found")
        
        # Business rule: Room must be available
        if not room.is_available():
            raise ValueError(f"Room {room_id} is not available")
        
        # Business rule: Number of guests cannot exceed room capacity
        if number_of_guests > room.get_max_guests():
            raise ValueError(f"Room can only accommodate {room.get_max_guests()} guests")
        
        # Check for overlapping bookings
        existing = self.booking_repo.find_by_room_id(room_id)
        for booking in existing:
            if booking.get_status() not in [BookingStatus.CANCELLED, BookingStatus.COMPLETED]:
                if not (check_out_date <= booking.get_check_in_date() or
                        check_in_date >= booking.get_check_out_date()):
                    raise ValueError(f"Room already booked for these dates")
        
        booking = Booking(booking_id, guest, room, check_in_date, check_out_date,
                         number_of_guests, special_requests)
        booking.calculate_total()
        self.booking_repo.save(booking)
        return booking
    
    def get_booking(self, booking_id: str) -> Booking:
        """Get booking by ID"""
        booking = self.booking_repo.find_by_id(booking_id)
        if not booking:
            raise ValueError(f"Booking with ID {booking_id} not found")
        return booking
    
    def get_all_bookings(self) -> List[Booking]:
        """Get all bookings"""
        return self.booking_repo.find_all()
    
    def confirm_booking(self, booking_id: str) -> Booking:
        """Confirm a booking"""
        booking = self.get_booking(booking_id)
        if not booking.confirm_booking():
            raise ValueError(f"Cannot confirm booking {booking_id}")
        self.booking_repo.save(booking)
        return booking
    
    def cancel_booking(self, booking_id: str) -> Booking:
        """Cancel a booking"""
        booking = self.get_booking(booking_id)
        if not booking.cancel_booking():
            raise ValueError(f"Cannot cancel booking {booking_id}")
        self.booking_repo.save(booking)
        return booking
    
    def check_in(self, booking_id: str) -> Booking:
        """Process check-in"""
        booking = self.get_booking(booking_id)
        if not booking.check_in():
            raise ValueError(f"Cannot check in booking {booking_id}")
        self.booking_repo.save(booking)
        return booking
    
    def check_out(self, booking_id: str) -> Booking:
        """Process check-out"""
        booking = self.get_booking(booking_id)
        if not booking.check_out():
            raise ValueError(f"Cannot check out booking {booking_id}")
        self.booking_repo.save(booking)
        return booking
    
    def get_bookings_by_guest(self, guest_id: str) -> List[Booking]:
        """Get all bookings for a guest"""
        return self.booking_repo.find_by_guest_id(guest_id)
    
    def get_upcoming_bookings(self) -> List[Booking]:
        """Get all upcoming bookings"""
        return self.booking_repo.find_upcoming_bookings()
