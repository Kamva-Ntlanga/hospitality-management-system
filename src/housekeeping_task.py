from enum import Enum
from datetime import datetime

class TaskStatus(Enum):
    ASSIGNED = "Assigned"
    IN_PROGRESS = "InProgress"
    COMPLETED = "Completed"
    ISSUE_REPORTED = "IssueReported"
    INSPECTED = "Inspected"

class Priority(Enum):
    HIGH = "High"
    MEDIUM = "Medium"
    LOW = "Low"

class HousekeepingTask:
    def __init__(self, task_id: str, room, priority: Priority = Priority.MEDIUM, scheduled_time: datetime = None):
        self._task_id = task_id
        self._room = room
        self._assigned_to = None
        self._status = TaskStatus.ASSIGNED
        self._priority = priority
        self._scheduled_time = scheduled_time or datetime.now()
        self._completed_time = None

    def get_task_id(self) -> str:
        return self._task_id

    def get_room(self):
        return self._room

    def get_assigned_to(self):
        return self._assigned_to

    def get_status(self) -> TaskStatus:
        return self._status

    def get_priority(self) -> Priority:
        return self._priority

    def assign_staff(self, staff):
        self._assigned_to = staff
        self._status = TaskStatus.ASSIGNED

    def start_task(self) -> None:
        if self._status == TaskStatus.ASSIGNED:
            self._status = TaskStatus.IN_PROGRESS

    def complete_task(self) -> None:
        if self._status == TaskStatus.IN_PROGRESS:
            self._status = TaskStatus.COMPLETED
            self._completed_time = datetime.now()

    def report_issue(self, description: str):
        self._status = TaskStatus.ISSUE_REPORTED
        return description

    def inspect(self) -> None:
        if self._status == TaskStatus.COMPLETED:
            self._status = TaskStatus.INSPECTED

    def __str__(self) -> str:
        return f"Task {self._task_id}: Room {self._room.get_room_number()} - {self._status.value}"
