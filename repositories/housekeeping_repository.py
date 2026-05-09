from typing import List, Optional, abstractmethod
from repositories.repository_interface import Repository
from src.housekeeping_task import HousekeepingTask

class HousekeepingTaskRepository(Repository[HousekeepingTask, str]):
    """Repository interface for HousekeepingTask entities."""
    
    @abstractmethod
    def find_by_room_id(self, room_id: str) -> List[HousekeepingTask]:
        """Find all tasks for a specific room"""
        pass
    
    @abstractmethod
    def find_pending_tasks(self) -> List[HousekeepingTask]:
        """Find tasks that are not yet completed"""
        pass
