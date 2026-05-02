import unittest
from datetime import date, timedelta
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from creational_patterns.simple_factory import RoomFactory
from creational_patterns.factory_method import CreditCardProcessorFactory, PayPalProcessorFactory, process_payment_with_factory
from creational_patterns.abstract_factory import StandardAmenityFactory, PremiumAmenityFactory, RoomAmenitySet
from creational_patterns.builder import BookingBuilder
from creational_patterns.prototype import RoomTemplateCache
from creational_patterns.singleton import DatabaseConnection, ConfigurationManager
from src.room import RoomType
from src.guest import Guest
from src.room import Room

class TestSimpleFactory(unittest.TestCase):
    def test_standard_room(self):
        room = RoomFactory.create_room(RoomType.STANDARD, "R001", "101", 1)
        self.assertEqual(room.get_price_per_night(), 100.0)
    def test_deluxe_room(self):
        room = RoomFactory.create_room(RoomType.DELUXE, "R002", "201", 2)
        self.assertEqual(room.get_price_per_night(), 200.0)

class TestFactoryMethod(unittest.TestCase):
    def test_credit_card(self):
        self.assertTrue(process_payment_with_factory(CreditCardProcessorFactory(), 100))
    def test_paypal(self):
        self.assertTrue(process_payment_with_factory(PayPalProcessorFactory(), 50))

class TestAbstractFactory(unittest.TestCase):
    def test_standard_amenities(self):
        suite = RoomAmenitySet(StandardAmenityFactory())
        self.assertIn("Towel", suite.describe())
    def test_premium_amenities(self):
        suite = RoomAmenitySet(PremiumAmenityFactory())
        self.assertIn("Luxury", suite.describe())

class TestBuilder(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("G001", "John", "Doe", "j@d.com", "123")
        self.room = Room("R001", "101", RoomType.DELUXE, 200.0, 1, 4)
    def test_build_booking(self):
        builder = BookingBuilder("B001", self.guest, self.room)
        booking = builder.set_dates(date.today(), date.today()+timedelta(days=2)).build()
        self.assertIsNotNone(booking)
    def test_max_guests_validation(self):
        builder = BookingBuilder("B001", self.guest, self.room)
        with self.assertRaises(ValueError):
            builder.set_number_of_guests(10)

class TestPrototype(unittest.TestCase):
    def test_clone(self):
        RoomTemplateCache.load_templates()
        orig = RoomTemplateCache.get_room_template("deluxe")
        clone = RoomTemplateCache.get_room_template("deluxe")
        self.assertIsNot(orig, clone)

class TestSingleton(unittest.TestCase):
    def test_db_singleton(self):
        db1 = DatabaseConnection()
        db2 = DatabaseConnection()
        self.assertIs(db1, db2)
    def test_config_singleton(self):
        c1 = ConfigurationManager()
        c2 = ConfigurationManager()
        self.assertIs(c1, c2)

if __name__ == "__main__":
    unittest.main()
