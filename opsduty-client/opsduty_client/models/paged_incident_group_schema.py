from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define, field as _attrs_field

if TYPE_CHECKING:
    from ..models.incident_group_schema import IncidentGroupSchema
    from ..models.page_info import PageInfo


T = TypeVar("T", bound="PagedIncidentGroupSchema")


@_attrs_define
class PagedIncidentGroupSchema:
    """
    Attributes:
        items (List['IncidentGroupSchema']):
        page_info (PageInfo):
    """

    items: List["IncidentGroupSchema"]
    page_info: "PageInfo"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        items = []
        for items_item_data in self.items:
            items_item = items_item_data.to_dict()
            items.append(items_item)

        page_info = self.page_info.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "items": items,
                "page_info": page_info,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.incident_group_schema import IncidentGroupSchema
        from ..models.page_info import PageInfo

        d = src_dict.copy()
        items = []
        _items = d.pop("items")
        for items_item_data in _items:
            items_item = IncidentGroupSchema.from_dict(items_item_data)

            items.append(items_item)

        page_info = PageInfo.from_dict(d.pop("page_info"))

        paged_incident_group_schema = cls(
            items=items,
            page_info=page_info,
        )

        paged_incident_group_schema.additional_properties = d
        return paged_incident_group_schema

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
