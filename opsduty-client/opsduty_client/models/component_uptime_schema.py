from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define, field as _attrs_field

T = TypeVar("T", bound="ComponentUptimeSchema")


@_attrs_define
class ComponentUptimeSchema:
    """
    Attributes:
        component_id (int):
        name (str):
        uptime (float): The share of the last ninety days this component was not showing an outage, as a percentage.
            Announced maintenance does not count against it.
    """

    component_id: int
    name: str
    uptime: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        component_id = self.component_id

        name = self.name

        uptime = self.uptime

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "component_id": component_id,
                "name": name,
                "uptime": uptime,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        component_id = d.pop("component_id")

        name = d.pop("name")

        uptime = d.pop("uptime")

        component_uptime_schema = cls(
            component_id=component_id,
            name=name,
            uptime=uptime,
        )

        component_uptime_schema.additional_properties = d
        return component_uptime_schema

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
