from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define, field as _attrs_field

if TYPE_CHECKING:
    from ..models.component_uptime_schema import ComponentUptimeSchema


T = TypeVar("T", bound="StatusPageUptimeSchema")


@_attrs_define
class StatusPageUptimeSchema:
    """
    Attributes:
        published (bool): Whether the page shows these figures to customers. They are worked out either way, so you can
            read them before turning it on.
        components (list[ComponentUptimeSchema]):
    """

    published: bool
    components: list[ComponentUptimeSchema]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        published = self.published

        components = []
        for components_item_data in self.components:
            components_item = components_item_data.to_dict()
            components.append(components_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "published": published,
                "components": components,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.component_uptime_schema import ComponentUptimeSchema  # noqa: PLC0415

        d = dict(src_dict)
        published = d.pop("published")

        components = []
        _components = d.pop("components")
        for components_item_data in _components:
            components_item = ComponentUptimeSchema.from_dict(components_item_data)

            components.append(components_item)

        status_page_uptime_schema = cls(
            published=published,
            components=components,
        )

        status_page_uptime_schema.additional_properties = d
        return status_page_uptime_schema

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
