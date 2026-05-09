from typing import List, Optional, abstractmethod
from repositories.repository_interface import Repository
from src.service_request import ServiceRequest

class ServiceRequestRepository(Repository[ServiceRequest, str]):
    """Repository interface for ServiceRequest entities."""
    
    @abstractmethod
    def find_by_guest_id(self, guest_id: str) -> List[ServiceRequest]:
        """Find all requests made by a specific guest"""
        pass
    
    @abstractmethod
    def find_by_room_id(self, room_id: str) -> List[ServiceRequest]:
        """Find all requests for a specific room"""
        pass
