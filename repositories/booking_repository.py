from typing import List, Optional, abstractmethod
from datetime import date
from repositories.repository_interface import Repository
from src.booking import Booking

class BookingRepository(Repository[Booking, str]):
    """Repository interface for Booking entities."""
    
    @abstractmethod
    def find_by_guest_id(self, guest_id: str) -> List[Booking]:
        """Find all bookings for a specific guest"""
        pass
    
    @abstractmethod
    def find_by_room_id(self, room_id: str) -> List[Booking]:
        """Find all bookings for a specific room"""
        pass
    
    @abstractmethod
    def find_by_date_range(self, start_date: date, end_date: date) -> List[Booking]:
        """Find bookings within a date range"""
        pass
    
    @abstractmethod
    def find_upcoming_bookings(self) -> List[Booking]:
        """Find all future bookings"""
        pass
    
    @abstractmethod
    def find_current_active_bookings(self) -> List[Booking]:
        """Find bookings currently checked in"""
        pass
