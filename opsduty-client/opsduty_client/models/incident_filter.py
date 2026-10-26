from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define, field as _attrs_field

from ..models.incident_filter_type_type_0 import IncidentFilterTypeType0
from ..models.incident_status import IncidentStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="IncidentFilter")


@_attrs_define
class IncidentFilter:
    """
    Attributes:
        status (list[IncidentStatus] | None | Unset): Only incidents in one of these statuses.
        type_ (IncidentFilterTypeType0 | None | Unset): Only planned work (scheduled, in progress or completed), or only
            unplanned incidents.
        created_after (datetime.datetime | None | Unset): Only incidents declared at or after this time.
        created_before (datetime.datetime | None | Unset): Only incidents declared before this time.
        component_id (int | None | Unset): Only incidents affecting this component.
    """

    status: list[IncidentStatus] | None | Unset = UNSET
    type_: IncidentFilterTypeType0 | None | Unset = UNSET
    created_after: datetime.datetime | None | Unset = UNSET
    created_before: datetime.datetime | None | Unset = UNSET
    component_id: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status: list[str] | None | Unset
        if isinstance(self.status, Unset):
            status = UNSET
        elif isinstance(self.status, list):
            status = []
            for status_type_0_item_data in self.status:
                status_type_0_item = status_type_0_item_data.value
                status.append(status_type_0_item)

        else:
            status = self.status

        type_: None | str | Unset
        if isinstance(self.type_, Unset):
            type_ = UNSET
        elif isinstance(self.type_, IncidentFilterTypeType0):
            type_ = self.type_.value
        else:
            type_ = self.type_

        created_after: None | str | Unset
        if isinstance(self.created_after, Unset):
            created_after = UNSET
        elif isinstance(self.created_after, datetime.datetime):
            created_after = self.created_after.isoformat()
        else:
            created_after = self.created_after

        created_before: None | str | Unset
        if isinstance(self.created_before, Unset):
            created_before = UNSET
        elif isinstance(self.created_before, datetime.datetime):
            created_before = self.created_before.isoformat()
        else:
            created_before = self.created_before

        component_id: int | None | Unset
        if isinstance(self.component_id, Unset):
            component_id = UNSET
        else:
            component_id = self.component_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if type_ is not UNSET:
            field_dict["type"] = type_
        if created_after is not UNSET:
            field_dict["created_after"] = created_after
        if created_before is not UNSET:
            field_dict["created_before"] = created_before
        if component_id is not UNSET:
            field_dict["component_id"] = component_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_status(data: object) -> list[IncidentStatus] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                status_type_0 = []
                _status_type_0 = data
                for status_type_0_item_data in _status_type_0:
                    status_type_0_item = IncidentStatus(status_type_0_item_data)

                    status_type_0.append(status_type_0_item)

                return status_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[IncidentStatus] | None | Unset, data)

        status = _parse_status(d.pop("status", UNSET))

        def _parse_type_(data: object) -> IncidentFilterTypeType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                type_type_0 = IncidentFilterTypeType0(data)

                return type_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(IncidentFilterTypeType0 | None | Unset, data)

        type_ = _parse_type_(d.pop("type", UNSET))

        def _parse_created_after(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_after_type_0 = datetime.datetime.fromisoformat(data)

                return created_after_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        created_after = _parse_created_after(d.pop("created_after", UNSET))

        def _parse_created_before(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_before_type_0 = datetime.datetime.fromisoformat(data)

                return created_before_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        created_before = _parse_created_before(d.pop("created_before", UNSET))

        def _parse_component_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        component_id = _parse_component_id(d.pop("component_id", UNSET))

        incident_filter = cls(
            status=status,
            type_=type_,
            created_after=created_after,
            created_before=created_before,
            component_id=component_id,
        )

        incident_filter.additional_properties = d
        return incident_filter

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
