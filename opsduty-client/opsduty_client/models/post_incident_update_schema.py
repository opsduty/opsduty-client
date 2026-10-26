from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define, field as _attrs_field

from ..models.incident_status import IncidentStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="PostIncidentUpdateSchema")


@_attrs_define
class PostIncidentUpdateSchema:
    """
    Attributes:
        body (str): What has changed since the last update. Markdown is supported.
        status (IncidentStatus | None | Unset): Move the incident to a new status at the same time. Pass 'resolved' to
            close it out.
        display_at (datetime.datetime | None | Unset): Schedule the update for later. It stays off the public page, and
            the status change waits, until this time. Leave it out to post now.
    """

    body: str
    status: IncidentStatus | None | Unset = UNSET
    display_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        body = self.body

        status: None | str | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        elif isinstance(self.status, IncidentStatus):
            status = self.status.value
        else:
            status = self.status

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
                "body": body,
            }
        )
        if status is not UNSET:
            field_dict["status"] = status
        if display_at is not UNSET:
            field_dict["display_at"] = display_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        body = d.pop("body")

        def _parse_status(data: object) -> IncidentStatus | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                status_type_0 = IncidentStatus(data)

                return status_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(IncidentStatus | None | Unset, data)

        status = _parse_status(d.pop("status", UNSET))

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

        post_incident_update_schema = cls(
            body=body,
            status=status,
            display_at=display_at,
        )

        post_incident_update_schema.additional_properties = d
        return post_incident_update_schema

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
