from enum import Enum


class ResponderStatus(str, Enum):
    ACTIVE = "active"
    PENDING = "pending"

    def __str__(self) -> str:
        return str(self.value)
