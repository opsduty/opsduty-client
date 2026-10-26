from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_heartbeat_state_input import CreateHeartbeatStateInput
from ...models.cron_heartbeat_state_schema import CronHeartbeatStateSchema
from ...models.interval_heartbeat_state_schema import IntervalHeartbeatStateSchema
from ...models.opsduty_api_v1_heartbeats_create_heartbeat_state_response_401 import OpsdutyApiV1HeartbeatsCreateHeartbeatStateResponse401
from ...models.opsduty_api_v1_heartbeats_create_heartbeat_state_response_422 import OpsdutyApiV1HeartbeatsCreateHeartbeatStateResponse422
from ...types import Response


def _get_kwargs(
    *,
    body: CreateHeartbeatStateInput,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/heartbeats/states/",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CronHeartbeatStateSchema | IntervalHeartbeatStateSchema | OpsdutyApiV1HeartbeatsCreateHeartbeatStateResponse401 | OpsdutyApiV1HeartbeatsCreateHeartbeatStateResponse422 | None:
    if response.status_code == 201:

        def _parse_response_201(data: object) -> CronHeartbeatStateSchema | IntervalHeartbeatStateSchema:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_201_type_0 = CronHeartbeatStateSchema.from_dict(data)

                return response_201_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_201_type_1 = IntervalHeartbeatStateSchema.from_dict(data)

            return response_201_type_1

        response_201 = _parse_response_201(response.json())

        return response_201

    if response.status_code == 401:
        response_401 = OpsdutyApiV1HeartbeatsCreateHeartbeatStateResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 422:
        response_422 = OpsdutyApiV1HeartbeatsCreateHeartbeatStateResponse422.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CronHeartbeatStateSchema | IntervalHeartbeatStateSchema | OpsdutyApiV1HeartbeatsCreateHeartbeatStateResponse401 | OpsdutyApiV1HeartbeatsCreateHeartbeatStateResponse422]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateHeartbeatStateInput,
) -> Response[CronHeartbeatStateSchema | IntervalHeartbeatStateSchema | OpsdutyApiV1HeartbeatsCreateHeartbeatStateResponse401 | OpsdutyApiV1HeartbeatsCreateHeartbeatStateResponse422]:
    """Add an environment to a heartbeat

     Start expecting check-ins from one environment of a job.

    A heartbeat on its own watches nothing. Each environment you add here gets
    its own schedule and its own check-in URL, so the same job in staging and
    production alert separately.

    Set `type` to `interval` and give `interval_seconds` for a job that runs
    every so often, or `cron` with `cron_expression` and `cron_timezone` for
    one on a fixed timetable. `timeout_seconds` is the grace period on top of
    that before OpsDuty decides the check-in is missing.

    Args:
        body (CreateHeartbeatStateInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CronHeartbeatStateSchema | IntervalHeartbeatStateSchema | OpsdutyApiV1HeartbeatsCreateHeartbeatStateResponse401 | OpsdutyApiV1HeartbeatsCreateHeartbeatStateResponse422]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: CreateHeartbeatStateInput,
) -> CronHeartbeatStateSchema | IntervalHeartbeatStateSchema | OpsdutyApiV1HeartbeatsCreateHeartbeatStateResponse401 | OpsdutyApiV1HeartbeatsCreateHeartbeatStateResponse422 | None:
    """Add an environment to a heartbeat

     Start expecting check-ins from one environment of a job.

    A heartbeat on its own watches nothing. Each environment you add here gets
    its own schedule and its own check-in URL, so the same job in staging and
    production alert separately.

    Set `type` to `interval` and give `interval_seconds` for a job that runs
    every so often, or `cron` with `cron_expression` and `cron_timezone` for
    one on a fixed timetable. `timeout_seconds` is the grace period on top of
    that before OpsDuty decides the check-in is missing.

    Args:
        body (CreateHeartbeatStateInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CronHeartbeatStateSchema | IntervalHeartbeatStateSchema | OpsdutyApiV1HeartbeatsCreateHeartbeatStateResponse401 | OpsdutyApiV1HeartbeatsCreateHeartbeatStateResponse422
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateHeartbeatStateInput,
) -> Response[CronHeartbeatStateSchema | IntervalHeartbeatStateSchema | OpsdutyApiV1HeartbeatsCreateHeartbeatStateResponse401 | OpsdutyApiV1HeartbeatsCreateHeartbeatStateResponse422]:
    """Add an environment to a heartbeat

     Start expecting check-ins from one environment of a job.

    A heartbeat on its own watches nothing. Each environment you add here gets
    its own schedule and its own check-in URL, so the same job in staging and
    production alert separately.

    Set `type` to `interval` and give `interval_seconds` for a job that runs
    every so often, or `cron` with `cron_expression` and `cron_timezone` for
    one on a fixed timetable. `timeout_seconds` is the grace period on top of
    that before OpsDuty decides the check-in is missing.

    Args:
        body (CreateHeartbeatStateInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CronHeartbeatStateSchema | IntervalHeartbeatStateSchema | OpsdutyApiV1HeartbeatsCreateHeartbeatStateResponse401 | OpsdutyApiV1HeartbeatsCreateHeartbeatStateResponse422]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: CreateHeartbeatStateInput,
) -> CronHeartbeatStateSchema | IntervalHeartbeatStateSchema | OpsdutyApiV1HeartbeatsCreateHeartbeatStateResponse401 | OpsdutyApiV1HeartbeatsCreateHeartbeatStateResponse422 | None:
    """Add an environment to a heartbeat

     Start expecting check-ins from one environment of a job.

    A heartbeat on its own watches nothing. Each environment you add here gets
    its own schedule and its own check-in URL, so the same job in staging and
    production alert separately.

    Set `type` to `interval` and give `interval_seconds` for a job that runs
    every so often, or `cron` with `cron_expression` and `cron_timezone` for
    one on a fixed timetable. `timeout_seconds` is the grace period on top of
    that before OpsDuty decides the check-in is missing.

    Args:
        body (CreateHeartbeatStateInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CronHeartbeatStateSchema | IntervalHeartbeatStateSchema | OpsdutyApiV1HeartbeatsCreateHeartbeatStateResponse401 | OpsdutyApiV1HeartbeatsCreateHeartbeatStateResponse422
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
