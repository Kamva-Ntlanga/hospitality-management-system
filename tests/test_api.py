import unittest
from datetime import date, timedelta
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)

class TestRoomAPI(unittest.TestCase):
    
    def test_create_and_get_room(self):
        # Create room
        response = client.post("/api/rooms", json={
            "room_id": "R001",
            "room_number": "101",
            "room_type": "Standard",
            "price_per_night": 100.0,
            "floor": 1,
            "max_guests": 2
        })
        self.assertEqual(response.status_code, 201)
        
        # Get room
        response = client.get("/api/rooms/R001")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["room_number"], "101")
    
    def test_get_all_rooms(self):
        response = client.get("/api/rooms")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)
    
    def test_get_room_not_found(self):
        response = client.get("/api/rooms/NOT_EXIST")
        self.assertEqual(response.status_code, 404)
    
    def test_update_room_status(self):
        # Create room
        client.post("/api/rooms", json={
            "room_id": "R002",
            "room_number": "102",
            "room_type": "Deluxe",
            "price_per_night": 200.0,
            "floor": 1,
            "max_guests": 4
        })
        
        # Update status
        response = client.put("/api/rooms/R002/status", json={"status": "Booked"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["status"], "Booked")

class TestGuestAPI(unittest.TestCase):
    
    def test_create_and_get_guest(self):
        # Create guest
        response = client.post("/api/guests", json={
            "guest_id": "G001",
            "first_name": "John",
            "last_name": "Doe",
            "email": "john@example.com",
            "phone": "1234567890"
        })
        self.assertEqual(response.status_code, 201)
        
        # Get guest
        response = client.get("/api/guests/G001")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["email"], "john@example.com")
    
    def test_create_guest_duplicate_email_fails(self):
        # Create first guest
        client.post("/api/guests", json={
            "guest_id": "G002",
            "first_name": "Jane",
            "last_name": "Smith",
            "email": "jane@example.com",
            "phone": "1234567890"
        })
        
        # Create duplicate
        response = client.post("/api/guests", json={
            "guest_id": "G003",
            "first_name": "Janet",
            "last_name": "Smith",
            "email": "jane@example.com",
            "phone": "0987654321"
        })
        self.assertEqual(response.status_code, 400)
    
    def test_add_loyalty_points(self):
        # Create guest
        client.post("/api/guests", json={
            "guest_id": "G004",
            "first_name": "Alice",
            "last_name": "Brown",
            "email": "alice@example.com",
            "phone": "1234567890"
        })
        
        # Add points
        response = client.post("/api/guests/G004/points", json={"points": 100})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["loyalty_points"], 100)

class TestBookingAPI(unittest.TestCase):
    
    def setUp(self):
        # Create test room and guest
        client.post("/api/rooms", json={
            "room_id": "R010",
            "room_number": "110",
            "room_type": "Standard",
            "price_per_night": 100.0,
            "floor": 1,
            "max_guests": 2
        })
        client.post("/api/guests", json={
            "guest_id": "G010",
            "first_name": "Bob",
            "last_name": "Wilson",
            "email": "bob@example.com",
            "phone": "1234567890"
        })
    
    def test_create_booking(self):
        check_in = (date.today() + timedelta(days=7)).isoformat()
        check_out = (date.today() + timedelta(days=10)).isoformat()
        
        response = client.post("/api/bookings", json={
            "booking_id": "B010",
            "guest_id": "G010",
            "room_id": "R010",
            "check_in_date": check_in,
            "check_out_date": check_out,
            "number_of_guests": 2,
            "special_requests": "Extra pillow"
        })
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()["booking_id"], "B010")
    
    def test_confirm_booking(self):
        check_in = (date.today() + timedelta(days=7)).isoformat()
        check_out = (date.today() + timedelta(days=10)).isoformat()
        
        client.post("/api/bookings", json={
            "booking_id": "B011",
            "guest_id": "G010",
            "room_id": "R010",
            "check_in_date": check_in,
            "check_out_date": check_out,
            "number_of_guests": 2
        })
        
        response = client.post("/api/bookings/B011/confirm")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["status"], "Confirmed")

if __name__ == "__main__":
    unittest.main()
