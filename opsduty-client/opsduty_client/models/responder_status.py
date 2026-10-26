from enum import StrEnum


class ResponderStatus(StrEnum):
    ACTIVE = "active"
    PENDING = "pending"

    def __str__(self) -> str:
        return str(self.value)
