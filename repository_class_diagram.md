# Repository Class Diagram

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
        +createRoomRepository(storageType: str) RoomRepository
        +createGuestRepository(storageType: str) GuestRepository
        +createBookingRepository(storageType: str) BookingRepository
    }

    RoomRepository --|> Repository
    GuestRepository --|> Repository
    BookingRepository --|> Repository

    InMemoryRoomRepository --|> RoomRepository
    InMemoryGuestRepository --|> GuestRepository
    InMemoryBookingRepository --|> BookingRepository

    RepositoryFactory ..> RoomRepository : creates
    RepositoryFactory ..> GuestRepository : creates
    RepositoryFactory ..> BookingRepository : creates
