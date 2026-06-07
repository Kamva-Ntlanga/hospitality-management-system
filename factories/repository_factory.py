from enum import Enum
from typing import Union

from repositories.room_repository import RoomRepository
from repositories.guest_repository import GuestRepository
from repositories.booking_repository import BookingRepository
from repositories.payment_repository import PaymentRepository
from repositories.housekeeping_repository import HousekeepingTaskRepository
from repositories.service_request_repository import ServiceRequestRepository
from repositories.staff_account_repository import StaffAccountRepository

from repositories.inmemory.in_memory_room_repository import InMemoryRoomRepository
from repositories.inmemory.in_memory_guest_repository import InMemoryGuestRepository
from repositories.inmemory.in_memory_booking_repository import InMemoryBookingRepository
from repositories.inmemory.in_memory_payment_repository import InMemoryPaymentRepository
from repositories.inmemory.in_memory_housekeeping_repository import InMemoryHousekeepingTaskRepository
from repositories.inmemory.in_memory_service_request_repository import InMemoryServiceRequestRepository
from repositories.inmemory.in_memory_staff_account_repository import InMemoryStaffAccountRepository

class StorageType(Enum):
    MEMORY = "memory"
    DATABASE = "database"      # Future implementation
    FILESYSTEM = "filesystem"  # Future implementation

class RepositoryFactory:
    """
    Factory for creating repository instances with different storage backends.
    This allows easy switching between storage implementations.
    """
    
    @staticmethod
    def create_room_repository(storage_type: StorageType = StorageType.MEMORY) -> RoomRepository:
        if storage_type == StorageType.MEMORY:
            return InMemoryRoomRepository()
        elif storage_type == StorageType.DATABASE:
            from future_stubs.database_repository_stub import DatabaseRoomRepository
            return DatabaseRoomRepository()
        else:
            raise ValueError(f"Unknown storage type: {storage_type}")
    
    @staticmethod
    def create_guest_repository(storage_type: StorageType = StorageType.MEMORY) -> GuestRepository:
        if storage_type == StorageType.MEMORY:
            return InMemoryGuestRepository()
        elif storage_type == StorageType.DATABASE:
            from future_stubs.database_repository_stub import DatabaseGuestRepository
            return DatabaseGuestRepository()
        else:
            raise ValueError(f"Unknown storage type: {storage_type}")
    
    @staticmethod
    def create_booking_repository(storage_type: StorageType = StorageType.MEMORY) -> BookingRepository:
        if storage_type == StorageType.MEMORY:
            return InMemoryBookingRepository()
        elif storage_type == StorageType.DATABASE:
            from future_stubs.database_repository_stub import DatabaseBookingRepository
            return DatabaseBookingRepository()
        else:
            raise ValueError(f"Unknown storage type: {storage_type}")

    @staticmethod
    def create_service_request_repository(storage_type: StorageType = StorageType.MEMORY) -> ServiceRequestRepository:
        if storage_type == StorageType.MEMORY:
            return InMemoryServiceRequestRepository()
        elif storage_type == StorageType.DATABASE:
            raise ValueError("Database storage is not implemented for service requests")
        else:
            raise ValueError(f"Unknown storage type: {storage_type}")

    # Additional create methods for Payment, Housekeeping, StaffAccount
