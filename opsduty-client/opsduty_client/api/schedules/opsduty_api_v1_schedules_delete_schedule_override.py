from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.opsduty_api_v1_schedules_delete_schedule_override_response_401 import OpsdutyApiV1SchedulesDeleteScheduleOverrideResponse401
from ...models.opsduty_api_v1_schedules_delete_schedule_override_response_404 import OpsdutyApiV1SchedulesDeleteScheduleOverrideResponse404
from ...models.opsduty_api_v1_schedules_delete_schedule_override_response_422 import OpsdutyApiV1SchedulesDeleteScheduleOverrideResponse422
from ...types import Response


def _get_kwargs(
    schedule_id: int,
    override_id: int,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/v1/schedules/{schedule_id}/overrides/{override_id}/".format(
            schedule_id=quote(str(schedule_id), safe=""),
            override_id=quote(str(override_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | OpsdutyApiV1SchedulesDeleteScheduleOverrideResponse401 | OpsdutyApiV1SchedulesDeleteScheduleOverrideResponse404 | OpsdutyApiV1SchedulesDeleteScheduleOverrideResponse422 | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 401:
        response_401 = OpsdutyApiV1SchedulesDeleteScheduleOverrideResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = OpsdutyApiV1SchedulesDeleteScheduleOverrideResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = OpsdutyApiV1SchedulesDeleteScheduleOverrideResponse422.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | OpsdutyApiV1SchedulesDeleteScheduleOverrideResponse401 | OpsdutyApiV1SchedulesDeleteScheduleOverrideResponse404 | OpsdutyApiV1SchedulesDeleteScheduleOverrideResponse422]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    schedule_id: int,
    override_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Any | OpsdutyApiV1SchedulesDeleteScheduleOverrideResponse401 | OpsdutyApiV1SchedulesDeleteScheduleOverrideResponse404 | OpsdutyApiV1SchedulesDeleteScheduleOverrideResponse422]:
    """Delete a schedule override

     Remove an override, handing the time back to the normal rotation.

    Whoever the layers put on call for that stretch is on call again, so check
    that somebody is before removing cover that is already running.

    Args:
        schedule_id (int):
        override_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | OpsdutyApiV1SchedulesDeleteScheduleOverrideResponse401 | OpsdutyApiV1SchedulesDeleteScheduleOverrideResponse404 | OpsdutyApiV1SchedulesDeleteScheduleOverrideResponse422]
    """

    kwargs = _get_kwargs(
        schedule_id=schedule_id,
        override_id=override_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    schedule_id: int,
    override_id: int,
    *,
    client: AuthenticatedClient,
) -> Any | OpsdutyApiV1SchedulesDeleteScheduleOverrideResponse401 | OpsdutyApiV1SchedulesDeleteScheduleOverrideResponse404 | OpsdutyApiV1SchedulesDeleteScheduleOverrideResponse422 | None:
    """Delete a schedule override

     Remove an override, handing the time back to the normal rotation.

    Whoever the layers put on call for that stretch is on call again, so check
    that somebody is before removing cover that is already running.

    Args:
        schedule_id (int):
        override_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | OpsdutyApiV1SchedulesDeleteScheduleOverrideResponse401 | OpsdutyApiV1SchedulesDeleteScheduleOverrideResponse404 | OpsdutyApiV1SchedulesDeleteScheduleOverrideResponse422
    """

    return sync_detailed(
        schedule_id=schedule_id,
        override_id=override_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    schedule_id: int,
    override_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Any | OpsdutyApiV1SchedulesDeleteScheduleOverrideResponse401 | OpsdutyApiV1SchedulesDeleteScheduleOverrideResponse404 | OpsdutyApiV1SchedulesDeleteScheduleOverrideResponse422]:
    """Delete a schedule override

     Remove an override, handing the time back to the normal rotation.

    Whoever the layers put on call for that stretch is on call again, so check
    that somebody is before removing cover that is already running.

    Args:
        schedule_id (int):
        override_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | OpsdutyApiV1SchedulesDeleteScheduleOverrideResponse401 | OpsdutyApiV1SchedulesDeleteScheduleOverrideResponse404 | OpsdutyApiV1SchedulesDeleteScheduleOverrideResponse422]
    """

    kwargs = _get_kwargs(
        schedule_id=schedule_id,
        override_id=override_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    schedule_id: int,
    override_id: int,
    *,
    client: AuthenticatedClient,
) -> Any | OpsdutyApiV1SchedulesDeleteScheduleOverrideResponse401 | OpsdutyApiV1SchedulesDeleteScheduleOverrideResponse404 | OpsdutyApiV1SchedulesDeleteScheduleOverrideResponse422 | None:
    """Delete a schedule override

     Remove an override, handing the time back to the normal rotation.

    Whoever the layers put on call for that stretch is on call again, so check
    that somebody is before removing cover that is already running.

    Args:
        schedule_id (int):
        override_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | OpsdutyApiV1SchedulesDeleteScheduleOverrideResponse401 | OpsdutyApiV1SchedulesDeleteScheduleOverrideResponse404 | OpsdutyApiV1SchedulesDeleteScheduleOverrideResponse422
    """

    return (
        await asyncio_detailed(
            schedule_id=schedule_id,
            override_id=override_id,
            client=client,
        )
    ).parsed
