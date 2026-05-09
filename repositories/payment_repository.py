from typing import List, Optional, abstractmethod
from repositories.repository_interface import Repository
from src.payment import Payment

class PaymentRepository(Repository[Payment, str]):
    """Repository interface for Payment entities."""
    
    @abstractmethod
    def find_by_booking_id(self, booking_id: str) -> Optional[Payment]:
        """Find payment for a specific booking"""
        pass
    
    @abstractmethod
    def find_by_status(self, status: str) -> List[Payment]:
        """Find payments by status (Pending, Captured, Refunded, etc.)"""
        pass
