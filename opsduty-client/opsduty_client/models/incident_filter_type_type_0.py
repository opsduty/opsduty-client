from enum import StrEnum


class IncidentFilterTypeType0(StrEnum):
    PLANNED = "planned"
    UNPLANNED = "unplanned"

    def __str__(self) -> str:
        return str(self.value)
