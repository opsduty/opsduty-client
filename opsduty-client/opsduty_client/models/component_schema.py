from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define, field as _attrs_field

from ..models.component_status import ComponentStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="ComponentSchema")


@_attrs_define
class ComponentSchema:
    """
    Attributes:
        status (ComponentStatus):
        component_group_id (int): The component group this component is shown under.
        service_ids (list[int]): The OpsDuty services this component represents.
        name (str):
        id (int | None | Unset):
        description (None | str | Unset):
    """

    status: ComponentStatus
    component_group_id: int
    service_ids: list[int]
    name: str
    id: int | None | Unset = UNSET
    description: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status.value

        component_group_id = self.component_group_id

        service_ids = self.service_ids

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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
                "component_group_id": component_group_id,
                "service_ids": service_ids,
                "name": name,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        status = ComponentStatus(d.pop("status"))

        component_group_id = d.pop("component_group_id")

        service_ids = cast(list[int], d.pop("service_ids"))

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

        component_schema = cls(
            status=status,
            component_group_id=component_group_id,
            service_ids=service_ids,
            name=name,
            id=id,
            description=description,
        )

        component_schema.additional_properties = d
        return component_schema

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
