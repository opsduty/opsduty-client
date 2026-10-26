from enum import StrEnum


class IncidentImpact(StrEnum):
    CRITICAL = "critical"
    MAINTENANCE = "maintenance"
    MAJOR = "major"
    MINOR = "minor"
    NONE = "none"

    def __str__(self) -> str:
        return str(self.value)
