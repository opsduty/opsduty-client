from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define, field as _attrs_field

from ..models.incident_status import IncidentStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="IncidentUpdateSchema")


@_attrs_define
class IncidentUpdateSchema:
    """
    Attributes:
        status (IncidentStatus | None): Where the incident stood right after this update was posted. Null on updates
            posted before statuses were recorded.
        visible (bool): Whether customers can read this update yet. One scheduled for later, or never given a display
            time, stays off the public page until then.
        published_at (datetime.datetime | None): When the update went out and any status change it carries was applied.
            Null while a scheduled update waits for its display time.
        body (str):
        created_at (datetime.datetime):
        id (int | None | Unset):
        display_at (datetime.datetime | None | Unset):
    """

    status: IncidentStatus | None
    visible: bool
    published_at: datetime.datetime | None
    body: str
    created_at: datetime.datetime
    id: int | None | Unset = UNSET
    display_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status: None | str
        if isinstance(self.status, IncidentStatus):
            status = self.status.value
        else:
            status = self.status

        visible = self.visible

        published_at: None | str
        if isinstance(self.published_at, datetime.datetime):
            published_at = self.published_at.isoformat()
        else:
            published_at = self.published_at

        body = self.body

        created_at = self.created_at.isoformat()

        id: int | None | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        display_at: None | str | Unset
        if isinstance(self.display_at, Unset):
            display_at = UNSET
        elif isinstance(self.display_at, datetime.datetime):
            display_at = self.display_at.isoformat()
        else:
            display_at = self.display_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
                "visible": visible,
                "published_at": published_at,
                "body": body,
                "created_at": created_at,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if display_at is not UNSET:
            field_dict["display_at"] = display_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_status(data: object) -> IncidentStatus | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                status_type_0 = IncidentStatus(data)

                return status_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(IncidentStatus | None, data)

        status = _parse_status(d.pop("status"))

        visible = d.pop("visible")

        def _parse_published_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                published_at_type_0 = datetime.datetime.fromisoformat(data)

                return published_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        published_at = _parse_published_at(d.pop("published_at"))

        body = d.pop("body")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        def _parse_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        id = _parse_id(d.pop("id", UNSET))

        def _parse_display_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                display_at_type_0 = datetime.datetime.fromisoformat(data)

                return display_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        display_at = _parse_display_at(d.pop("display_at", UNSET))

        incident_update_schema = cls(
            status=status,
            visible=visible,
            published_at=published_at,
            body=body,
            created_at=created_at,
            id=id,
            display_at=display_at,
        )

        incident_update_schema.additional_properties = d
        return incident_update_schema

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
