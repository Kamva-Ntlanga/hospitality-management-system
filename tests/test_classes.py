import unittest
from datetime import date
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.room import Room, RoomType, RoomStatus
from src.guest import Guest
from src.booking import Booking, BookingStatus
from src.payment import Payment, PaymentMethod, PaymentStatus
from src.housekeeping_task import HousekeepingTask, TaskStatus, Priority
from src.service_request import ServiceRequest, RequestCategory, RequestStatus
from src.staff_account import StaffAccount, Role

class TestRoom(unittest.TestCase):
    def test_room_creation(self):
        r = Room("R01", "101", RoomType.STANDARD, 100.0, 1, 2)
        self.assertEqual(r.get_room_number(), "101")
        self.assertTrue(r.is_available())
    def test_update_status(self):
        r = Room("R01", "101", RoomType.STANDARD, 100.0, 1, 2)
        r.update_status(RoomStatus.BOOKED)
        self.assertFalse(r.is_available())
    def test_price_calculation(self):
        r = Room("R01", "101", RoomType.STANDARD, 100.0, 1, 2)
        total = r.get_price_for_dates(date(2025,5,1), date(2025,5,5))
        self.assertEqual(total, 400.0)

class TestGuest(unittest.TestCase):
    def test_guest_creation(self):
        g = Guest("G01", "Alice", "Smith", "a@b.com", "123")
        self.assertEqual(g.get_first_name(), "Alice")
    def test_loyalty_points(self):
        g = Guest("G01", "Alice", "Smith", "a@b.com", "123")
        g.add_loyalty_points(100)
        self.assertEqual(g.get_loyalty_points(), 100)

class TestBooking(unittest.TestCase):
    def setUp(self):
        self.room = Room("R01", "101", RoomType.STANDARD, 100.0, 1, 2)
        self.guest = Guest("G01", "Bob", "Jones", "b@c.com", "456")
        self.ci = date(2025,6,1)
        self.co = date(2025,6,3)
    def test_booking_creation(self):
        b = Booking("B01", self.guest, self.room, self.ci, self.co, 1)
        self.assertEqual(b.get_status(), BookingStatus.PENDING)
        self.assertEqual(b.calculate_total(), 200.0)
    def test_confirm_booking(self):
        b = Booking("B01", self.guest, self.room, self.ci, self.co, 1)
        b.calculate_total()
        self.assertTrue(b.confirm_booking())
        self.assertEqual(self.room.get_status(), RoomStatus.BOOKED)
    def test_cancel_booking(self):
        b = Booking("B01", self.guest, self.room, self.ci, self.co, 1)
        b.confirm_booking()
        self.assertTrue(b.cancel_booking())
        self.assertEqual(b.get_status(), BookingStatus.CANCELLED)
    def test_check_in_out(self):
        b = Booking("B01", self.guest, self.room, self.ci, self.co, 1)
        b.calculate_total()
        b.confirm_booking()
        self.assertTrue(b.check_in())
        self.assertEqual(b.get_status(), BookingStatus.CHECKED_IN)
        self.assertTrue(b.check_out())
        self.assertEqual(b.get_status(), BookingStatus.COMPLETED)

class TestPayment(unittest.TestCase):
    def test_payment_flow(self):
        room = Room("R01", "101", RoomType.STANDARD, 100.0, 1, 2)
        guest = Guest("G01", "Charlie", "Brown", "c@d.com", "789")
        ci = date(2025,7,1)
        co = date(2025,7,2)
        b = Booking("B01", guest, room, ci, co, 1)
        b.calculate_total()
        p = Payment("P01", b.get_total_price(), PaymentMethod.CREDIT_CARD, b)
        self.assertTrue(p.authorize())
        self.assertEqual(p.get_status(), PaymentStatus.AUTHORIZED)
        self.assertTrue(p.capture())
        self.assertEqual(p.get_status(), PaymentStatus.CAPTURED)

class TestHousekeepingTask(unittest.TestCase):
    def test_task_lifecycle(self):
        room = Room("R01", "101", RoomType.STANDARD, 100.0, 1, 2)
        task = HousekeepingTask("T01", room, Priority.HIGH)
        task.start_task()
        self.assertEqual(task.get_status(), TaskStatus.IN_PROGRESS)
        task.complete_task()
        self.assertEqual(task.get_status(), TaskStatus.COMPLETED)

class TestServiceRequest(unittest.TestCase):
    def test_request_flow(self):
        room = Room("R01", "101", RoomType.STANDARD, 100.0, 1, 2)
        guest = Guest("G01", "Diana", "Prince", "d@e.com", "000")
        req = ServiceRequest("SR01", guest, room, RequestCategory.ROOM_SERVICE, "Coffee")
        req.acknowledge()
        self.assertEqual(req.get_status(), RequestStatus.ACKNOWLEDGED)

class TestStaffAccount(unittest.TestCase):
    def test_login_lockout(self):
        staff = StaffAccount("S01", "mgr", "pass", Role.MANAGER)
        for _ in range(5):
            staff.login("wrong")
        self.assertFalse(staff.is_active())
    def test_reset_password(self):
        staff = StaffAccount("S01", "mgr", "pass", Role.MANAGER)
        staff.reset_password("new")
        self.assertTrue(staff.login("new"))
    def test_permissions(self):
        staff = StaffAccount("S01", "mgr", "pass", Role.MANAGER)
        self.assertTrue(staff.has_permission("view_reports"))

if __name__ == "__main__":
    unittest.main()
