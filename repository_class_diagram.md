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

```mermaid

### Explanation

The Repository Class Diagram illustrates the structure of the repository layer used in the Hospitality Management System. At the core of the design is the generic `Repository<T, ID>` interface, which defines common CRUD operations such as saving, finding, deleting, and counting entities.

Specialized repositories such as `RoomRepository`, `GuestRepository`, and `BookingRepository` extend the generic repository and include entity-specific methods. Examples include searching rooms by room type, finding guests by email, and retrieving bookings by date or guest ID.

The diagram also shows the in-memory repository implementations (`InMemoryRoomRepository`, `InMemoryGuestRepository`, and `InMemoryBookingRepository`) that provide concrete storage functionality using memory-based data storage.

Additionally, the `RepositoryFactory` class demonstrates the Factory Pattern by creating repository objects based on the selected storage type. This design improves flexibility, scalability, and maintainability by separating data access logic from the business logic and allowing future support for database or file-based storage systems.

