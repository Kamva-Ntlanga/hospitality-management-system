# Class Diagram – Hospitality Management System

```mermaid
classDiagram
    class Room {
        - roomId: String
        - roomNumber: String
        - roomType: String
        - pricePerNight: Double
        - status: String
        - floor: Integer
        - maxGuests: Integer
        + updateStatus(newStatus)
        + isAvailable(): Boolean
        + getPriceForDates(checkIn, checkOut): Double
    }

    class Guest {
        - guestId: String
        - firstName: String
        - lastName: String
        - email: String
        - phone: String
        - loyaltyPoints: Integer
        - preferences: String
        + updateProfile()
        + viewBookingHistory(): List~Booking~
        + requestService(category, description): ServiceRequest
    }

    class Booking {
        - bookingId: String
        - checkInDate: Date
        - checkOutDate: Date
        - totalPrice: Double
        - status: String
        - numberOfGuests: Integer
        - specialRequests: String
        + confirmBooking()
        + cancelBooking()
        + checkIn()
        + checkOut()
        + calculateTotal(): Double
    }

    class Payment {
        - paymentId: String
        - amount: Double
        - paymentDate: DateTime
        - method: String
        - status: String
        - transactionId: String
        + authorize(): Boolean
        + capture(): Boolean
        + refund(): Boolean
        + generateReceipt(): String
    }

    class HousekeepingTask {
        - taskId: String
        - roomId: String
        - assignedTo: String
        - status: String
        - priority: String
        - scheduledTime: DateTime
        - completedTime: DateTime
        + assignStaff(staffId)
        + startTask()
        + completeTask()
        + reportIssue(description): MaintenanceRequest
    }

    class ServiceRequest {
        - requestId: String
        - guestId: String
        - roomId: String
        - category: String
        - description: String
        - status: String
        - requestTime: DateTime
        - estimatedCompletion: DateTime
        + acknowledge()
        + start()
        + complete()
        + escalate()
    }

    class StaffAccount {
        - staffId: String
        - username: String
        - passwordHash: String
        - role: String
        - permissions: List~String~
        - isActive: Boolean
        - lastLogin: DateTime
        + login(password): Boolean
        + logout()
        + resetPassword()
        + hasPermission(permission): Boolean
    }

    Guest "1" --> "0..*" Booking : makes
    Room "1" <-- "0..*" Booking : reservedFor
    Booking "1" --> "1" Payment : has
    Guest "1" --> "0..*" ServiceRequest : requests
    Room "1" --> "0..*" ServiceRequest : associatedWith
    Room "1" --> "0..*" HousekeepingTask : requiresCleaning
    StaffAccount "1" o--> "0..*" HousekeepingTask : assignedTo
    StaffAccount "1" --> "0..*" ServiceRequest : handles
