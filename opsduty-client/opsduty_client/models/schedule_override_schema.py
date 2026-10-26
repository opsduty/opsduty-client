from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define, field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.schedule_override_user_schema import ScheduleOverrideUserSchema


T = TypeVar("T", bound="ScheduleOverrideSchema")


@_attrs_define
class ScheduleOverrideSchema:
    """
    Attributes:
        user (ScheduleOverrideUserSchema):
        start (datetime.datetime):
        end (datetime.datetime):
        id (int | None | Unset):
    """

    user: ScheduleOverrideUserSchema
    start: datetime.datetime
    end: datetime.datetime
    id: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        user = self.user.to_dict()

        start = self.start.isoformat()

        end = self.end.isoformat()

        id: int | None | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "user": user,
                "start": start,
                "end": end,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.schedule_override_user_schema import ScheduleOverrideUserSchema  # noqa: PLC0415

        d = dict(src_dict)
        user = ScheduleOverrideUserSchema.from_dict(d.pop("user"))

        start = datetime.datetime.fromisoformat(d.pop("start"))

        end = datetime.datetime.fromisoformat(d.pop("end"))

        def _parse_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        id = _parse_id(d.pop("id", UNSET))

        schedule_override_schema = cls(
            user=user,
            start=start,
            end=end,
            id=id,
        )

        schedule_override_schema.additional_properties = d
        return schedule_override_schema

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
