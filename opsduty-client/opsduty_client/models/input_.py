from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define, field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Input")


@_attrs_define
class Input:
    """
    Attributes:
        first (int | None | Unset): How many items to return from the start of the list, or after `after`.
        last (int | None | Unset): How many items to return from the end of the list, or before `before`. They are still
            in list order.
        before (None | str | Unset): A `start_cursor` to page back from.
        after (None | str | Unset): An `end_cursor` to page on from.
    """

    first: int | None | Unset = UNSET
    last: int | None | Unset = UNSET
    before: None | str | Unset = UNSET
    after: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        first: int | None | Unset
        if isinstance(self.first, Unset):
            first = UNSET
        else:
            first = self.first

        last: int | None | Unset
        if isinstance(self.last, Unset):
            last = UNSET
        else:
            last = self.last

        before: None | str | Unset
        if isinstance(self.before, Unset):
            before = UNSET
        else:
            before = self.before

        after: None | str | Unset
        if isinstance(self.after, Unset):
            after = UNSET
        else:
            after = self.after

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if first is not UNSET:
            field_dict["first"] = first
        if last is not UNSET:
            field_dict["last"] = last
        if before is not UNSET:
            field_dict["before"] = before
        if after is not UNSET:
            field_dict["after"] = after

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_first(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        first = _parse_first(d.pop("first", UNSET))

        def _parse_last(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        last = _parse_last(d.pop("last", UNSET))

        def _parse_before(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        before = _parse_before(d.pop("before", UNSET))

        def _parse_after(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        after = _parse_after(d.pop("after", UNSET))

        input_ = cls(
            first=first,
            last=last,
            before=before,
            after=after,
        )

        input_.additional_properties = d
        return input_

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
