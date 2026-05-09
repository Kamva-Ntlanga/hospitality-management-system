from typing import List, Optional
from src.staff_account import StaffAccount, Role
from repositories.staff_account_repository import StaffAccountRepository
from repositories.inmemory.in_memory_base import InMemoryRepository

class InMemoryStaffAccountRepository(StaffAccountRepository):
    def __init__(self):
        self._storage = InMemoryRepository[StaffAccount, str]()
    
    def save(self, entity: StaffAccount) -> None:
        self._storage.save(entity, entity.get_staff_id())
    
    def find_by_id(self, id: str) -> Optional[StaffAccount]:
        return self._storage.find_by_id(id)
    
    def find_all(self) -> List[StaffAccount]:
        return self._storage.find_all()
    
    def delete(self, id: str) -> None:
        self._storage.delete(id)
    
    def exists(self, id: str) -> bool:
        return self._storage.exists(id)
    
    def count(self) -> int:
        return self._storage.count()
    
    def find_by_username(self, username: str) -> Optional[StaffAccount]:
        for staff in self.find_all():
            if staff.get_username() == username:
                return staff
        return None
    
    def find_by_role(self, role: Role) -> List[StaffAccount]:
        return [s for s in self.find_all() if s.get_role() == role]
    
    def find_active_staff(self) -> List[StaffAccount]:
        return [s for s in self.find_all() if s.is_active()]
    
    def clear(self):
        self._storage.clear()
