from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define, field as _attrs_field

from ..models.incident_reference_status import IncidentReferenceStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="IncidentReferenceSchema")


@_attrs_define
class IncidentReferenceSchema:
    """
    Attributes:
        status (IncidentReferenceStatus): The status of an incident reference.
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        id (None | str | Unset):
        reason (None | str | Unset):
        incident_group (int | None | Unset):
    """

    status: IncidentReferenceStatus
    created_at: datetime.datetime
    updated_at: datetime.datetime
    id: None | str | Unset = UNSET
    reason: None | str | Unset = UNSET
    incident_group: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status.value

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        reason: None | str | Unset
        if isinstance(self.reason, Unset):
            reason = UNSET
        else:
            reason = self.reason

        incident_group: int | None | Unset
        if isinstance(self.incident_group, Unset):
            incident_group = UNSET
        else:
            incident_group = self.incident_group

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if reason is not UNSET:
            field_dict["reason"] = reason
        if incident_group is not UNSET:
            field_dict["incident_group"] = incident_group

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        status = IncidentReferenceStatus(d.pop("status"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        def _parse_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        id = _parse_id(d.pop("id", UNSET))

        def _parse_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        reason = _parse_reason(d.pop("reason", UNSET))

        def _parse_incident_group(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        incident_group = _parse_incident_group(d.pop("incident_group", UNSET))

        incident_reference_schema = cls(
            status=status,
            created_at=created_at,
            updated_at=updated_at,
            id=id,
            reason=reason,
            incident_group=incident_group,
        )

        incident_reference_schema.additional_properties = d
        return incident_reference_schema

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
