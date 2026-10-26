from enum import StrEnum


class IncidentGroupStatus(StrEnum):
    ACKNOWLEDGED = "acknowledged"
    RESOLVED = "resolved"
    SILENCED = "silenced"
    TRIGGERED = "triggered"

    def __str__(self) -> str:
        return str(self.value)
