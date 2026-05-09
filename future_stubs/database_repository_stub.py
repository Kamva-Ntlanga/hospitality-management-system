"""
STUB IMPLEMENTATION - For future use when switching to a real database.
This demonstrates how easy it is to add a new storage backend.
"""

from typing import List, Optional
from src.room import Room
from repositories.room_repository import RoomRepository

class DatabaseRoomRepository(RoomRepository):
    """
    Placeholder for database implementation.
    When ready, replace with actual database connection code.
    """
    
    def __init__(self, connection_string: str = "localhost:5432/hotelhub"):
        self.connection_string = connection_string
        print(f"Database repository would connect to: {connection_string}")
    
    def save(self, entity: Room) -> None:
        print(f"STUB: Would save room {entity.get_room_id()} to database")
    
    def find_by_id(self, id: str) -> Optional[Room]:
        print(f"STUB: Would find room {id} in database")
        return None
    
    def find_all(self) -> List[Room]:
        print("STUB: Would return all rooms from database")
        return []
    
    def delete(self, id: str) -> None:
        print(f"STUB: Would delete room {id} from database")
    
    def exists(self, id: str) -> bool:
        print(f"STUB: Would check if room {id} exists in database")
        return False
    
    def count(self) -> int:
        print("STUB: Would count rooms in database")
        return 0
    
    def find_by_room_number(self, room_number: str) -> Optional[Room]:
        print(f"STUB: Would find room by number {room_number} in database")
        return None
    
    def find_by_room_type(self, room_type) -> List[Room]:
        print(f"STUB: Would find rooms by type in database")
        return []
    
    def find_available_rooms(self) -> List[Room]:
        print("STUB: Would find available rooms in database")
        return []


class DatabaseGuestRepository:
    """Stub for Guest database repository"""
    pass


class DatabaseBookingRepository:
    """Stub for Booking database repository"""
    pass
