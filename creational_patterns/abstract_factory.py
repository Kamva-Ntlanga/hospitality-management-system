from abc import ABC, abstractmethod

class Amenity(ABC):
    @abstractmethod
    def get_name(self) -> str:
        pass

class Towel(Amenity):
    def get_name(self) -> str:
        return "Towel"

class LuxuryTowel(Amenity):
    def get_name(self) -> str:
        return "Luxury Egyptian Cotton Towel"

class Soap(Amenity):
    def get_name(self) -> str:
        return "Soap"

class PremiumSoap(Amenity):
    def get_name(self) -> str:
        return "Premium Organic Soap"

class MinibarItem(Amenity):
    def get_name(self) -> str:
        return "Minibar Item"

class PremiumMinibarItem(Amenity):
    def get_name(self) -> str:
        return "Premium Minibar (Wine & Snacks)"

class RoomAmenityFactory(ABC):
    @abstractmethod
    def create_towel(self) -> Amenity:
        pass
    @abstractmethod
    def create_soap(self) -> Amenity:
        pass
    @abstractmethod
    def create_minibar_item(self) -> Amenity:
        pass

class StandardAmenityFactory(RoomAmenityFactory):
    def create_towel(self) -> Amenity:
        return Towel()
    def create_soap(self) -> Amenity:
        return Soap()
    def create_minibar_item(self) -> Amenity:
        return MinibarItem()

class PremiumAmenityFactory(RoomAmenityFactory):
    def create_towel(self) -> Amenity:
        return LuxuryTowel()
    def create_soap(self) -> Amenity:
        return PremiumSoap()
    def create_minibar_item(self) -> Amenity:
        return PremiumMinibarItem()

class RoomAmenitySet:
    def __init__(self, factory: RoomAmenityFactory):
        self.towel = factory.create_towel()
        self.soap = factory.create_soap()
        self.minibar = factory.create_minibar_item()
    def describe(self) -> str:
        return f"Amenities: {self.towel.get_name()}, {self.soap.get_name()}, {self.minibar.get_name()}"

if __name__ == "__main__":
    standard = RoomAmenitySet(StandardAmenityFactory())
    premium = RoomAmenitySet(PremiumAmenityFactory())
    print("Standard Room:", standard.describe())
    print("Premium Room:", premium.describe())
