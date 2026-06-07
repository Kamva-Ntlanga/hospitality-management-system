from typing import List, Optional
from src.service_request import ServiceRequest, RequestStatus
from repositories.service_request_repository import ServiceRequestRepository
from repositories.inmemory.in_memory_base import InMemoryRepository

class InMemoryServiceRequestRepository(ServiceRequestRepository):
    def __init__(self):
        self._storage = InMemoryRepository[ServiceRequest, str]()
    
    def save(self, entity: ServiceRequest) -> None:
        self._storage.save(entity, entity.get_request_id())
    
    def find_by_id(self, id: str) -> Optional[ServiceRequest]:
        return self._storage.find_by_id(id)
    
    def find_all(self) -> List[ServiceRequest]:
        return self._storage.find_all()
    
    def delete(self, id: str) -> None:
        self._storage.delete(id)
    
    def exists(self, id: str) -> bool:
        return self._storage.exists(id)
    
    def count(self) -> int:
        return self._storage.count()
    
    def find_by_guest_id(self, guest_id: str) -> List[ServiceRequest]:
        return [r for r in self.find_all() if r.get_guest_id() == guest_id]
    
    def find_by_room_id(self, room_id: str) -> List[ServiceRequest]:
        return [r for r in self.find_all() if r.get_room_id() == room_id]
    
    def find_by_status(self, status: RequestStatus) -> List[ServiceRequest]:
        return [r for r in self.find_all() if r.get_status() == status]
    
    def clear(self):
        self._storage.clear()
