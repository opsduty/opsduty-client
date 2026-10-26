from enum import StrEnum


class OrderedModelMovement(StrEnum):
    BOTTOM = "bottom"
    DOWN = "down"
    TOP = "top"
    UP = "up"

    def __str__(self) -> str:
        return str(self.value)
