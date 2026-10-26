from enum import StrEnum


class HeartbeatType(StrEnum):
    CRON = "cron"
    INTERVAL = "interval"

    def __str__(self) -> str:
        return str(self.value)
