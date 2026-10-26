from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define, field as _attrs_field

T = TypeVar("T", bound="OpsdutyApiV1StatuspagesListStatusPageComponentGroupsResponse422")


@_attrs_define
class OpsdutyApiV1StatuspagesListStatusPageComponentGroupsResponse422:
    """
    Attributes:
        detail (list[Any]):
    """

    detail: list[Any]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        detail = self.detail

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "detail": detail,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        detail = cast(list[Any], d.pop("detail"))

        opsduty_api_v1_statuspages_list_status_page_component_groups_response_422 = cls(
            detail=detail,
        )

        opsduty_api_v1_statuspages_list_status_page_component_groups_response_422.additional_properties = d
        return opsduty_api_v1_statuspages_list_status_page_component_groups_response_422

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
