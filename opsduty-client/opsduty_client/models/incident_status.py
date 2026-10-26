from enum import StrEnum


class IncidentStatus(StrEnum):
    COMPLETED = "completed"
    IDENTIFIED = "identified"
    INVESTIGATING = "investigating"
    IN_PROGRESS = "in_progress"
    MONITORING = "monitoring"
    RESOLVED = "resolved"
    SCHEDULED = "scheduled"
    VERIFYING = "verifying"

    def __str__(self) -> str:
        return str(self.value)
