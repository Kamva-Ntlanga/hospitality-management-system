from typing import List, Optional
from repositories.repository_interface import Repository
from src.room import Room

class RoomRepository(Repository[Room, str]):
    """
    Repository interface for Room entities.
    Includes Room-specific query methods.
    """
    
    @abstractmethod
    def find_by_room_number(self, room_number: str) -> Optional[Room]:
        """Find a room by its room number"""
        pass
    
    @abstractmethod
    def find_by_room_type(self, room_type: str) -> List[Room]:
        """Find all rooms of a specific type"""
        pass
    
    @abstractmethod
    def find_available_rooms(self) -> List[Room]:
        """Find all available rooms"""
        pass
