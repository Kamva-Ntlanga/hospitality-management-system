from datetime import date, timedelta
from src.booking import Booking

class BookingBuilder:
    def __init__(self, booking_id: str, guest, room):
        self.booking_id = booking_id
        self.guest = guest
        self.room = room
        self.check_in_date = date.today()
        self.check_out_date = date.today() + timedelta(days=1)
        self.number_of_guests = 1
        self.special_requests = ""
        self.extras = []

    def set_dates(self, check_in: date, check_out: date):
        self.check_in_date = check_in
        self.check_out_date = check_out
        return self

    def set_number_of_guests(self, num: int):
        if num > self.room.get_max_guests():
            raise ValueError(f"Cannot exceed max guests ({self.room.get_max_guests()})")
        self.number_of_guests = num
        return self

    def add_special_requests(self, requests: str):
        self.special_requests = requests
        return self

    def add_extra(self, extra: str):
        self.extras.append(extra)
        return self

    def build(self):
        booking = Booking(
            self.booking_id, self.guest, self.room,
            self.check_in_date, self.check_out_date,
            self.number_of_guests, self.special_requests
        )
        booking._extras = self.extras
        return booking

class BookingDirector:
    @staticmethod
    def create_weekend_getaway(builder: BookingBuilder) -> BookingBuilder:
        return (builder
                .set_dates(date.today(), date.today() + timedelta(days=2))
                .add_extra("Breakfast included")
                .add_extra("Late checkout"))
    @staticmethod
    def create_business_trip(builder: BookingBuilder) -> BookingBuilder:
        return (builder
                .set_dates(date.today(), date.today() + timedelta(days=3))
                .add_extra("High-speed WiFi")
                .add_extra("Workspace setup"))

if __name__ == "__main__":
    from src.guest import Guest
    from src.room import Room, RoomType
    guest = Guest("G001", "John", "Doe", "john@example.com", "123456")
    room = Room("R001", "101", RoomType.DELUXE, 200.0, 1, 4)
    builder = BookingBuilder("B001", guest, room)
    booking = (builder
               .set_dates(date.today(), date.today() + timedelta(days=2))
               .set_number_of_guests(2)
               .add_special_requests("Extra pillows")
               .add_extra("Spa access")
               .build())
    print(f"Created booking: {booking}")
    print(f"Extras: {booking._extras}")
