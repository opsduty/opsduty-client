from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define, field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cron_heartbeat_state_schema import CronHeartbeatStateSchema
    from ..models.interval_heartbeat_state_schema import IntervalHeartbeatStateSchema


T = TypeVar("T", bound="HeartbeatSchema")


@_attrs_define
class HeartbeatSchema:
    """
    Attributes:
        states (list[CronHeartbeatStateSchema | IntervalHeartbeatStateSchema]):
        name (str):
        service (int):
        id (int | None | Unset):
        public_primary_key (str | Unset):
        description (None | str | Unset):  Default: ''.
        link (None | str | Unset):
        incident_urgency (None | str | Unset):
    """

    states: list[CronHeartbeatStateSchema | IntervalHeartbeatStateSchema]
    name: str
    service: int
    id: int | None | Unset = UNSET
    public_primary_key: str | Unset = UNSET
    description: None | str | Unset = ""
    link: None | str | Unset = UNSET
    incident_urgency: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.cron_heartbeat_state_schema import CronHeartbeatStateSchema  # noqa: PLC0415

        states = []
        for states_item_data in self.states:
            states_item: dict[str, Any]
            if isinstance(states_item_data, CronHeartbeatStateSchema):
                states_item = states_item_data.to_dict()
            else:
                states_item = states_item_data.to_dict()

            states.append(states_item)

        name = self.name

        service = self.service

        id: int | None | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        public_primary_key = self.public_primary_key

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        link: None | str | Unset
        if isinstance(self.link, Unset):
            link = UNSET
        else:
            link = self.link

        incident_urgency: None | str | Unset
        if isinstance(self.incident_urgency, Unset):
            incident_urgency = UNSET
        else:
            incident_urgency = self.incident_urgency

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "states": states,
                "name": name,
                "service": service,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if public_primary_key is not UNSET:
            field_dict["public_primary_key"] = public_primary_key
        if description is not UNSET:
            field_dict["description"] = description
        if link is not UNSET:
            field_dict["link"] = link
        if incident_urgency is not UNSET:
            field_dict["incident_urgency"] = incident_urgency

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cron_heartbeat_state_schema import CronHeartbeatStateSchema  # noqa: PLC0415
        from ..models.interval_heartbeat_state_schema import IntervalHeartbeatStateSchema  # noqa: PLC0415

        d = dict(src_dict)
        states = []
        _states = d.pop("states")
        for states_item_data in _states:

            def _parse_states_item(data: object) -> CronHeartbeatStateSchema | IntervalHeartbeatStateSchema:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    states_item_type_0 = CronHeartbeatStateSchema.from_dict(data)

                    return states_item_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                states_item_type_1 = IntervalHeartbeatStateSchema.from_dict(data)

                return states_item_type_1

            states_item = _parse_states_item(states_item_data)

            states.append(states_item)

        name = d.pop("name")

        service = d.pop("service")

        def _parse_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        id = _parse_id(d.pop("id", UNSET))

        public_primary_key = d.pop("public_primary_key", UNSET)

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_link(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        link = _parse_link(d.pop("link", UNSET))

        def _parse_incident_urgency(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        incident_urgency = _parse_incident_urgency(d.pop("incident_urgency", UNSET))

        heartbeat_schema = cls(
            states=states,
            name=name,
            service=service,
            id=id,
            public_primary_key=public_primary_key,
            description=description,
            link=link,
            incident_urgency=incident_urgency,
        )

        heartbeat_schema.additional_properties = d
        return heartbeat_schema

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
