from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define, field as _attrs_field

from ..models.status_page_access_mode import StatusPageAccessMode
from ..types import UNSET, Unset

T = TypeVar("T", bound="StatusPageSchema")


@_attrs_define
class StatusPageSchema:
    """
    Attributes:
        calculate_uptime (bool): Whether this page shows each component's uptime to customers. The figure is worked out
            either way, so a component's `uptime` is populated even when this is false.
        access_mode (StatusPageAccessMode): Who can see a status page on its domain.
        name (str):
        domain (str):
        created_at (datetime.datetime):
        id (int | None | Unset):
        description (None | str | Unset):
        enabled (bool | Unset):  Default: True.
    """

    calculate_uptime: bool
    access_mode: StatusPageAccessMode
    name: str
    domain: str
    created_at: datetime.datetime
    id: int | None | Unset = UNSET
    description: None | str | Unset = UNSET
    enabled: bool | Unset = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        calculate_uptime = self.calculate_uptime

        access_mode = self.access_mode.value

        name = self.name

        domain = self.domain

        created_at = self.created_at.isoformat()

        id: int | None | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        enabled = self.enabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "calculate_uptime": calculate_uptime,
                "access_mode": access_mode,
                "name": name,
                "domain": domain,
                "created_at": created_at,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if description is not UNSET:
            field_dict["description"] = description
        if enabled is not UNSET:
            field_dict["enabled"] = enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        calculate_uptime = d.pop("calculate_uptime")

        access_mode = StatusPageAccessMode(d.pop("access_mode"))

        name = d.pop("name")

        domain = d.pop("domain")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        def _parse_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        id = _parse_id(d.pop("id", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        enabled = d.pop("enabled", UNSET)

        status_page_schema = cls(
            calculate_uptime=calculate_uptime,
            access_mode=access_mode,
            name=name,
            domain=domain,
            created_at=created_at,
            id=id,
            description=description,
            enabled=enabled,
        )

        status_page_schema.additional_properties = d
        return status_page_schema

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
