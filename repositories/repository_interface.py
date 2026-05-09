from abc import ABC, abstractmethod
from typing import Generic, TypeVar, List, Optional

T = TypeVar('T')
ID = TypeVar('ID')

class Repository(ABC, Generic[T, ID]):
    """
    Generic repository interface for CRUD operations.
    This abstracts storage details behind a simple interface.
    """
    
    @abstractmethod
    def save(self, entity: T) -> None:
        """Create or update an entity"""
        pass
    
    @abstractmethod
    def find_by_id(self, id: ID) -> Optional[T]:
        """Find an entity by its ID"""
        pass
    
    @abstractmethod
    def find_all(self) -> List[T]:
        """Return all entities"""
        pass
    
    @abstractmethod
    def delete(self, id: ID) -> None:
        """Delete an entity by ID"""
        pass
    
    @abstractmethod
    def exists(self, id: ID) -> bool:
        """Check if an entity exists"""
        pass
    
    @abstractmethod
    def count(self) -> int:
        """Return total number of entities"""
        pass
