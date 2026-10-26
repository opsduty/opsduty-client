from enum import StrEnum


class ComponentStatus(StrEnum):
    DEGRADED_PERFORMANCE = "degraded_performance"
    MAJOR_OUTAGE = "major_outage"
    OPERATIONAL = "operational"
    PARTIAL_OUTAGE = "partial_outage"
    UNDER_MAINTENANCE = "under_maintenance"

    def __str__(self) -> str:
        return str(self.value)
