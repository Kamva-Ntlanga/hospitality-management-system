from typing import List, Optional
from src.housekeeping_task import HousekeepingTask, TaskStatus
from repositories.housekeeping_repository import HousekeepingTaskRepository
from repositories.inmemory.in_memory_base import InMemoryRepository

class InMemoryHousekeepingTaskRepository(HousekeepingTaskRepository):
    def __init__(self):
        self._storage = InMemoryRepository[HousekeepingTask, str]()
    
    def save(self, entity: HousekeepingTask) -> None:
        self._storage.save(entity, entity.get_task_id())
    
    def find_by_id(self, id: str) -> Optional[HousekeepingTask]:
        return self._storage.find_by_id(id)
    
    def find_all(self) -> List[HousekeepingTask]:
        return self._storage.find_all()
    
    def delete(self, id: str) -> None:
        self._storage.delete(id)
    
    def exists(self, id: str) -> bool:
        return self._storage.exists(id)
    
    def count(self) -> int:
        return self._storage.count()
    
    def find_by_room_id(self, room_id: str) -> List[HousekeepingTask]:
        return [t for t in self.find_all() if t.get_room().get_room_id() == room_id]
    
    def find_pending_tasks(self) -> List[HousekeepingTask]:
        pending_statuses = [TaskStatus.ASSIGNED, TaskStatus.IN_PROGRESS]
        return [t for t in self.find_all() if t.get_status() in pending_statuses]
    
    def clear(self):
        self._storage.clear()
