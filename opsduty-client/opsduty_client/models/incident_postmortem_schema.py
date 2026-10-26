from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define, field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="IncidentPostmortemSchema")


@_attrs_define
class IncidentPostmortemSchema:
    """
    Attributes:
        published (bool): Whether customers can read this. An unpublished postmortem stays a draft and never reaches the
            public page or the feed.
        body (str):
        created_at (datetime.datetime):
        id (int | None | Unset):
        published_at (datetime.datetime | None | Unset):
    """

    published: bool
    body: str
    created_at: datetime.datetime
    id: int | None | Unset = UNSET
    published_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        published = self.published

        body = self.body

        created_at = self.created_at.isoformat()

        id: int | None | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        published_at: None | str | Unset
        if isinstance(self.published_at, Unset):
            published_at = UNSET
        elif isinstance(self.published_at, datetime.datetime):
            published_at = self.published_at.isoformat()
        else:
            published_at = self.published_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "published": published,
                "body": body,
                "created_at": created_at,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if published_at is not UNSET:
            field_dict["published_at"] = published_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        published = d.pop("published")

        body = d.pop("body")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        def _parse_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        id = _parse_id(d.pop("id", UNSET))

        def _parse_published_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                published_at_type_0 = datetime.datetime.fromisoformat(data)

                return published_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        published_at = _parse_published_at(d.pop("published_at", UNSET))

        incident_postmortem_schema = cls(
            published=published,
            body=body,
            created_at=created_at,
            id=id,
            published_at=published_at,
        )

        incident_postmortem_schema.additional_properties = d
        return incident_postmortem_schema

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
