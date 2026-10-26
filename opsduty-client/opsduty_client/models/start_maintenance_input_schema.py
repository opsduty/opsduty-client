from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define, field as _attrs_field

from ..models.maintenance_mode import MaintenanceMode
from ..types import UNSET, Unset

T = TypeVar("T", bound="StartMaintenanceInputSchema")


@_attrs_define
class StartMaintenanceInputSchema:
    """
    Attributes:
        mode (MaintenanceMode | Unset):  Default: MaintenanceMode.MAINTENANCE.
        duration_minutes (int | Unset): How long maintenance mode stays active before it ends by itself, in minutes. At
            most 24 hours. Default: 60.
    """

    mode: MaintenanceMode | Unset = MaintenanceMode.MAINTENANCE
    duration_minutes: int | Unset = 60
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mode: str | Unset = UNSET
        if not isinstance(self.mode, Unset):
            mode = self.mode.value

        duration_minutes = self.duration_minutes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mode is not UNSET:
            field_dict["mode"] = mode
        if duration_minutes is not UNSET:
            field_dict["duration_minutes"] = duration_minutes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _mode = d.pop("mode", UNSET)
        mode: MaintenanceMode | Unset
        if isinstance(_mode, Unset):
            mode = UNSET
        else:
            mode = MaintenanceMode(_mode)

        duration_minutes = d.pop("duration_minutes", UNSET)

        start_maintenance_input_schema = cls(
            mode=mode,
            duration_minutes=duration_minutes,
        )

        start_maintenance_input_schema.additional_properties = d
        return start_maintenance_input_schema

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
