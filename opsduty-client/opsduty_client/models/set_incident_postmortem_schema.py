from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define, field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SetIncidentPostmortemSchema")


@_attrs_define
class SetIncidentPostmortemSchema:
    """
    Attributes:
        body (str): The retrospective customers read. Markdown is supported.
        published (bool | Unset): Publish it to the public page and the feed. Defaults to false, so writing a postmortem
            does not show it to customers until you say so. Setting this back to false takes a published one down again.
            Default: False.
    """

    body: str
    published: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        body = self.body

        published = self.published

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "body": body,
            }
        )
        if published is not UNSET:
            field_dict["published"] = published

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        body = d.pop("body")

        published = d.pop("published", UNSET)

        set_incident_postmortem_schema = cls(
            body=body,
            published=published,
        )

        set_incident_postmortem_schema.additional_properties = d
        return set_incident_postmortem_schema

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
