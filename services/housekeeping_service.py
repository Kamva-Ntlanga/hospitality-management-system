from typing import List, Optional
from datetime import datetime
from src.housekeeping_task import HousekeepingTask, TaskStatus, Priority

class HousekeepingService:
    """Business logic for Housekeeping operations"""
    
    def __init__(self):
        # Using an in-memory list tracking data store to match the current scope
        self._tasks: List[HousekeepingTask] = []

    def create_task(self, task_id: str, room_id: str, priority_str: str = "MEDIUM") -> HousekeepingTask:
        """Helper to provision a housekeeping task for a room"""
        try:
            priority = Priority[priority_str.upper()]
        except KeyError:
            priority = Priority.MEDIUM

        new_task = HousekeepingTask(task_id=task_id, room=room_id, priority=priority)
        self._tasks.append(new_task)
        return new_task

    def get_all_tasks(self) -> List[HousekeepingTask]:
        """View all housekeeping tasks (Matches US-006 View requirement)"""
        return self._tasks

    def get_task_by_id(self, task_id: str) -> Optional[HousekeepingTask]:
        """Find a single task by ID"""
        for task in self._tasks:
            if task.get_task_id() == task_id:
                return task
        return None

    def update_task_status(self, task_id: str, action: str) -> HousekeepingTask:
        """Manage task states smoothly (Matches US-006 Manage requirement)"""
        task = self.get_task_by_id(task_id)
        if not task:
            raise ValueError(f"Housekeeping task with ID {task_id} not found")

        normalized_action = action.lower().strip()
        
        if normalized_action == "start":
            task.start_task()
        elif normalized_action == "complete":
            task.complete_task()
        elif normalized_action == "inspect":
            task.inspect()
        else:
            raise ValueError(f"Invalid management action: '{action}'. Use start, complete, or inspect.")
            
        return task

    def report_task_issue(self, task_id: str, description: str) -> HousekeepingTask:
        """Flag maintenance or room issues directly on the task"""
        task = self.get_task_by_id(task_id)
        if not task:
            raise ValueError(f"Housekeeping task with ID {task_id} not found")
        task.report_issue(description)
        return task