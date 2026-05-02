import copy
from src.room import Room, RoomType

class RoomTemplateCache:
    _cache = {}
    @staticmethod
    def load_templates():
        standard = Room("TMPL_STD", "TEMPLATE", RoomType.STANDARD, 100.0, 1, 2)
        deluxe = Room("TMPL_DLX", "TEMPLATE", RoomType.DELUXE, 200.0, 1, 4)
        suite = Room("TMPL_STE", "TEMPLATE", RoomType.SUITE, 350.0, 1, 6)
        RoomTemplateCache._cache["standard"] = standard
        RoomTemplateCache._cache["deluxe"] = deluxe
        RoomTemplateCache._cache["suite"] = suite
    @staticmethod
    def get_room_template(template_type: str) -> Room:
        return copy.deepcopy(RoomTemplateCache._cache.get(template_type))
    @staticmethod
    def add_template(key: str, room: Room):
        RoomTemplateCache._cache[key] = room

if __name__ == "__main__":
    RoomTemplateCache.load_templates()
    template = RoomTemplateCache.get_room_template("deluxe")
    template._room_number = "202"
    print(f"Cloned room: {template}")
