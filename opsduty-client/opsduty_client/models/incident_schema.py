from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define, field as _attrs_field

from ..models.incident_impact import IncidentImpact
from ..models.incident_status import IncidentStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="IncidentSchema")


@_attrs_define
class IncidentSchema:
    """
    Attributes:
        status (IncidentStatus):
        impact (IncidentImpact): The impact of an incident on the users of the affected services.

            The impact can be used to automatically update the status of the affected
            components.
        component_ids (list[int]):
        sync_component_status (bool): Whether the affected components follow this incident's impact while it is open.
        duration_seconds (int | None): How long the incident lasted. Null until it is resolved.
        draft (bool): Whether this is a draft only your team can see. Publish it to put it on the status page.
        status_page (int):
        title (str):
        created_at (datetime.datetime):
        id (int | None | Unset):
        incident_group (int | None | Unset):
        body (None | str | Unset):
        monitoring_at (datetime.datetime | None | Unset):
        resolved_at (datetime.datetime | None | Unset):
        scheduled_start (datetime.datetime | None | Unset):
        scheduled_end (datetime.datetime | None | Unset):
    """

    status: IncidentStatus
    impact: IncidentImpact
    component_ids: list[int]
    sync_component_status: bool
    duration_seconds: int | None
    draft: bool
    status_page: int
    title: str
    created_at: datetime.datetime
    id: int | None | Unset = UNSET
    incident_group: int | None | Unset = UNSET
    body: None | str | Unset = UNSET
    monitoring_at: datetime.datetime | None | Unset = UNSET
    resolved_at: datetime.datetime | None | Unset = UNSET
    scheduled_start: datetime.datetime | None | Unset = UNSET
    scheduled_end: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status.value

        impact = self.impact.value

        component_ids = self.component_ids

        sync_component_status = self.sync_component_status

        duration_seconds: int | None
        duration_seconds = self.duration_seconds

        draft = self.draft

        status_page = self.status_page

        title = self.title

        created_at = self.created_at.isoformat()

        id: int | None | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        incident_group: int | None | Unset
        if isinstance(self.incident_group, Unset):
            incident_group = UNSET
        else:
            incident_group = self.incident_group

        body: None | str | Unset
        if isinstance(self.body, Unset):
            body = UNSET
        else:
            body = self.body

        monitoring_at: None | str | Unset
        if isinstance(self.monitoring_at, Unset):
            monitoring_at = UNSET
        elif isinstance(self.monitoring_at, datetime.datetime):
            monitoring_at = self.monitoring_at.isoformat()
        else:
            monitoring_at = self.monitoring_at

        resolved_at: None | str | Unset
        if isinstance(self.resolved_at, Unset):
            resolved_at = UNSET
        elif isinstance(self.resolved_at, datetime.datetime):
            resolved_at = self.resolved_at.isoformat()
        else:
            resolved_at = self.resolved_at

        scheduled_start: None | str | Unset
        if isinstance(self.scheduled_start, Unset):
            scheduled_start = UNSET
        elif isinstance(self.scheduled_start, datetime.datetime):
            scheduled_start = self.scheduled_start.isoformat()
        else:
            scheduled_start = self.scheduled_start

        scheduled_end: None | str | Unset
        if isinstance(self.scheduled_end, Unset):
            scheduled_end = UNSET
        elif isinstance(self.scheduled_end, datetime.datetime):
            scheduled_end = self.scheduled_end.isoformat()
        else:
            scheduled_end = self.scheduled_end

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
                "impact": impact,
                "component_ids": component_ids,
                "sync_component_status": sync_component_status,
                "duration_seconds": duration_seconds,
                "draft": draft,
                "status_page": status_page,
                "title": title,
                "created_at": created_at,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if incident_group is not UNSET:
            field_dict["incident_group"] = incident_group
        if body is not UNSET:
            field_dict["body"] = body
        if monitoring_at is not UNSET:
            field_dict["monitoring_at"] = monitoring_at
        if resolved_at is not UNSET:
            field_dict["resolved_at"] = resolved_at
        if scheduled_start is not UNSET:
            field_dict["scheduled_start"] = scheduled_start
        if scheduled_end is not UNSET:
            field_dict["scheduled_end"] = scheduled_end

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        status = IncidentStatus(d.pop("status"))

        impact = IncidentImpact(d.pop("impact"))

        component_ids = cast(list[int], d.pop("component_ids"))

        sync_component_status = d.pop("sync_component_status")

        def _parse_duration_seconds(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        duration_seconds = _parse_duration_seconds(d.pop("duration_seconds"))

        draft = d.pop("draft")

        status_page = d.pop("status_page")

        title = d.pop("title")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        def _parse_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        id = _parse_id(d.pop("id", UNSET))

        def _parse_incident_group(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        incident_group = _parse_incident_group(d.pop("incident_group", UNSET))

        def _parse_body(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        body = _parse_body(d.pop("body", UNSET))

        def _parse_monitoring_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                monitoring_at_type_0 = datetime.datetime.fromisoformat(data)

                return monitoring_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        monitoring_at = _parse_monitoring_at(d.pop("monitoring_at", UNSET))

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

        def _parse_scheduled_start(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                scheduled_start_type_0 = datetime.datetime.fromisoformat(data)

                return scheduled_start_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        scheduled_start = _parse_scheduled_start(d.pop("scheduled_start", UNSET))

        def _parse_scheduled_end(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                scheduled_end_type_0 = datetime.datetime.fromisoformat(data)

                return scheduled_end_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        scheduled_end = _parse_scheduled_end(d.pop("scheduled_end", UNSET))

        incident_schema = cls(
            status=status,
            impact=impact,
            component_ids=component_ids,
            sync_component_status=sync_component_status,
            duration_seconds=duration_seconds,
            draft=draft,
            status_page=status_page,
            title=title,
            created_at=created_at,
            id=id,
            incident_group=incident_group,
            body=body,
            monitoring_at=monitoring_at,
            resolved_at=resolved_at,
            scheduled_start=scheduled_start,
            scheduled_end=scheduled_end,
        )

        incident_schema.additional_properties = d
        return incident_schema

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
