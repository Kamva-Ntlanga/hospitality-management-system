# Assignment 9 Reflection: Domain Model and Class Diagram

## Challenges in Designing the Domain Model

The first challenge was abstraction – deciding which attributes and methods belong to each entity. For example, should *totalPrice* be stored in Booking or calculated on demand? I chose to store it because it is a business value that may be fixed at booking time even if nightly rates change later. Similarly, *loyaltyPoints* on Guest is stored rather than calculated from booking history for performance.

Another challenge was defining relationships with correct multiplicity. The booking–payment relationship was particularly tricky: can a booking have multiple payments (e.g., deposit + final payment)? For HotelHub’s MVP, we assume one payment per booking, but future versions may split payments. I used 1 to 1 for simplicity and to align with FR-7 (Integrated Billing).

Method definitions also required trade-offs. Some methods like *calculateTotal()* on Booking could be a helper method or a separate pricing service. I placed it in Booking because it depends only on Booking’s dates and Room’s pricePerNight, which are accessible via association.

## Alignment with Previous Assignments

The class diagram directly traces to:

- **Functional Requirements (Assignment 4)**: FR-1, FR-2, FR-3, FR-4, FR-6, FR-7, FR-9
- **Use Cases (Assignment 5)**: UC-02 (Book Room), UC-05 (Make Payment)
- **State Diagrams (Assignment 8)**: Status attributes match states defined in those diagrams.
- **Activity Diagrams (Assignment 8)**: Methods like *checkIn()* and *checkOut()* encapsulate activity steps.

## Trade-offs Made

1. **Inheritance vs. Composition**: I chose not to create a superclass *Person* for Guest and StaffAccount because they have very different attributes.
2. **Bidirectional vs. Unidirectional Associations**: I kept bidirectional where both sides need navigation.
3. **Data Types**: Used simple types instead of enums because Mermaid.js does not support enums directly.
4. **Method Signatures**: Omitted some parameters to keep diagram readable.

## Lessons Learned about Object-Oriented Design

Domain modeling is iterative. I started with 5 entities and added more as I discovered missing relationships. Multiplicity decisions affect business rules. Mermaid.js is powerful but limited for advanced UML features.

This assignment reinforced that a good domain model is the foundation for both database design and application logic.
