from typing import List, Optional
from datetime import date
from src.booking import Booking, BookingStatus
from repositories.booking_repository import BookingRepository
from repositories.inmemory.in_memory_base import InMemoryRepository

class InMemoryBookingRepository(BookingRepository):
    def __init__(self):
        self._storage = InMemoryRepository[Booking, str]()
    
    def save(self, entity: Booking) -> None:
        self._storage.save(entity, entity.get_booking_id())
    
    def find_by_id(self, id: str) -> Optional[Booking]:
        return self._storage.find_by_id(id)
    
    def find_all(self) -> List[Booking]:
        return self._storage.find_all()
    
    def delete(self, id: str) -> None:
        self._storage.delete(id)
    
    def exists(self, id: str) -> bool:
        return self._storage.exists(id)
    
    def count(self) -> int:
        return self._storage.count()
    
    def find_by_guest_id(self, guest_id: str) -> List[Booking]:
        return [b for b in self.find_all() if b.get_guest().get_guest_id() == guest_id]
    
    def find_by_room_id(self, room_id: str) -> List[Booking]:
        return [b for b in self.find_all() if b.get_room().get_room_id() == room_id]
    
    def find_by_date_range(self, start_date: date, end_date: date) -> List[Booking]:
        return [b for b in self.find_all() if start_date <= b.get_check_in_date() <= end_date]
    
    def find_upcoming_bookings(self) -> List[Booking]:
        today = date.today()
        return [b for b in self.find_all() if b.get_check_in_date() >= today and b.get_status() != BookingStatus.CANCELLED]
    
    def find_current_active_bookings(self) -> List[Booking]:
        return [b for b in self.find_all() if b.get_status() == BookingStatus.CHECKED_IN]
    
    def clear(self):
        self._storage.clear()
