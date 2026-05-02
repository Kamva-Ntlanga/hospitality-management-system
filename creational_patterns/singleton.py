import threading

class DatabaseConnection:
    _instance = None
    _lock = threading.Lock()
    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance._initialize()
        return cls._instance
    def _initialize(self):
        self.connection_string = "localhost:5432/hotelhub"
        self.is_connected = True
        print("Database connection established (Singleton instance created).")
    def query(self, sql: str) -> list:
        if not self.is_connected:
            raise Exception("Not connected to database")
        print(f"Executing query: {sql}")
        return [{"result": "dummy data"}]
    def close(self):
        self.is_connected = False
        print("Database connection closed.")
    def get_connection_string(self) -> str:
        return self.connection_string

class ConfigurationManager:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._load_config()
        return cls._instance
    def _load_config(self):
        self.config = {
            "app_name": "HotelHub",
            "version": "1.0.0",
            "debug": True,
            "max_bookings_per_guest": 5
        }
    def get(self, key: str):
        return self.config.get(key)
    def set(self, key: str, value):
        self.config[key] = value

if __name__ == "__main__":
    db1 = DatabaseConnection()
    db2 = DatabaseConnection()
    print(f"Same instance? {db1 is db2}")
    cfg = ConfigurationManager()
    print(f"App name: {cfg.get('app_name')}")
