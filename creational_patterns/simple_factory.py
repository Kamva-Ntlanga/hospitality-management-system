import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.room import Room, RoomType

class RoomFactory:
    @staticmethod
    def create_room(room_type: RoomType, room_id: str, room_number: str, 
                    floor: int, price_per_night: float = None) -> Room:
        if price_per_night is None:
            prices = {
                RoomType.STANDARD: 100.0,
                RoomType.DELUXE: 200.0,
                RoomType.SUITE: 350.0
            }
            price_per_night = prices.get(room_type, 150.0)
        max_guests = {
            RoomType.STANDARD: 2,
            RoomType.DELUXE: 4,
            RoomType.SUITE: 6
        }.get(room_type, 2)
        return Room(room_id, room_number, room_type, price_per_night, floor, max_guests)

# Example usage (can be removed)
if __name__ == "__main__":
    std = RoomFactory.create_room(RoomType.STANDARD, "R001", "101", 1)
    print(std)
