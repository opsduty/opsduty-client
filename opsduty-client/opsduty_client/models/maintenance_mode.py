from enum import StrEnum


class MaintenanceMode(StrEnum):
    DEBUG = "debug"
    MAINTENANCE = "maintenance"

    def __str__(self) -> str:
        return str(self.value)
