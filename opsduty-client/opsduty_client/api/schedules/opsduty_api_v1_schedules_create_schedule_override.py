from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.opsduty_api_v1_schedules_create_schedule_override_response_401 import OpsdutyApiV1SchedulesCreateScheduleOverrideResponse401
from ...models.opsduty_api_v1_schedules_create_schedule_override_response_404 import OpsdutyApiV1SchedulesCreateScheduleOverrideResponse404
from ...models.opsduty_api_v1_schedules_create_schedule_override_response_422 import OpsdutyApiV1SchedulesCreateScheduleOverrideResponse422
from ...models.schedule_override_input_schema import ScheduleOverrideInputSchema
from ...models.schedule_override_schema import ScheduleOverrideSchema
from ...types import Response


def _get_kwargs(
    schedule_id: int,
    *,
    body: ScheduleOverrideInputSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/schedules/{schedule_id}/overrides/".format(
            schedule_id=quote(str(schedule_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> OpsdutyApiV1SchedulesCreateScheduleOverrideResponse401 | OpsdutyApiV1SchedulesCreateScheduleOverrideResponse404 | OpsdutyApiV1SchedulesCreateScheduleOverrideResponse422 | ScheduleOverrideSchema | None:
    if response.status_code == 201:
        response_201 = ScheduleOverrideSchema.from_dict(response.json())

        return response_201

    if response.status_code == 401:
        response_401 = OpsdutyApiV1SchedulesCreateScheduleOverrideResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = OpsdutyApiV1SchedulesCreateScheduleOverrideResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = OpsdutyApiV1SchedulesCreateScheduleOverrideResponse422.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[OpsdutyApiV1SchedulesCreateScheduleOverrideResponse401 | OpsdutyApiV1SchedulesCreateScheduleOverrideResponse404 | OpsdutyApiV1SchedulesCreateScheduleOverrideResponse422 | ScheduleOverrideSchema]:
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
    body: ScheduleOverrideInputSchema,
) -> Response[OpsdutyApiV1SchedulesCreateScheduleOverrideResponse401 | OpsdutyApiV1SchedulesCreateScheduleOverrideResponse404 | OpsdutyApiV1SchedulesCreateScheduleOverrideResponse422 | ScheduleOverrideSchema]:
    """Create a schedule override

     Put one person on call for a stretch of a schedule, covering the rotation.

    Use this to arrange cover when someone cannot take their shift. `user` has
    to be a member of the schedule, and is rejected otherwise.

    Args:
        schedule_id (int):
        body (ScheduleOverrideInputSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OpsdutyApiV1SchedulesCreateScheduleOverrideResponse401 | OpsdutyApiV1SchedulesCreateScheduleOverrideResponse404 | OpsdutyApiV1SchedulesCreateScheduleOverrideResponse422 | ScheduleOverrideSchema]
    """

    kwargs = _get_kwargs(
        schedule_id=schedule_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    schedule_id: int,
    *,
    client: AuthenticatedClient,
    body: ScheduleOverrideInputSchema,
) -> OpsdutyApiV1SchedulesCreateScheduleOverrideResponse401 | OpsdutyApiV1SchedulesCreateScheduleOverrideResponse404 | OpsdutyApiV1SchedulesCreateScheduleOverrideResponse422 | ScheduleOverrideSchema | None:
    """Create a schedule override

     Put one person on call for a stretch of a schedule, covering the rotation.

    Use this to arrange cover when someone cannot take their shift. `user` has
    to be a member of the schedule, and is rejected otherwise.

    Args:
        schedule_id (int):
        body (ScheduleOverrideInputSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OpsdutyApiV1SchedulesCreateScheduleOverrideResponse401 | OpsdutyApiV1SchedulesCreateScheduleOverrideResponse404 | OpsdutyApiV1SchedulesCreateScheduleOverrideResponse422 | ScheduleOverrideSchema
    """

    return sync_detailed(
        schedule_id=schedule_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    schedule_id: int,
    *,
    client: AuthenticatedClient,
    body: ScheduleOverrideInputSchema,
) -> Response[OpsdutyApiV1SchedulesCreateScheduleOverrideResponse401 | OpsdutyApiV1SchedulesCreateScheduleOverrideResponse404 | OpsdutyApiV1SchedulesCreateScheduleOverrideResponse422 | ScheduleOverrideSchema]:
    """Create a schedule override

     Put one person on call for a stretch of a schedule, covering the rotation.

    Use this to arrange cover when someone cannot take their shift. `user` has
    to be a member of the schedule, and is rejected otherwise.

    Args:
        schedule_id (int):
        body (ScheduleOverrideInputSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OpsdutyApiV1SchedulesCreateScheduleOverrideResponse401 | OpsdutyApiV1SchedulesCreateScheduleOverrideResponse404 | OpsdutyApiV1SchedulesCreateScheduleOverrideResponse422 | ScheduleOverrideSchema]
    """

    kwargs = _get_kwargs(
        schedule_id=schedule_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    schedule_id: int,
    *,
    client: AuthenticatedClient,
    body: ScheduleOverrideInputSchema,
) -> OpsdutyApiV1SchedulesCreateScheduleOverrideResponse401 | OpsdutyApiV1SchedulesCreateScheduleOverrideResponse404 | OpsdutyApiV1SchedulesCreateScheduleOverrideResponse422 | ScheduleOverrideSchema | None:
    """Create a schedule override

     Put one person on call for a stretch of a schedule, covering the rotation.

    Use this to arrange cover when someone cannot take their shift. `user` has
    to be a member of the schedule, and is rejected otherwise.

    Args:
        schedule_id (int):
        body (ScheduleOverrideInputSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OpsdutyApiV1SchedulesCreateScheduleOverrideResponse401 | OpsdutyApiV1SchedulesCreateScheduleOverrideResponse404 | OpsdutyApiV1SchedulesCreateScheduleOverrideResponse422 | ScheduleOverrideSchema
    """

    return (
        await asyncio_detailed(
            schedule_id=schedule_id,
            client=client,
            body=body,
        )
    ).parsed
