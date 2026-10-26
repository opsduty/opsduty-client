from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define, field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PageInfo")


@_attrs_define
class PageInfo:
    """
    Attributes:
        has_next_page (bool):
        has_previous_page (bool):
        start_cursor (None | str | Unset):
        end_cursor (None | str | Unset):
    """

    has_next_page: bool
    has_previous_page: bool
    start_cursor: None | str | Unset = UNSET
    end_cursor: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        has_next_page = self.has_next_page

        has_previous_page = self.has_previous_page

        start_cursor: None | str | Unset
        if isinstance(self.start_cursor, Unset):
            start_cursor = UNSET
        else:
            start_cursor = self.start_cursor

        end_cursor: None | str | Unset
        if isinstance(self.end_cursor, Unset):
            end_cursor = UNSET
        else:
            end_cursor = self.end_cursor

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "has_next_page": has_next_page,
                "has_previous_page": has_previous_page,
            }
        )
        if start_cursor is not UNSET:
            field_dict["start_cursor"] = start_cursor
        if end_cursor is not UNSET:
            field_dict["end_cursor"] = end_cursor

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        has_next_page = d.pop("has_next_page")

        has_previous_page = d.pop("has_previous_page")

        def _parse_start_cursor(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        start_cursor = _parse_start_cursor(d.pop("start_cursor", UNSET))

        def _parse_end_cursor(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        end_cursor = _parse_end_cursor(d.pop("end_cursor", UNSET))

        page_info = cls(
            has_next_page=has_next_page,
            has_previous_page=has_previous_page,
            start_cursor=start_cursor,
            end_cursor=end_cursor,
        )

        page_info.additional_properties = d
        return page_info

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
