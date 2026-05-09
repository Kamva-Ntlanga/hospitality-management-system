from typing import List, Optional
from src.payment import Payment, PaymentStatus
from repositories.payment_repository import PaymentRepository
from repositories.inmemory.in_memory_base import InMemoryRepository

class InMemoryPaymentRepository(PaymentRepository):
    def __init__(self):
        self._storage = InMemoryRepository[Payment, str]()
    
    def save(self, entity: Payment) -> None:
        self._storage.save(entity, entity.get_payment_id())
    
    def find_by_id(self, id: str) -> Optional[Payment]:
        return self._storage.find_by_id(id)
    
    def find_all(self) -> List[Payment]:
        return self._storage.find_all()
    
    def delete(self, id: str) -> None:
        self._storage.delete(id)
    
    def exists(self, id: str) -> bool:
        return self._storage.exists(id)
    
    def count(self) -> int:
        return self._storage.count()
    
    def find_by_booking_id(self, booking_id: str) -> Optional[Payment]:
        for payment in self.find_all():
            booking = payment._booking
            if booking and booking.get_booking_id() == booking_id:
                return payment
        return None
    
    def find_by_status(self, status: PaymentStatus) -> List[Payment]:
        return [p for p in self.find_all() if p.get_status() == status]
    
    def clear(self):
        self._storage.clear()
