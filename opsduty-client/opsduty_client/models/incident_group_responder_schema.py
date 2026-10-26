from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define, field as _attrs_field

from ..models.responder_status import ResponderStatus

if TYPE_CHECKING:
    from ..models.user_schema import UserSchema


T = TypeVar("T", bound="IncidentGroupResponderSchema")


@_attrs_define
class IncidentGroupResponderSchema:
    """
    Attributes:
        id (int):
        last_notified (datetime.datetime | None):
        status (ResponderStatus):
        status_updated_at (datetime.datetime | None):
        user (UserSchema):
    """

    id: int
    last_notified: datetime.datetime | None
    status: ResponderStatus
    status_updated_at: datetime.datetime | None
    user: UserSchema
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        last_notified: None | str
        if isinstance(self.last_notified, datetime.datetime):
            last_notified = self.last_notified.isoformat()
        else:
            last_notified = self.last_notified

        status = self.status.value

        status_updated_at: None | str
        if isinstance(self.status_updated_at, datetime.datetime):
            status_updated_at = self.status_updated_at.isoformat()
        else:
            status_updated_at = self.status_updated_at

        user = self.user.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "last_notified": last_notified,
                "status": status,
                "status_updated_at": status_updated_at,
                "user": user,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_schema import UserSchema  # noqa: PLC0415

        d = dict(src_dict)
        id = d.pop("id")

        def _parse_last_notified(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_notified_type_0 = datetime.datetime.fromisoformat(data)

                return last_notified_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        last_notified = _parse_last_notified(d.pop("last_notified"))

        status = ResponderStatus(d.pop("status"))

        def _parse_status_updated_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                status_updated_at_type_0 = datetime.datetime.fromisoformat(data)

                return status_updated_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        status_updated_at = _parse_status_updated_at(d.pop("status_updated_at"))

        user = UserSchema.from_dict(d.pop("user"))

        incident_group_responder_schema = cls(
            id=id,
            last_notified=last_notified,
            status=status,
            status_updated_at=status_updated_at,
            user=user,
        )

        incident_group_responder_schema.additional_properties = d
        return incident_group_responder_schema

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
