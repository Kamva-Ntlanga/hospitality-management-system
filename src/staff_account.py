from enum import Enum
from datetime import datetime
from typing import List

class Role(Enum):
    MANAGER = "Manager"
    FRONT_DESK = "FrontDesk"
    HOUSEKEEPING = "Housekeeping"
    FINANCE = "Finance"
    IT = "IT"

class StaffAccount:
    def __init__(self, staff_id: str, username: str, password: str, role: Role):
        self._staff_id = staff_id
        self._username = username
        self._password_hash = self._hash_password(password)
        self._role = role
        self._permissions = self._get_default_permissions(role)
        self._is_active = True
        self._last_login = None
        self._failed_login_attempts = 0

    def _hash_password(self, password: str) -> str:
        return f"hashed_{password}"

    def _get_default_permissions(self, role: Role) -> List[str]:
        permissions_map = {
            Role.MANAGER: ["view_reports", "manage_staff", "view_dashboard", "create_promotions"],
            Role.FRONT_DESK: ["search_rooms", "create_booking", "process_payment", "manage_housekeeping"],
            Role.HOUSEKEEPING: ["view_tasks", "update_task_status", "report_issue"],
            Role.FINANCE: ["view_financial_reports", "process_refunds"],
            Role.IT: ["manage_staff_accounts", "view_system_logs", "manage_notifications"]
        }
        return permissions_map.get(role, [])

    def get_staff_id(self) -> str:
        return self._staff_id

    def get_username(self) -> str:
        return self._username

    def get_role(self) -> Role:
        return self._role

    def is_active(self) -> bool:
        return self._is_active

    def login(self, password: str) -> bool:
        if not self._is_active:
            return False
        if self._password_hash == self._hash_password(password):
            self._last_login = datetime.now()
            self._failed_login_attempts = 0
            return True
        self._failed_login_attempts += 1
        if self._failed_login_attempts >= 5:
            self._is_active = False
        return False

    def logout(self) -> None:
        self._last_login = None

    def reset_password(self, new_password: str) -> None:
        self._password_hash = self._hash_password(new_password)
        self._failed_login_attempts = 0
        self._is_active = True

    def has_permission(self, permission: str) -> bool:
        return permission in self._permissions

    def deactivate(self) -> None:
        self._is_active = False

    def activate(self) -> None:
        self._is_active = True
        self._failed_login_attempts = 0

    def __str__(self) -> str:
        return f"Staff: {self._username} ({self._role.value}) - {'Active' if self._is_active else 'Inactive'}"
