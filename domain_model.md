# Domain Model – Hospitality Management System

## Core Domain Entities (7 entities)

| Entity | Description |
|--------|-------------|
| **Room** | Physical hotel room with type, price, and status |
| **Guest** | Customer who makes bookings and uses services |
| **Booking** | Reservation of a room by a guest for specific dates |
| **Payment** | Financial transaction for a booking or service |
| **HousekeepingTask** | Cleaning job assigned to a room |
| **ServiceRequest** | Guest request for amenities, room service, or maintenance |
| **StaffAccount** | Employee login with role and permissions |

## Detailed Domain Model Table

| Entity | Attributes | Methods | Relationships | Business Rules |
|--------|------------|---------|---------------|----------------|
| **Room** | roomId: String<br>roomNumber: String<br>roomType: String (Standard, Deluxe, Suite)<br>pricePerNight: Double<br>status: String (Available, Booked, Occupied, Maintenance)<br>floor: Integer<br>maxGuests: Integer | +updateStatus(newStatus)<br>+isAvailable(): Boolean<br>+getPriceForDates(checkIn, checkOut): Double | Room "1" to "0..*" Booking<br>Room "1" to "0..*" HousekeepingTask<br>Room "1" to "0..*" ServiceRequest | Room cannot be booked if not Available.<br>Room must be cleaned after each check-out. |
| **Guest** | guestId: String<br>firstName: String<br>lastName: String<br>email: String<br>phone: String<br>loyaltyPoints: Integer<br>preferences: String | +updateProfile()<br>+viewBookingHistory(): List&lt;Booking&gt;<br>+requestService(category, description): ServiceRequest | Guest "1" to "0..*" Booking<br>Guest "1" to "0..*" ServiceRequest<br>Guest "1" to "0..*" Payment | Email must be unique.<br>Loyalty points = 10 points per night stayed. |
| **Booking** | bookingId: String<br>checkInDate: Date<br>checkOutDate: Date<br>totalPrice: Double<br>status: String (Pending, Confirmed, CheckedIn, Completed, Cancelled)<br>numberOfGuests: Integer<br>specialRequests: String | +confirmBooking()<br>+cancelBooking()<br>+checkIn()<br>+checkOut()<br>+calculateTotal(): Double | Booking belongs to Guest (1 to 1).<br>Booking for Room (1 to 1).<br>Booking has Payment (1 to 1). | No overlapping bookings for same room.<br>Cancel only if Pending or Confirmed.<br>Check-in only within 24h of arrival. |
| **Payment** | paymentId: String<br>amount: Double<br>paymentDate: DateTime<br>method: String (Credit Card, Cash, Digital Wallet)<br>status: String (Pending, Authorized, Captured, Failed, Refunded)<br>transactionId: String | +authorize(): Boolean<br>+capture(): Boolean<br>+refund(): Boolean<br>+generateReceipt(): String | Payment belongs to Booking (1 to 1).<br>Payment associated with Guest (many to 1). | Cannot capture without authorize.<br>Refund only if Captured and within 30 days. |
| **HousekeepingTask** | taskId: String<br>roomId: String<br>assignedTo: String<br>status: String (Assigned, InProgress, Completed, IssueReported, Inspected)<br>priority: String (High, Medium, Low)<br>scheduledTime: DateTime<br>completedTime: DateTime | +assignStaff(staffId)<br>+startTask()<br>+completeTask()<br>+reportIssue(description): MaintenanceRequest | Task for Room (1 to 1).<br>Task assigned to StaffAccount (1 to 1). | Auto-created when room status becomes Available after check-out.<br>VIP rooms get High priority. |
| **ServiceRequest** | requestId: String<br>guestId: String<br>roomId: String<br>category: String (Housekeeping, RoomService, Maintenance, Concierge)<br>description: String<br>status: String (Submitted, Acknowledged, InProgress, Completed, Escalated)<br>requestTime: DateTime<br>estimatedCompletion: DateTime | +acknowledge()<br>+start()<br>+complete()<br>+escalate() | Request made by Guest (1 to 1).<br>Request associated with Room (1 to 1).<br>Request may be handled by StaffAccount (0..1). | Must be acknowledged within 5 min peak hours.<br>Maintenance requests auto-create MaintenanceRequest. |
| **StaffAccount** | staffId: String<br>username: String<br>passwordHash: String<br>role: String (Manager, FrontDesk, Housekeeping, Finance, IT)<br>permissions: List&lt;String&gt;<br>isActive: Boolean<br>lastLogin: DateTime | +login(password): Boolean<br>+logout()<br>+resetPassword()<br>+hasPermission(permission): Boolean | StaffAccount assigned many HousekeepingTasks (1 to 0..*).<br>StaffAccount handles many ServiceRequests (1 to 0..*). | Lock after 5 failed logins.<br>Only IT Admin can deactivate accounts. |
