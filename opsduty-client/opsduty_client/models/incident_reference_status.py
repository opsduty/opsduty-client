from enum import StrEnum


class IncidentReferenceStatus(StrEnum):
    COMPLETED = "completed"
    FAILED = "failed"
    PENDING = "pending"
    STOPPED = "stopped"

    def __str__(self) -> str:
        return str(self.value)
