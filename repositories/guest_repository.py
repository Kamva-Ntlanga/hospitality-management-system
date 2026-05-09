from typing import List, Optional, abstractmethod
from repositories.repository_interface import Repository
from src.guest import Guest

class GuestRepository(Repository[Guest, str]):
    """Repository interface for Guest entities."""
    
    @abstractmethod
    def find_by_email(self, email: str) -> Optional[Guest]:
        """Find a guest by email address"""
        pass
    
    @abstractmethod
    def find_by_loyalty_points_range(self, min_points: int, max_points: int) -> List[Guest]:
        """Find guests with loyalty points in range"""
        pass
