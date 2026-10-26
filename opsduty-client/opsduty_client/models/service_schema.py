from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define, field as _attrs_field

from ..models.maintenance_mode import MaintenanceMode
from ..types import UNSET, Unset

T = TypeVar("T", bound="ServiceSchema")


@_attrs_define
class ServiceSchema:
    """
    Attributes:
        maintenance_mode (MaintenanceMode | None):
        maintenance_window_start (datetime.datetime | None):
        maintenance_window_end (datetime.datetime | None):
        routing_key (str): Key you send events to.
        name (str):
        id (int | None | Unset):
        description (None | str | Unset):
        service_type (str | Unset):  Default: 'technical'.
    """

    maintenance_mode: MaintenanceMode | None
    maintenance_window_start: datetime.datetime | None
    maintenance_window_end: datetime.datetime | None
    routing_key: str
    name: str
    id: int | None | Unset = UNSET
    description: None | str | Unset = UNSET
    service_type: str | Unset = "technical"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        maintenance_mode: None | str
        if isinstance(self.maintenance_mode, MaintenanceMode):
            maintenance_mode = self.maintenance_mode.value
        else:
            maintenance_mode = self.maintenance_mode

        maintenance_window_start: None | str
        if isinstance(self.maintenance_window_start, datetime.datetime):
            maintenance_window_start = self.maintenance_window_start.isoformat()
        else:
            maintenance_window_start = self.maintenance_window_start

        maintenance_window_end: None | str
        if isinstance(self.maintenance_window_end, datetime.datetime):
            maintenance_window_end = self.maintenance_window_end.isoformat()
        else:
            maintenance_window_end = self.maintenance_window_end

        routing_key = self.routing_key

        name = self.name

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

        service_type = self.service_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "maintenance_mode": maintenance_mode,
                "maintenance_window_start": maintenance_window_start,
                "maintenance_window_end": maintenance_window_end,
                "routing_key": routing_key,
                "name": name,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if description is not UNSET:
            field_dict["description"] = description
        if service_type is not UNSET:
            field_dict["service_type"] = service_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_maintenance_mode(data: object) -> MaintenanceMode | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                maintenance_mode_type_0 = MaintenanceMode(data)

                return maintenance_mode_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MaintenanceMode | None, data)

        maintenance_mode = _parse_maintenance_mode(d.pop("maintenance_mode"))

        def _parse_maintenance_window_start(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                maintenance_window_start_type_0 = datetime.datetime.fromisoformat(data)

                return maintenance_window_start_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        maintenance_window_start = _parse_maintenance_window_start(d.pop("maintenance_window_start"))

        def _parse_maintenance_window_end(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                maintenance_window_end_type_0 = datetime.datetime.fromisoformat(data)

                return maintenance_window_end_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        maintenance_window_end = _parse_maintenance_window_end(d.pop("maintenance_window_end"))

        routing_key = d.pop("routing_key")

        name = d.pop("name")

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

        service_type = d.pop("service_type", UNSET)

        service_schema = cls(
            maintenance_mode=maintenance_mode,
            maintenance_window_start=maintenance_window_start,
            maintenance_window_end=maintenance_window_end,
            routing_key=routing_key,
            name=name,
            id=id,
            description=description,
            service_type=service_type,
        )

        service_schema.additional_properties = d
        return service_schema

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
