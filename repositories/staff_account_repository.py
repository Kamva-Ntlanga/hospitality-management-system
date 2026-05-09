from typing import List, Optional, abstractmethod
from repositories.repository_interface import Repository
from src.staff_account import StaffAccount

class StaffAccountRepository(Repository[StaffAccount, str]):
    """Repository interface for StaffAccount entities."""
    
    @abstractmethod
    def find_by_username(self, username: str) -> Optional[StaffAccount]:
        """Find staff by username"""
        pass
    
    @abstractmethod
    def find_by_role(self, role: str) -> List[StaffAccount]:
        """Find all staff with a specific role"""
        pass
    
    @abstractmethod
    def find_active_staff(self) -> List[StaffAccount]:
        """Find all active staff accounts"""
        pass
