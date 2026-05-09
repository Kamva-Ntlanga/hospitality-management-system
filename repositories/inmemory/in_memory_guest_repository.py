from typing import List, Optional
from src.guest import Guest
from repositories.guest_repository import GuestRepository
from repositories.inmemory.in_memory_base import InMemoryRepository

class InMemoryGuestRepository(GuestRepository):
    def __init__(self):
        self._storage = InMemoryRepository[Guest, str]()
    
    def save(self, entity: Guest) -> None:
        self._storage.save(entity, entity.get_guest_id())
    
    def find_by_id(self, id: str) -> Optional[Guest]:
        return self._storage.find_by_id(id)
    
    def find_all(self) -> List[Guest]:
        return self._storage.find_all()
    
    def delete(self, id: str) -> None:
        self._storage.delete(id)
    
    def exists(self, id: str) -> bool:
        return self._storage.exists(id)
    
    def count(self) -> int:
        return self._storage.count()
    
    def find_by_email(self, email: str) -> Optional[Guest]:
        for guest in self.find_all():
            if guest.get_email() == email:
                return guest
        return None
    
    def find_by_loyalty_points_range(self, min_points: int, max_points: int) -> List[Guest]:
        return [g for g in self.find_all() if min_points <= g.get_loyalty_points() <= max_points]
    
    def clear(self):
        self._storage.clear()
