class Guest:
    def __init__(self, guest_id: str, first_name: str, last_name: str, 
                 email: str, phone: str):
        self._guest_id = guest_id
        self._first_name = first_name
        self._last_name = last_name
        self._email = email
        self._phone = phone
        self._loyalty_points = 0
        self._preferences = ""

    def get_guest_id(self) -> str:
        return self._guest_id

    def get_first_name(self) -> str:
        return self._first_name

    def get_last_name(self) -> str:
        return self._last_name

    def get_email(self) -> str:
        return self._email

    def get_phone(self) -> str:
        return self._phone

    def get_loyalty_points(self) -> int:
        return self._loyalty_points

    def get_preferences(self) -> str:
        return self._preferences

    def update_profile(self, first_name: str = None, last_name: str = None,
                       email: str = None, phone: str = None) -> None:
        if first_name:
            self._first_name = first_name
        if last_name:
            self._last_name = last_name
        if email:
            self._email = email
        if phone:
            self._phone = phone

    def add_loyalty_points(self, points: int) -> None:
        self._loyalty_points += points

    def set_preferences(self, preferences: str) -> None:
        self._preferences = preferences

    def __str__(self) -> str:
        return f"Guest: {self._first_name} {self._last_name} ({self._email})"
