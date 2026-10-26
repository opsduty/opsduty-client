from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define, field as _attrs_field

from ..models.incident_impact import IncidentImpact
from ..models.incident_status import IncidentStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="DeclareIncidentSchema")


@_attrs_define
class DeclareIncidentSchema:
    """
    Attributes:
        title (str): The headline customers see, e.g. 'Elevated error rates'.
        status (IncidentStatus | Unset):  Default: IncidentStatus.INVESTIGATING.
        impact (IncidentImpact | Unset): The impact of an incident on the users of the affected services.

            The impact can be used to automatically update the status of the affected
            components. Default: IncidentImpact.MINOR.
        body (str | Unset): The opening message customers read. Markdown is supported. Default: ''.
        component_ids (list[int] | Unset): Components on this status page the incident affects.
        incident_group_id (int | None | Unset): The operational incident this one tells customers about. Pass the id
            from /api/v1/incidents/ so the two are linked.
        derive_affected_components (bool | Unset): Work out the affected components from the linked incident's service
            instead of listing them yourself. Needs incident_group_id, and is ignored when you pass component_ids. Default:
            False.
        sync_component_status (bool | Unset): Keep the affected components in step with this incident's impact. While it
            is open they read the status the impact implies, and resolving it puts them back to operational. Default: False.
        published (bool | Unset): Publish it to the status page straight away. Set to false to save a draft only your
            team can see, and publish it when it is ready. Default: True.
    """

    title: str
    status: IncidentStatus | Unset = IncidentStatus.INVESTIGATING
    impact: IncidentImpact | Unset = IncidentImpact.MINOR
    body: str | Unset = ""
    component_ids: list[int] | Unset = UNSET
    incident_group_id: int | None | Unset = UNSET
    derive_affected_components: bool | Unset = False
    sync_component_status: bool | Unset = False
    published: bool | Unset = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        impact: str | Unset = UNSET
        if not isinstance(self.impact, Unset):
            impact = self.impact.value

        body = self.body

        component_ids: list[int] | Unset = UNSET
        if not isinstance(self.component_ids, Unset):
            component_ids = self.component_ids

        incident_group_id: int | None | Unset
        if isinstance(self.incident_group_id, Unset):
            incident_group_id = UNSET
        else:
            incident_group_id = self.incident_group_id

        derive_affected_components = self.derive_affected_components

        sync_component_status = self.sync_component_status

        published = self.published

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "title": title,
            }
        )
        if status is not UNSET:
            field_dict["status"] = status
        if impact is not UNSET:
            field_dict["impact"] = impact
        if body is not UNSET:
            field_dict["body"] = body
        if component_ids is not UNSET:
            field_dict["component_ids"] = component_ids
        if incident_group_id is not UNSET:
            field_dict["incident_group_id"] = incident_group_id
        if derive_affected_components is not UNSET:
            field_dict["derive_affected_components"] = derive_affected_components
        if sync_component_status is not UNSET:
            field_dict["sync_component_status"] = sync_component_status
        if published is not UNSET:
            field_dict["published"] = published

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        title = d.pop("title")

        _status = d.pop("status", UNSET)
        status: IncidentStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = IncidentStatus(_status)

        _impact = d.pop("impact", UNSET)
        impact: IncidentImpact | Unset
        if isinstance(_impact, Unset):
            impact = UNSET
        else:
            impact = IncidentImpact(_impact)

        body = d.pop("body", UNSET)

        component_ids = cast(list[int], d.pop("component_ids", UNSET))

        def _parse_incident_group_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        incident_group_id = _parse_incident_group_id(d.pop("incident_group_id", UNSET))

        derive_affected_components = d.pop("derive_affected_components", UNSET)

        sync_component_status = d.pop("sync_component_status", UNSET)

        published = d.pop("published", UNSET)

        declare_incident_schema = cls(
            title=title,
            status=status,
            impact=impact,
            body=body,
            component_ids=component_ids,
            incident_group_id=incident_group_id,
            derive_affected_components=derive_affected_components,
            sync_component_status=sync_component_status,
            published=published,
        )

        declare_incident_schema.additional_properties = d
        return declare_incident_schema

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
