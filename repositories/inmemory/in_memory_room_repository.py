from typing import List, Optional
from src.room import Room, RoomType, RoomStatus
from repositories.room_repository import RoomRepository
from repositories.inmemory.in_memory_base import InMemoryRepository

class InMemoryRoomRepository(RoomRepository):
    def __init__(self):
        self._storage = InMemoryRepository[Room, str]()
    
    def save(self, entity: Room) -> None:
        self._storage.save(entity, entity.get_room_id())
    
    def find_by_id(self, id: str) -> Optional[Room]:
        return self._storage.find_by_id(id)
    
    def find_all(self) -> List[Room]:
        return self._storage.find_all()
    
    def delete(self, id: str) -> None:
        self._storage.delete(id)
    
    def exists(self, id: str) -> bool:
        return self._storage.exists(id)
    
    def count(self) -> int:
        return self._storage.count()
    
    def find_by_room_number(self, room_number: str) -> Optional[Room]:
        for room in self.find_all():
            if room.get_room_number() == room_number:
                return room
        return None
    
    def find_by_room_type(self, room_type: RoomType) -> List[Room]:
        return [r for r in self.find_all() if r.get_room_type() == room_type]
    
    def find_available_rooms(self) -> List[Room]:
        return [r for r in self.find_all() if r.is_available()]
    
    def clear(self):
        self._storage.clear()
