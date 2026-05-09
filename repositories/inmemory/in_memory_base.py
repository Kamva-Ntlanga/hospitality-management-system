from typing import Dict, List, Optional, Generic, TypeVar
from repositories.repository_interface import Repository

T = TypeVar('T')
ID = TypeVar('ID')

class InMemoryRepository(Generic[T, ID]):
    """
    Base in-memory repository using HashMap/Dictionary for storage.
    Shared implementation for all entity repositories.
    """
    
    def __init__(self):
        self._storage: Dict[ID, T] = {}
    
    def save(self, entity: T, entity_id: ID) -> None:
        """Save entity to in-memory storage"""
        self._storage[entity_id] = entity
    
    def find_by_id(self, id: ID) -> Optional[T]:
        """Find entity by ID"""
        return self._storage.get(id)
    
    def find_all(self) -> List[T]:
        """Return all entities"""
        return list(self._storage.values())
    
    def delete(self, id: ID) -> None:
        """Delete entity by ID"""
        if id in self._storage:
            del self._storage[id]
    
    def exists(self, id: ID) -> bool:
        """Check if entity exists"""
        return id in self._storage
    
    def count(self) -> int:
        """Return total number of entities"""
        return len(self._storage)
    
    def clear(self) -> None:
        """Clear all data (useful for testing)"""
        self._storage.clear()
