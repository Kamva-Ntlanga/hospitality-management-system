import unittest
from datetime import date, timedelta
from src.room import Room, RoomType, RoomStatus
from src.guest import Guest
from src.booking import Booking, BookingStatus
from src.payment import Payment, PaymentMethod
from repositories.inmemory.in_memory_room_repository import InMemoryRoomRepository
from repositories.inmemory.in_memory_guest_repository import InMemoryGuestRepository
from repositories.inmemory.in_memory_booking_repository import InMemoryBookingRepository

class TestInMemoryRoomRepository(unittest.TestCase):
    def setUp(self):
        self.repo = InMemoryRoomRepository()
        self.room1 = Room("R001", "101", RoomType.STANDARD, 100.0, 1, 2)
        self.room2 = Room("R002", "102", RoomType.DELUXE, 200.0, 1, 4)
        self.room3 = Room("R003", "103", RoomType.SUITE, 350.0, 1, 6)
    
    def test_save_and_find_by_id(self):
        self.repo.save(self.room1)
        found = self.repo.find_by_id("R001")
        self.assertIsNotNone(found)
        self.assertEqual(found.get_room_number(), "101")
    
    def test_find_all(self):
        self.repo.save(self.room1)
        self.repo.save(self.room2)
        all_rooms = self.repo.find_all()
        self.assertEqual(len(all_rooms), 2)
    
    def test_delete(self):
        self.repo.save(self.room1)
        self.repo.delete("R001")
        found = self.repo.find_by_id("R001")
        self.assertIsNone(found)
    
    def test_find_available_rooms(self):
        self.repo.save(self.room1)
        self.repo.save(self.room2)
        self.repo.save(self.room3)
        self.room2.update_status(RoomStatus.BOOKED)
        available = self.repo.find_available_rooms()
        self.assertEqual(len(available), 2)
    
    def test_count(self):
        self.repo.save(self.room1)
        self.repo.save(self.room2)
        self.assertEqual(self.repo.count(), 2)

class TestInMemoryGuestRepository(unittest.TestCase):
    def setUp(self):
        self.repo = InMemoryGuestRepository()
        self.guest1 = Guest("G001", "John", "Doe", "john@example.com", "123456")
        self.guest2 = Guest("G002", "Jane", "Smith", "jane@example.com", "789012")
    
    def test_save_and_find_by_email(self):
        self.repo.save(self.guest1)
        found = self.repo.find_by_email("john@example.com")
        self.assertIsNotNone(found)
        self.assertEqual(found.get_first_name(), "John")
    
    def test_find_by_loyalty_points_range(self):
        self.repo.save(self.guest1)
        self.repo.save(self.guest2)
        self.guest1.add_loyalty_points(100)
        self.guest2.add_loyalty_points(300)
        result = self.repo.find_by_loyalty_points_range(50, 200)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].get_guest_id(), "G001")

class TestInMemoryBookingRepository(unittest.TestCase):
    def setUp(self):
        self.repo = InMemoryBookingRepository()
        self.room = Room("R001", "101", RoomType.STANDARD, 100.0, 1, 2)
        self.guest = Guest("G001", "John", "Doe", "john@example.com", "123456")
        self.check_in = date.today() + timedelta(days=7)
        self.check_out = date.today() + timedelta(days=10)
        self.booking = Booking("B001", self.guest, self.room, self.check_in, self.check_out, 2)
    
    def test_save_and_find_by_id(self):
        self.repo.save(self.booking)
        found = self.repo.find_by_id("B001")
        self.assertIsNotNone(found)
        self.assertEqual(found.get_booking_id(), "B001")
    
    def test_find_upcoming_bookings(self):
        self.repo.save(self.booking)
        upcoming = self.repo.find_upcoming_bookings()
        self.assertEqual(len(upcoming), 1)
    
    def test_find_by_guest_id(self):
        self.repo.save(self.booking)
        by_guest = self.repo.find_by_guest_id("G001")
        self.assertEqual(len(by_guest), 1)

if __name__ == "__main__":
    unittest.main()
