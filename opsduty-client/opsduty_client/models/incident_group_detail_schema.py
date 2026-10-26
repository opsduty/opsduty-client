from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define, field as _attrs_field

from ..models.incident_group_status import IncidentGroupStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.incident_group_detail_note_schema import IncidentGroupDetailNoteSchema
    from ..models.incident_group_service_schema import IncidentGroupServiceSchema


T = TypeVar("T", bound="IncidentGroupDetailSchema")


@_attrs_define
class IncidentGroupDetailSchema:
    """
    Attributes:
        status (IncidentGroupStatus):
        service (IncidentGroupServiceSchema | None):
        notes (list[IncidentGroupDetailNoteSchema]):
        created_at (datetime.datetime):
        id (int | None | Unset):
        incident_number (int | Unset):  Default: 0.
        summary (None | str | Unset):
        acknowledged_at (datetime.datetime | None | Unset):
        resolved_at (datetime.datetime | None | Unset):
        silenced_at (datetime.datetime | None | Unset):
        last_status_change_at (datetime.datetime | None | Unset):
    """

    status: IncidentGroupStatus
    service: IncidentGroupServiceSchema | None
    notes: list[IncidentGroupDetailNoteSchema]
    created_at: datetime.datetime
    id: int | None | Unset = UNSET
    incident_number: int | Unset = 0
    summary: None | str | Unset = UNSET
    acknowledged_at: datetime.datetime | None | Unset = UNSET
    resolved_at: datetime.datetime | None | Unset = UNSET
    silenced_at: datetime.datetime | None | Unset = UNSET
    last_status_change_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.incident_group_service_schema import IncidentGroupServiceSchema  # noqa: PLC0415

        status = self.status.value

        service: dict[str, Any] | None
        if isinstance(self.service, IncidentGroupServiceSchema):
            service = self.service.to_dict()
        else:
            service = self.service

        notes = []
        for notes_item_data in self.notes:
            notes_item = notes_item_data.to_dict()
            notes.append(notes_item)

        created_at = self.created_at.isoformat()

        id: int | None | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        incident_number = self.incident_number

        summary: None | str | Unset
        if isinstance(self.summary, Unset):
            summary = UNSET
        else:
            summary = self.summary

        acknowledged_at: None | str | Unset
        if isinstance(self.acknowledged_at, Unset):
            acknowledged_at = UNSET
        elif isinstance(self.acknowledged_at, datetime.datetime):
            acknowledged_at = self.acknowledged_at.isoformat()
        else:
            acknowledged_at = self.acknowledged_at

        resolved_at: None | str | Unset
        if isinstance(self.resolved_at, Unset):
            resolved_at = UNSET
        elif isinstance(self.resolved_at, datetime.datetime):
            resolved_at = self.resolved_at.isoformat()
        else:
            resolved_at = self.resolved_at

        silenced_at: None | str | Unset
        if isinstance(self.silenced_at, Unset):
            silenced_at = UNSET
        elif isinstance(self.silenced_at, datetime.datetime):
            silenced_at = self.silenced_at.isoformat()
        else:
            silenced_at = self.silenced_at

        last_status_change_at: None | str | Unset
        if isinstance(self.last_status_change_at, Unset):
            last_status_change_at = UNSET
        elif isinstance(self.last_status_change_at, datetime.datetime):
            last_status_change_at = self.last_status_change_at.isoformat()
        else:
            last_status_change_at = self.last_status_change_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
                "service": service,
                "notes": notes,
                "created_at": created_at,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if incident_number is not UNSET:
            field_dict["incident_number"] = incident_number
        if summary is not UNSET:
            field_dict["summary"] = summary
        if acknowledged_at is not UNSET:
            field_dict["acknowledged_at"] = acknowledged_at
        if resolved_at is not UNSET:
            field_dict["resolved_at"] = resolved_at
        if silenced_at is not UNSET:
            field_dict["silenced_at"] = silenced_at
        if last_status_change_at is not UNSET:
            field_dict["last_status_change_at"] = last_status_change_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.incident_group_detail_note_schema import IncidentGroupDetailNoteSchema  # noqa: PLC0415
        from ..models.incident_group_service_schema import IncidentGroupServiceSchema  # noqa: PLC0415

        d = dict(src_dict)
        status = IncidentGroupStatus(d.pop("status"))

        def _parse_service(data: object) -> IncidentGroupServiceSchema | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                service_type_0 = IncidentGroupServiceSchema.from_dict(data)

                return service_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(IncidentGroupServiceSchema | None, data)

        service = _parse_service(d.pop("service"))

        notes = []
        _notes = d.pop("notes")
        for notes_item_data in _notes:
            notes_item = IncidentGroupDetailNoteSchema.from_dict(notes_item_data)

            notes.append(notes_item)

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        def _parse_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        id = _parse_id(d.pop("id", UNSET))

        incident_number = d.pop("incident_number", UNSET)

        def _parse_summary(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        summary = _parse_summary(d.pop("summary", UNSET))

        def _parse_acknowledged_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                acknowledged_at_type_0 = datetime.datetime.fromisoformat(data)

                return acknowledged_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        acknowledged_at = _parse_acknowledged_at(d.pop("acknowledged_at", UNSET))

        def _parse_resolved_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                resolved_at_type_0 = datetime.datetime.fromisoformat(data)

                return resolved_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        resolved_at = _parse_resolved_at(d.pop("resolved_at", UNSET))

        def _parse_silenced_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                silenced_at_type_0 = datetime.datetime.fromisoformat(data)

                return silenced_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        silenced_at = _parse_silenced_at(d.pop("silenced_at", UNSET))

        def _parse_last_status_change_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_status_change_at_type_0 = datetime.datetime.fromisoformat(data)

                return last_status_change_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_status_change_at = _parse_last_status_change_at(d.pop("last_status_change_at", UNSET))

        incident_group_detail_schema = cls(
            status=status,
            service=service,
            notes=notes,
            created_at=created_at,
            id=id,
            incident_number=incident_number,
            summary=summary,
            acknowledged_at=acknowledged_at,
            resolved_at=resolved_at,
            silenced_at=silenced_at,
            last_status_change_at=last_status_change_at,
        )

        incident_group_detail_schema.additional_properties = d
        return incident_group_detail_schema

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
