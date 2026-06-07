import unittest
from datetime import date, timedelta
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from services.room_service import RoomService
from services.guest_service import GuestService
from services.booking_service import BookingService
from repositories.inmemory.in_memory_room_repository import InMemoryRoomRepository
from repositories.inmemory.in_memory_guest_repository import InMemoryGuestRepository
from repositories.inmemory.in_memory_booking_repository import InMemoryBookingRepository
from src.room import RoomType, RoomStatus
from src.room import Room, RoomType, RoomStatus
from src.booking import BookingStatus
from src.guest import Guest

class TestRoomService(unittest.TestCase):
    def setUp(self):
        self.repo = InMemoryRoomRepository()
        self.service = RoomService(self.repo)
    
    def test_create_room_success(self):
        room = self.service.create_room("R001", "101", RoomType.STANDARD, 100.0, 1, 2)
        self.assertEqual(room.get_room_number(), "101")
    
    def test_create_room_duplicate_number_fails(self):
        self.service.create_room("R001", "101", RoomType.STANDARD, 100.0, 1, 2)
        with self.assertRaises(ValueError):
            self.service.create_room("R002", "101", RoomType.DELUXE, 200.0, 1, 4)
    
    def test_create_room_negative_price_fails(self):
        with self.assertRaises(ValueError):
            self.service.create_room("R001", "101", RoomType.STANDARD, -100.0, 1, 2)
    
    def test_get_room_not_found(self):
        with self.assertRaises(ValueError):
            self.service.get_room("NOT_EXIST")
    
    def test_get_available_rooms(self):
        self.service.create_room("R001", "101", RoomType.STANDARD, 100.0, 1, 2)
        self.service.create_room("R002", "102", RoomType.DELUXE, 200.0, 1, 4)
        self.service.update_room_status("R001", RoomStatus.BOOKED)
        available = self.service.get_available_rooms()
        self.assertEqual(len(available), 1)
        self.assertEqual(available[0].get_room_number(), "102")

class TestGuestService(unittest.TestCase):
    def setUp(self):
        self.repo = InMemoryGuestRepository()
        self.service = GuestService(self.repo)
    
    def test_create_guest_success(self):
        guest = self.service.create_guest("G001", "John", "Doe", "john@example.com", "1234567890")
        self.assertEqual(guest.get_email(), "john@example.com")
    
    def test_create_guest_duplicate_email_fails(self):
        self.service.create_guest("G001", "John", "Doe", "john@example.com", "1234567890")
        with self.assertRaises(ValueError):
            self.service.create_guest("G002", "Jane", "Doe", "john@example.com", "0987654321")
    
    def test_create_guest_invalid_email_fails(self):
        with self.assertRaises(ValueError):
            self.service.create_guest("G001", "John", "Doe", "invalid", "1234567890")
    
    def test_create_guest_short_phone_fails(self):
        with self.assertRaises(ValueError):
            self.service.create_guest("G001", "John", "Doe", "john@example.com", "123")
    
    def test_add_loyalty_points(self):
        self.service.create_guest("G001", "John", "Doe", "john@example.com", "1234567890")
        guest = self.service.add_loyalty_points("G001", 100)
        self.assertEqual(guest.get_loyalty_points(), 100)

class TestBookingService(unittest.TestCase):
    def setUp(self):
        self.room_repo = InMemoryRoomRepository()
        self.guest_repo = InMemoryGuestRepository()
        self.booking_repo = InMemoryBookingRepository()
        self.service = BookingService(self.booking_repo, self.room_repo, self.guest_repo)
        
        # Create test data
        self.room = self.room_repo.save_with_return(Room("R001", "101", RoomType.STANDARD, 100.0, 1, 2))
        self.guest = self.guest_repo.save_with_return(Guest("G001", "John", "Doe", "john@example.com", "1234567890"))
        self.check_in = date.today() + timedelta(days=7)
        self.check_out = date.today() + timedelta(days=10)
    
    def save_with_return(self, entity):
        # Helper to save and return entity with ID
        self.booking_repo.save(entity)
        return entity
    
    def test_create_booking_success(self):
        booking = self.service.create_booking(
            "B001", "G001", "R001", self.check_in, self.check_out, 2
        )
        self.assertEqual(booking.get_booking_id(), "B001")
    
    def test_create_booking_past_dates_fails(self):
        past_check_in = date.today() - timedelta(days=7)
        past_check_out = date.today() - timedelta(days=5)
        with self.assertRaises(ValueError):
            self.service.create_booking(
                "B001", "G001", "R001", past_check_in, past_check_out, 2
            )
    
    def test_create_booking_check_in_after_check_out_fails(self):
        with self.assertRaises(ValueError):
            self.service.create_booking(
                "B001", "G001", "R001", self.check_out, self.check_in, 2
            )
    
    def test_create_booking_exceeds_max_guests_fails(self):
        with self.assertRaises(ValueError):
            self.service.create_booking(
                "B001", "G001", "R001", self.check_in, self.check_out, 10
            )
    
    def test_confirm_booking(self):
        booking = self.service.create_booking(
            "B001", "G001", "R001", self.check_in, self.check_out, 2
        )
        confirmed = self.service.confirm_booking("B001")
        self.assertEqual(confirmed.get_status(), BookingStatus.CONFIRMED)
    
    def test_cancel_booking(self):
        booking = self.service.create_booking(
            "B001", "G001", "R001", self.check_in, self.check_out, 2
        )
        cancelled = self.service.cancel_booking("B001")
        self.assertEqual(cancelled.get_status(), BookingStatus.CANCELLED)


from services.service_request_service import ServiceRequestService, StaffNotificationService
from repositories.inmemory.in_memory_service_request_repository import InMemoryServiceRequestRepository
from src.service_request import RequestCategory, RequestStatus

class TestServiceRequestService(unittest.TestCase):
    def setUp(self):
        self.repo = InMemoryServiceRequestRepository()
        self.notifications = StaffNotificationService()
        self.service = ServiceRequestService(self.repo, self.notifications)

    def test_create_service_request_success(self):
        request = self.service.create_service_request(
            "guest-001", "205", RequestCategory.HOUSEKEEPING, "Please bring extra towels"
        )

        self.assertEqual(request.get_guest_id(), "guest-001")
        self.assertEqual(request.get_room_number(), "205")
        self.assertEqual(request.get_status(), RequestStatus.PENDING)
        self.assertEqual(self.repo.count(), 1)

    def test_estimated_completion_time_by_category(self):
        housekeeping = self.service.create_service_request("guest-001", "205", RequestCategory.HOUSEKEEPING)
        room_service = self.service.create_service_request("guest-002", "206", RequestCategory.ROOM_SERVICE)
        maintenance = self.service.create_service_request("guest-003", "207", RequestCategory.MAINTENANCE)

        self.assertEqual(housekeeping.get_estimated_completion_minutes(), 15)
        self.assertEqual(room_service.get_estimated_completion_minutes(), 30)
        self.assertEqual(maintenance.get_estimated_completion_minutes(), 45)

    def test_invalid_category_rejected(self):
        with self.assertRaises(ValueError):
            self.service.create_service_request("guest-001", "205", "SPA")

    def test_staff_notification_is_generated(self):
        self.service.create_service_request("guest-001", "205", RequestCategory.HOUSEKEEPING)

        self.assertEqual(
            self.service.get_staff_notifications(),
            ["New HOUSEKEEPING request for room 205"],
        )

if __name__ == "__main__":
    unittest.main()
