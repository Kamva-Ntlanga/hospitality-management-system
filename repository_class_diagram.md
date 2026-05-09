# Updated Class Diagram with Repository Pattern

## Mermaid Class Diagram

```mermaid
classDiagram
    class Repository~T, ID~ {
        <<interface>>
        +save(entity: T) void
        +findById(id: ID) Optional~T~
        +findAll() List~T~
        +delete(id: ID) void
        +exists(id: ID) bool
        +count() int
    }

    class RoomRepository {
        <<interface>>
        +findByRoomNumber(roomNumber: str) Optional~Room~
        +findByRoomType(roomType: RoomType) List~Room~
        +findAvailableRooms() List~Room~
    }

    class GuestRepository {
        <<interface>>
        +findByEmail(email: str) Optional~Guest~
        +findByLoyaltyPointsRange(minPoints, maxPoints) List~Guest~
    }

    class BookingRepository {
        <<interface>>
        +findByGuestId(guestId: str) List~Booking~
        +findByRoomId(roomId: str) List~Booking~
        +findByDateRange(startDate, endDate) List~Booking~
        +findUpcomingBookings() List~Booking~
        +findCurrentActiveBookings() List~Booking~
    }

    class PaymentRepository {
        <<interface>>
        +findByBookingId(bookingId: str) Optional~Payment~
        +findByStatus(status: PaymentStatus) List~Payment~
    }

    class HousekeepingTaskRepository {
        <<interface>>
        +findByRoomId(roomId: str) List~HousekeepingTask~
        +findPendingTasks() List~HousekeepingTask~
    }

    class ServiceRequestRepository {
        <<interface>>
        +findByGuestId(guestId: str) List~ServiceRequest~
        +findByRoomId(roomId: str) List~ServiceRequest~
    }

    class StaffAccountRepository {
        <<interface>>
        +findByUsername(username: str) Optional~StaffAccount~
        +findByRole(role: Role) List~StaffAccount~
        +findActiveStaff() List~StaffAccount~
    }

    class InMemoryBase~T, ID~ {
        -_storage: Dict
        +save(entity: T, id: ID) void
        +findById(id: ID) Optional~T~
        +findAll() List~T~
        +delete(id: ID) void
        +exists(id: ID) bool
        +count() int
        +clear() void
    }

    class InMemoryRoomRepository {
        +findByRoomNumber(roomNumber: str) Optional~Room~
        +findByRoomType(roomType: RoomType) List~Room~
        +findAvailableRooms() List~Room~
    }

    class InMemoryGuestRepository {
        +findByEmail(email: str) Optional~Guest~
        +findByLoyaltyPointsRange(minPoints, maxPoints) List~Guest~
    }

    class InMemoryBookingRepository {
        +findByGuestId(guestId: str) List~Booking~
        +findByRoomId(roomId: str) List~Booking~
        +findByDateRange(startDate, endDate) List~Booking~
        +findUpcomingBookings() List~Booking~
        +findCurrentActiveBookings() List~Booking~
    }

    class RepositoryFactory {
        +createRoomRepository(storageType: StorageType) RoomRepository
        +createGuestRepository(storageType: StorageType) GuestRepository
        +createBookingRepository(storageType: StorageType) BookingRepository
        +createPaymentRepository(storageType: StorageType) PaymentRepository
        +createHousekeepingRepository(storageType: StorageType) HousekeepingTaskRepository
        +createServiceRequestRepository(storageType: StorageType) ServiceRequestRepository
        +createStaffAccountRepository(storageType: StorageType) StaffAccountRepository
    }

    class StorageType {
        <<enumeration>>
        MEMORY
        DATABASE
        FILESYSTEM
    }

    RoomRepository --|> Repository
    GuestRepository --|> Repository
    BookingRepository --|> Repository
    PaymentRepository --|> Repository
    HousekeepingTaskRepository --|> Repository
    ServiceRequestRepository --|> Repository
    StaffAccountRepository --|> Repository

    InMemoryRoomRepository --|> RoomRepository
    InMemoryGuestRepository --|> GuestRepository
    InMemoryBookingRepository --|> BookingRepository

    InMemoryRoomRepository --|> InMemoryBase
    InMemoryGuestRepository --|> InMemoryBase
    InMemoryBookingRepository --|> InMemoryBase

    RepositoryFactory --> StorageType
    RepositoryFactory ..> RoomRepository : creates
    RepositoryFactory ..> GuestRepository : creates
    RepositoryFactory ..> BookingRepository : creates
