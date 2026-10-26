from enum import StrEnum


class StatusPageAccessMode(StrEnum):
    CUSTOM_BACKEND = "custom_backend"
    OPSDUTY_MEMBERS = "opsduty_members"
    PUBLIC = "public"

    def __str__(self) -> str:
        return str(self.value)
