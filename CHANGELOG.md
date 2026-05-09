# Changelog - HotelHub

## 2025-05-01

### Added -  Assignment 10
- Initial class implementations (Room, Guest, Booking, Payment, HousekeepingTask, ServiceRequest, StaffAccount)
- Simple Factory pattern: RoomFactory
- Factory Method pattern: PaymentProcessor
- Abstract Factory pattern: RoomAmenityFactory
- Builder pattern: BookingBuilder
- Prototype pattern: RoomTemplateCache
- Singleton pattern: DatabaseConnection and ConfigurationManager

### Testing
- Unit tests for all classes
- Unit tests for all creational patterns

  ## 2025-05-09

  ### Added - Assignment 11: Repository Pattern

- Generic Repository interface with CRUD operations
- Entity-specific repository interfaces (Room, Guest, Booking, Payment, Housekeeping, ServiceRequest, StaffAccount)
- In-memory HashMap implementations for all 7 entities
- Factory pattern (RepositoryFactory) for storage abstraction
- Stub for future database storage backend
- Unit tests for in-memory repositories
- Unit tests for repository factory
- Updated class diagram showing repository layer
