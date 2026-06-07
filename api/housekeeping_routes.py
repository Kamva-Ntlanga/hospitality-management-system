from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from typing import List, Optional
from services.housekeeping_service import HousekeepingService

router = APIRouter()

# Request schemas matching testing inputs
class TaskCreateRequest(BaseModel):
    task_id: str
    room_id: str
    priority: Optional[str] = "MEDIUM"

class TaskManageRequest(BaseModel):
    action: str

class IssueReportRequest(BaseModel):
    description: str

def serialize_task(task) -> dict:
    """Helper utility to extract and structure instance attributes safely into JSON mappings"""
    return {
        "task_id": task.get_task_id(),
        "room_id": str(task.get_room()), 
        "status": task.get_status().value,
        "priority": task.get_priority().value,
        "assigned_to": task.get_assigned_to()
    }

# A clean internal dependency provider to get around top-level circular imports
def get_local_housekeeping_service() -> HousekeepingService:
    from api.main import get_housekeeping_service
    return get_housekeeping_service()

@router.post("/", response_model=dict, status_code=status.HTTP_201_CREATED)
async def create_housekeeping_task(
    payload: TaskCreateRequest, 
    service: HousekeepingService = Depends(get_local_housekeeping_service)
):
    """Endpoint to dynamically create a new cleaning assignment record"""
    try:
        task = service.create_task(payload.task_id, payload.room_id, payload.priority)
        return serialize_task(task)
    except ValueError as err:
        raise HTTPException(status_code=400, detail=str(err))

@router.get("/", response_model=List[dict])
async def view_all_tasks(
    service: HousekeepingService = Depends(get_local_housekeeping_service)
):
    """Exposes US-006: View Housekeeping Tasks endpoint"""
    tasks = service.get_all_tasks()
    return [serialize_task(t) for t in tasks]

@router.post("/{task_id}/manage", response_model=dict)
async def manage_task_status(
    task_id: str, 
    payload: TaskManageRequest,
    service: HousekeepingService = Depends(get_local_housekeeping_service)
):
    """Exposes US-006: Manage Housekeeping Tasks endpoint (start/complete/inspect)"""
    try:
        updated_task = service.update_task_status(task_id, payload.action)
        return serialize_task(updated_task)
    except ValueError as err:
        raise HTTPException(status_code=400, detail=str(err))

@router.post("/{task_id}/report-issue", response_model=dict)
async def report_room_issue(
    task_id: str, 
    payload: IssueReportRequest,
    service: HousekeepingService = Depends(get_local_housekeeping_service)
):
    """Endpoint to flag structural issues found inside rooms by housekeeping staff"""
    try:
        updated_task = service.report_task_issue(task_id, payload.description)
        return serialize_task(updated_task)
    except ValueError as err:
        raise HTTPException(status_code=400, detail=str(err))