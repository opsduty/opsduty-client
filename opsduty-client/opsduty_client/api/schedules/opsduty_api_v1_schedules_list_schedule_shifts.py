import datetime
from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.opsduty_api_v1_schedules_list_schedule_shifts_response_401 import OpsdutyApiV1SchedulesListScheduleShiftsResponse401
from ...models.opsduty_api_v1_schedules_list_schedule_shifts_response_404 import OpsdutyApiV1SchedulesListScheduleShiftsResponse404
from ...models.opsduty_api_v1_schedules_list_schedule_shifts_response_422 import OpsdutyApiV1SchedulesListScheduleShiftsResponse422
from ...models.schedule_shift_schema import ScheduleShiftSchema
from ...types import UNSET, Response, Unset


def _get_kwargs(
    schedule_id: int,
    *,
    datetime_start: datetime.datetime,
    datetime_end: datetime.datetime,
    overflow: bool | Unset = True,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_datetime_start = datetime_start.isoformat()
    params["datetime_start"] = json_datetime_start

    json_datetime_end = datetime_end.isoformat()
    params["datetime_end"] = json_datetime_end

    params["overflow"] = overflow

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/schedules/{schedule_id}/shifts/".format(
            schedule_id=quote(str(schedule_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> OpsdutyApiV1SchedulesListScheduleShiftsResponse401 | OpsdutyApiV1SchedulesListScheduleShiftsResponse404 | OpsdutyApiV1SchedulesListScheduleShiftsResponse422 | list[ScheduleShiftSchema] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ScheduleShiftSchema.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if response.status_code == 401:
        response_401 = OpsdutyApiV1SchedulesListScheduleShiftsResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = OpsdutyApiV1SchedulesListScheduleShiftsResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = OpsdutyApiV1SchedulesListScheduleShiftsResponse422.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[OpsdutyApiV1SchedulesListScheduleShiftsResponse401 | OpsdutyApiV1SchedulesListScheduleShiftsResponse404 | OpsdutyApiV1SchedulesListScheduleShiftsResponse422 | list[ScheduleShiftSchema]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    schedule_id: int,
    *,
    client: AuthenticatedClient,
    datetime_start: datetime.datetime,
    datetime_end: datetime.datetime,
    overflow: bool | Unset = True,
) -> Response[OpsdutyApiV1SchedulesListScheduleShiftsResponse401 | OpsdutyApiV1SchedulesListScheduleShiftsResponse404 | OpsdutyApiV1SchedulesListScheduleShiftsResponse422 | list[ScheduleShiftSchema]]:
    """List schedule shifts

     Work out who is on call between two times, layers and overrides applied.

    `datetime_start` and `datetime_end` are required and must be at most 120
    days apart. Shifts are computed rather than stored, so this is not paged
    and returns the whole range at once.

    A shift that starts before the range or ends after it is returned with its
    real handover times. Pass `overflow=false` to cut those shifts back to the
    range you asked for instead.

    Args:
        schedule_id (int):
        datetime_start (datetime.datetime):
        datetime_end (datetime.datetime):
        overflow (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OpsdutyApiV1SchedulesListScheduleShiftsResponse401 | OpsdutyApiV1SchedulesListScheduleShiftsResponse404 | OpsdutyApiV1SchedulesListScheduleShiftsResponse422 | list[ScheduleShiftSchema]]
    """

    kwargs = _get_kwargs(
        schedule_id=schedule_id,
        datetime_start=datetime_start,
        datetime_end=datetime_end,
        overflow=overflow,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    schedule_id: int,
    *,
    client: AuthenticatedClient,
    datetime_start: datetime.datetime,
    datetime_end: datetime.datetime,
    overflow: bool | Unset = True,
) -> OpsdutyApiV1SchedulesListScheduleShiftsResponse401 | OpsdutyApiV1SchedulesListScheduleShiftsResponse404 | OpsdutyApiV1SchedulesListScheduleShiftsResponse422 | list[ScheduleShiftSchema] | None:
    """List schedule shifts

     Work out who is on call between two times, layers and overrides applied.

    `datetime_start` and `datetime_end` are required and must be at most 120
    days apart. Shifts are computed rather than stored, so this is not paged
    and returns the whole range at once.

    A shift that starts before the range or ends after it is returned with its
    real handover times. Pass `overflow=false` to cut those shifts back to the
    range you asked for instead.

    Args:
        schedule_id (int):
        datetime_start (datetime.datetime):
        datetime_end (datetime.datetime):
        overflow (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OpsdutyApiV1SchedulesListScheduleShiftsResponse401 | OpsdutyApiV1SchedulesListScheduleShiftsResponse404 | OpsdutyApiV1SchedulesListScheduleShiftsResponse422 | list[ScheduleShiftSchema]
    """

    return sync_detailed(
        schedule_id=schedule_id,
        client=client,
        datetime_start=datetime_start,
        datetime_end=datetime_end,
        overflow=overflow,
    ).parsed


async def asyncio_detailed(
    schedule_id: int,
    *,
    client: AuthenticatedClient,
    datetime_start: datetime.datetime,
    datetime_end: datetime.datetime,
    overflow: bool | Unset = True,
) -> Response[OpsdutyApiV1SchedulesListScheduleShiftsResponse401 | OpsdutyApiV1SchedulesListScheduleShiftsResponse404 | OpsdutyApiV1SchedulesListScheduleShiftsResponse422 | list[ScheduleShiftSchema]]:
    """List schedule shifts

     Work out who is on call between two times, layers and overrides applied.

    `datetime_start` and `datetime_end` are required and must be at most 120
    days apart. Shifts are computed rather than stored, so this is not paged
    and returns the whole range at once.

    A shift that starts before the range or ends after it is returned with its
    real handover times. Pass `overflow=false` to cut those shifts back to the
    range you asked for instead.

    Args:
        schedule_id (int):
        datetime_start (datetime.datetime):
        datetime_end (datetime.datetime):
        overflow (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OpsdutyApiV1SchedulesListScheduleShiftsResponse401 | OpsdutyApiV1SchedulesListScheduleShiftsResponse404 | OpsdutyApiV1SchedulesListScheduleShiftsResponse422 | list[ScheduleShiftSchema]]
    """

    kwargs = _get_kwargs(
        schedule_id=schedule_id,
        datetime_start=datetime_start,
        datetime_end=datetime_end,
        overflow=overflow,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    schedule_id: int,
    *,
    client: AuthenticatedClient,
    datetime_start: datetime.datetime,
    datetime_end: datetime.datetime,
    overflow: bool | Unset = True,
) -> OpsdutyApiV1SchedulesListScheduleShiftsResponse401 | OpsdutyApiV1SchedulesListScheduleShiftsResponse404 | OpsdutyApiV1SchedulesListScheduleShiftsResponse422 | list[ScheduleShiftSchema] | None:
    """List schedule shifts

     Work out who is on call between two times, layers and overrides applied.

    `datetime_start` and `datetime_end` are required and must be at most 120
    days apart. Shifts are computed rather than stored, so this is not paged
    and returns the whole range at once.

    A shift that starts before the range or ends after it is returned with its
    real handover times. Pass `overflow=false` to cut those shifts back to the
    range you asked for instead.

    Args:
        schedule_id (int):
        datetime_start (datetime.datetime):
        datetime_end (datetime.datetime):
        overflow (bool | Unset):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OpsdutyApiV1SchedulesListScheduleShiftsResponse401 | OpsdutyApiV1SchedulesListScheduleShiftsResponse404 | OpsdutyApiV1SchedulesListScheduleShiftsResponse422 | list[ScheduleShiftSchema]
    """

    return (
        await asyncio_detailed(
            schedule_id=schedule_id,
            client=client,
            datetime_start=datetime_start,
            datetime_end=datetime_end,
            overflow=overflow,
        )
    ).parsed
