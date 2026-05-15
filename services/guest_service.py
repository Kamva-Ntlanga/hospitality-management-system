from typing import List, Optional
from src.guest import Guest
from repositories.guest_repository import GuestRepository

class GuestService:
    """Business logic for Guest operations"""
    
    def __init__(self, guest_repository: GuestRepository):
        self.guest_repo = guest_repository
    
    def create_guest(self, guest_id: str, first_name: str, last_name: str,
                     email: str, phone: str) -> Guest:
        """Create a new guest"""
        # Business rule: Email must be unique
        existing = self.guest_repo.find_by_email(email)
        if existing:
            raise ValueError(f"Guest with email {email} already exists")
        
        # Business rule: Email must contain @ symbol
        if "@" not in email:
            raise ValueError("Invalid email format")
        
        # Business rule: Phone must be at least 10 digits
        if len(phone) < 10:
            raise ValueError("Phone number must be at least 10 digits")
        
        guest = Guest(guest_id, first_name, last_name, email, phone)
        self.guest_repo.save(guest)
        return guest
    
    def get_guest(self, guest_id: str) -> Guest:
        """Get guest by ID"""
        guest = self.guest_repo.find_by_id(guest_id)
        if not guest:
            raise ValueError(f"Guest with ID {guest_id} not found")
        return guest
    
    def get_guest_by_email(self, email: str) -> Optional[Guest]:
        """Get guest by email"""
        return self.guest_repo.find_by_email(email)
    
    def get_all_guests(self) -> List[Guest]:
        """Get all guests"""
        return self.guest_repo.find_all()
    
    def update_guest_profile(self, guest_id: str, first_name: str = None,
                             last_name: str = None, phone: str = None) -> Guest:
        """Update guest profile"""
        guest = self.get_guest(guest_id)
        if first_name:
            guest.update_profile(first_name=first_name)
        if last_name:
            guest.update_profile(last_name=last_name)
        if phone:
            if len(phone) < 10:
                raise ValueError("Phone number must be at least 10 digits")
            guest.update_profile(phone=phone)
        self.guest_repo.save(guest)
        return guest
    
    def add_loyalty_points(self, guest_id: str, points: int) -> Guest:
        """Add loyalty points to guest"""
        # Business rule: Points must be positive
        if points <= 0:
            raise ValueError("Points must be positive")
        guest = self.get_guest(guest_id)
        guest.add_loyalty_points(points)
        self.guest_repo.save(guest)
        return guest
    
    def delete_guest(self, guest_id: str) -> None:
        """Delete a guest"""
        # Business rule: Cannot delete guest with active bookings
        # This would check bookings - simplified for now
        self.guest_repo.delete(guest_id)
