from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define, field as _attrs_field

from ..models.heartbeat_type import HeartbeatType
from ..types import UNSET, Unset

T = TypeVar("T", bound="UpdateHeartbeatStateInput")


@_attrs_define
class UpdateHeartbeatStateInput:
    """
    Attributes:
        type (HeartbeatType):
        timeout_seconds (int):
        muted (bool):
        resolve_incident (bool):
        cron_expression (Union[None, Unset, str]):
        cron_timezone (Union[None, Unset, str]):
        interval_seconds (Union[None, Unset, int]):
    """

    type: HeartbeatType
    timeout_seconds: int
    muted: bool
    resolve_incident: bool
    cron_expression: Union[None, Unset, str] = UNSET
    cron_timezone: Union[None, Unset, str] = UNSET
    interval_seconds: Union[None, Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type.value

        timeout_seconds = self.timeout_seconds

        muted = self.muted

        resolve_incident = self.resolve_incident

        cron_expression: Union[None, Unset, str]
        if isinstance(self.cron_expression, Unset):
            cron_expression = UNSET
        else:
            cron_expression = self.cron_expression

        cron_timezone: Union[None, Unset, str]
        if isinstance(self.cron_timezone, Unset):
            cron_timezone = UNSET
        else:
            cron_timezone = self.cron_timezone

        interval_seconds: Union[None, Unset, int]
        if isinstance(self.interval_seconds, Unset):
            interval_seconds = UNSET
        else:
            interval_seconds = self.interval_seconds

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "timeout_seconds": timeout_seconds,
                "muted": muted,
                "resolve_incident": resolve_incident,
            }
        )
        if cron_expression is not UNSET:
            field_dict["cron_expression"] = cron_expression
        if cron_timezone is not UNSET:
            field_dict["cron_timezone"] = cron_timezone
        if interval_seconds is not UNSET:
            field_dict["interval_seconds"] = interval_seconds

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        type = HeartbeatType(d.pop("type"))

        timeout_seconds = d.pop("timeout_seconds")

        muted = d.pop("muted")

        resolve_incident = d.pop("resolve_incident")

        def _parse_cron_expression(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        cron_expression = _parse_cron_expression(d.pop("cron_expression", UNSET))

        def _parse_cron_timezone(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        cron_timezone = _parse_cron_timezone(d.pop("cron_timezone", UNSET))

        def _parse_interval_seconds(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        interval_seconds = _parse_interval_seconds(d.pop("interval_seconds", UNSET))

        update_heartbeat_state_input = cls(
            type=type,
            timeout_seconds=timeout_seconds,
            muted=muted,
            resolve_incident=resolve_incident,
            cron_expression=cron_expression,
            cron_timezone=cron_timezone,
            interval_seconds=interval_seconds,
        )

        update_heartbeat_state_input.additional_properties = d
        return update_heartbeat_state_input

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
