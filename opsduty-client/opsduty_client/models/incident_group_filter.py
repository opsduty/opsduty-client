import datetime
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define, field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="IncidentGroupFilter")


@_attrs_define
class IncidentGroupFilter:
    """
    Attributes:
        since (Union[None, Unset, datetime.datetime]):
        until (Union[None, Unset, datetime.datetime]):
        service (Union[None, Unset, int]):
    """

    since: Union[None, Unset, datetime.datetime] = UNSET
    until: Union[None, Unset, datetime.datetime] = UNSET
    service: Union[None, Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        since: Union[None, Unset, str]
        if isinstance(self.since, Unset):
            since = UNSET
        elif isinstance(self.since, datetime.datetime):
            since = self.since.isoformat()
        else:
            since = self.since

        until: Union[None, Unset, str]
        if isinstance(self.until, Unset):
            until = UNSET
        elif isinstance(self.until, datetime.datetime):
            until = self.until.isoformat()
        else:
            until = self.until

        service: Union[None, Unset, int]
        if isinstance(self.service, Unset):
            service = UNSET
        else:
            service = self.service

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if since is not UNSET:
            field_dict["since"] = since
        if until is not UNSET:
            field_dict["until"] = until
        if service is not UNSET:
            field_dict["service"] = service

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()

        def _parse_since(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                since_type_0 = isoparse(data)

                return since_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        since = _parse_since(d.pop("since", UNSET))

        def _parse_until(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                until_type_0 = isoparse(data)

                return until_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        until = _parse_until(d.pop("until", UNSET))

        def _parse_service(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        service = _parse_service(d.pop("service", UNSET))

        incident_group_filter = cls(
            since=since,
            until=until,
            service=service,
        )

        incident_group_filter.additional_properties = d
        return incident_group_filter

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
