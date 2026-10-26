from enum import StrEnum


class OpsdutyApiV1StatuspagesListStatusPageIncidentsTypeType0(StrEnum):
    PLANNED = "planned"
    UNPLANNED = "unplanned"

    def __str__(self) -> str:
        return str(self.value)
