from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.cron_heartbeat_state_schema import CronHeartbeatStateSchema
from ...models.interval_heartbeat_state_schema import IntervalHeartbeatStateSchema
from ...models.opsduty_api_v1_heartbeats_update_heartbeat_state_response_401 import OpsdutyApiV1HeartbeatsUpdateHeartbeatStateResponse401
from ...models.opsduty_api_v1_heartbeats_update_heartbeat_state_response_404 import OpsdutyApiV1HeartbeatsUpdateHeartbeatStateResponse404
from ...models.opsduty_api_v1_heartbeats_update_heartbeat_state_response_422 import OpsdutyApiV1HeartbeatsUpdateHeartbeatStateResponse422
from ...models.update_heartbeat_state_input import UpdateHeartbeatStateInput
from ...types import Response


def _get_kwargs(
    heartbeat_state_id: int,
    *,
    body: UpdateHeartbeatStateInput,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/v1/heartbeats/states/{heartbeat_state_id}/".format(
            heartbeat_state_id=quote(str(heartbeat_state_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CronHeartbeatStateSchema | IntervalHeartbeatStateSchema | OpsdutyApiV1HeartbeatsUpdateHeartbeatStateResponse401 | OpsdutyApiV1HeartbeatsUpdateHeartbeatStateResponse404 | OpsdutyApiV1HeartbeatsUpdateHeartbeatStateResponse422 | None:
    if response.status_code == 200:

        def _parse_response_200(data: object) -> CronHeartbeatStateSchema | IntervalHeartbeatStateSchema:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_0 = CronHeartbeatStateSchema.from_dict(data)

                return response_200_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_200_type_1 = IntervalHeartbeatStateSchema.from_dict(data)

            return response_200_type_1

        response_200 = _parse_response_200(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = OpsdutyApiV1HeartbeatsUpdateHeartbeatStateResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = OpsdutyApiV1HeartbeatsUpdateHeartbeatStateResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = OpsdutyApiV1HeartbeatsUpdateHeartbeatStateResponse422.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[CronHeartbeatStateSchema | IntervalHeartbeatStateSchema | OpsdutyApiV1HeartbeatsUpdateHeartbeatStateResponse401 | OpsdutyApiV1HeartbeatsUpdateHeartbeatStateResponse404 | OpsdutyApiV1HeartbeatsUpdateHeartbeatStateResponse422]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    heartbeat_state_id: int,
    *,
    client: AuthenticatedClient,
    body: UpdateHeartbeatStateInput,
) -> Response[CronHeartbeatStateSchema | IntervalHeartbeatStateSchema | OpsdutyApiV1HeartbeatsUpdateHeartbeatStateResponse401 | OpsdutyApiV1HeartbeatsUpdateHeartbeatStateResponse404 | OpsdutyApiV1HeartbeatsUpdateHeartbeatStateResponse422]:
    """Update an environment on a heartbeat

     Change what one environment expects, or stop it alerting.

    Every field is replaced, so send the whole state and not only the parts
    you are changing. Set `muted` while a job is knowingly off, which keeps
    the environment and its history but stops it raising incidents.

    Args:
        heartbeat_state_id (int):
        body (UpdateHeartbeatStateInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CronHeartbeatStateSchema | IntervalHeartbeatStateSchema | OpsdutyApiV1HeartbeatsUpdateHeartbeatStateResponse401 | OpsdutyApiV1HeartbeatsUpdateHeartbeatStateResponse404 | OpsdutyApiV1HeartbeatsUpdateHeartbeatStateResponse422]
    """

    kwargs = _get_kwargs(
        heartbeat_state_id=heartbeat_state_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    heartbeat_state_id: int,
    *,
    client: AuthenticatedClient,
    body: UpdateHeartbeatStateInput,
) -> CronHeartbeatStateSchema | IntervalHeartbeatStateSchema | OpsdutyApiV1HeartbeatsUpdateHeartbeatStateResponse401 | OpsdutyApiV1HeartbeatsUpdateHeartbeatStateResponse404 | OpsdutyApiV1HeartbeatsUpdateHeartbeatStateResponse422 | None:
    """Update an environment on a heartbeat

     Change what one environment expects, or stop it alerting.

    Every field is replaced, so send the whole state and not only the parts
    you are changing. Set `muted` while a job is knowingly off, which keeps
    the environment and its history but stops it raising incidents.

    Args:
        heartbeat_state_id (int):
        body (UpdateHeartbeatStateInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CronHeartbeatStateSchema | IntervalHeartbeatStateSchema | OpsdutyApiV1HeartbeatsUpdateHeartbeatStateResponse401 | OpsdutyApiV1HeartbeatsUpdateHeartbeatStateResponse404 | OpsdutyApiV1HeartbeatsUpdateHeartbeatStateResponse422
    """

    return sync_detailed(
        heartbeat_state_id=heartbeat_state_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    heartbeat_state_id: int,
    *,
    client: AuthenticatedClient,
    body: UpdateHeartbeatStateInput,
) -> Response[CronHeartbeatStateSchema | IntervalHeartbeatStateSchema | OpsdutyApiV1HeartbeatsUpdateHeartbeatStateResponse401 | OpsdutyApiV1HeartbeatsUpdateHeartbeatStateResponse404 | OpsdutyApiV1HeartbeatsUpdateHeartbeatStateResponse422]:
    """Update an environment on a heartbeat

     Change what one environment expects, or stop it alerting.

    Every field is replaced, so send the whole state and not only the parts
    you are changing. Set `muted` while a job is knowingly off, which keeps
    the environment and its history but stops it raising incidents.

    Args:
        heartbeat_state_id (int):
        body (UpdateHeartbeatStateInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CronHeartbeatStateSchema | IntervalHeartbeatStateSchema | OpsdutyApiV1HeartbeatsUpdateHeartbeatStateResponse401 | OpsdutyApiV1HeartbeatsUpdateHeartbeatStateResponse404 | OpsdutyApiV1HeartbeatsUpdateHeartbeatStateResponse422]
    """

    kwargs = _get_kwargs(
        heartbeat_state_id=heartbeat_state_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    heartbeat_state_id: int,
    *,
    client: AuthenticatedClient,
    body: UpdateHeartbeatStateInput,
) -> CronHeartbeatStateSchema | IntervalHeartbeatStateSchema | OpsdutyApiV1HeartbeatsUpdateHeartbeatStateResponse401 | OpsdutyApiV1HeartbeatsUpdateHeartbeatStateResponse404 | OpsdutyApiV1HeartbeatsUpdateHeartbeatStateResponse422 | None:
    """Update an environment on a heartbeat

     Change what one environment expects, or stop it alerting.

    Every field is replaced, so send the whole state and not only the parts
    you are changing. Set `muted` while a job is knowingly off, which keeps
    the environment and its history but stops it raising incidents.

    Args:
        heartbeat_state_id (int):
        body (UpdateHeartbeatStateInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CronHeartbeatStateSchema | IntervalHeartbeatStateSchema | OpsdutyApiV1HeartbeatsUpdateHeartbeatStateResponse401 | OpsdutyApiV1HeartbeatsUpdateHeartbeatStateResponse404 | OpsdutyApiV1HeartbeatsUpdateHeartbeatStateResponse422
    """

    return (
        await asyncio_detailed(
            heartbeat_state_id=heartbeat_state_id,
            client=client,
            body=body,
        )
    ).parsed
