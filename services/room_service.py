from typing import List, Optional
from src.room import Room, RoomType, RoomStatus
from repositories.room_repository import RoomRepository

class RoomService:
    """Business logic for Room operations"""
    
    def __init__(self, room_repository: RoomRepository):
        self.room_repo = room_repository
    
    def create_room(self, room_id: str, room_number: str, room_type: RoomType,
                    price_per_night: float, floor: int, max_guests: int) -> Room:
        """Create a new room"""
        # Business rule: Room number must be unique
        existing = self.room_repo.find_by_room_number(room_number)
        if existing:
            raise ValueError(f"Room with number {room_number} already exists")
        
        # Business rule: Price must be positive
        if price_per_night <= 0:
            raise ValueError("Price per night must be positive")
        
        # Business rule: Max guests must be between 1 and 10
        if max_guests < 1 or max_guests > 10:
            raise ValueError("Max guests must be between 1 and 10")
        
        room = Room(room_id, room_number, room_type, price_per_night, floor, max_guests)
        self.room_repo.save(room)
        return room
    
    def get_room(self, room_id: str) -> Room:
        """Get room by ID"""
        room = self.room_repo.find_by_id(room_id)
        if not room:
            raise ValueError(f"Room with ID {room_id} not found")
        return room
    
    def get_all_rooms(self) -> List[Room]:
        """Get all rooms"""
        return self.room_repo.find_all()
    
    def update_room_status(self, room_id: str, new_status: RoomStatus) -> Room:
        """Update room status"""
        room = self.get_room(room_id)
        room.update_status(new_status)
        self.room_repo.save(room)
        return room
    
    def get_available_rooms(self) -> List[Room]:
        """Get all available rooms"""
        return self.room_repo.find_available_rooms()
    
    def get_rooms_by_type(self, room_type: RoomType) -> List[Room]:
        """Get rooms by type"""
        return self.room_repo.find_by_room_type(room_type)
    
    def delete_room(self, room_id: str) -> None:
        """Delete a room"""
        # Business rule: Cannot delete room that is booked or occupied
        room = self.get_room(room_id)
        if room.get_status() in [RoomStatus.BOOKED, RoomStatus.OCCUPIED]:
            raise ValueError(f"Cannot delete room {room_id} - it is {room.get_status().value}")
        self.room_repo.delete(room_id)
