from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.heartbeat_schema import HeartbeatSchema
from ...models.opsduty_api_v1_heartbeats_update_heartbeat_response_401 import OpsdutyApiV1HeartbeatsUpdateHeartbeatResponse401
from ...models.opsduty_api_v1_heartbeats_update_heartbeat_response_404 import OpsdutyApiV1HeartbeatsUpdateHeartbeatResponse404
from ...models.opsduty_api_v1_heartbeats_update_heartbeat_response_422 import OpsdutyApiV1HeartbeatsUpdateHeartbeatResponse422
from ...models.update_heartbeat_input import UpdateHeartbeatInput
from ...types import Response


def _get_kwargs(
    heartbeat_id: int,
    *,
    body: UpdateHeartbeatInput,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/v1/heartbeats/{heartbeat_id}/".format(
            heartbeat_id=quote(str(heartbeat_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HeartbeatSchema | OpsdutyApiV1HeartbeatsUpdateHeartbeatResponse401 | OpsdutyApiV1HeartbeatsUpdateHeartbeatResponse404 | OpsdutyApiV1HeartbeatsUpdateHeartbeatResponse422 | None:
    if response.status_code == 200:
        response_200 = HeartbeatSchema.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = OpsdutyApiV1HeartbeatsUpdateHeartbeatResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = OpsdutyApiV1HeartbeatsUpdateHeartbeatResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = OpsdutyApiV1HeartbeatsUpdateHeartbeatResponse422.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[HeartbeatSchema | OpsdutyApiV1HeartbeatsUpdateHeartbeatResponse401 | OpsdutyApiV1HeartbeatsUpdateHeartbeatResponse404 | OpsdutyApiV1HeartbeatsUpdateHeartbeatResponse422]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    heartbeat_id: int,
    *,
    client: AuthenticatedClient,
    body: UpdateHeartbeatInput,
) -> Response[HeartbeatSchema | OpsdutyApiV1HeartbeatsUpdateHeartbeatResponse401 | OpsdutyApiV1HeartbeatsUpdateHeartbeatResponse404 | OpsdutyApiV1HeartbeatsUpdateHeartbeatResponse422]:
    """Update a heartbeat

     Change a heartbeat's details.

    Every field is replaced, so send the whole heartbeat. This covers what the
    job is and who hears about it; the schedule it checks in on lives on each
    environment.

    Args:
        heartbeat_id (int):
        body (UpdateHeartbeatInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HeartbeatSchema | OpsdutyApiV1HeartbeatsUpdateHeartbeatResponse401 | OpsdutyApiV1HeartbeatsUpdateHeartbeatResponse404 | OpsdutyApiV1HeartbeatsUpdateHeartbeatResponse422]
    """

    kwargs = _get_kwargs(
        heartbeat_id=heartbeat_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    heartbeat_id: int,
    *,
    client: AuthenticatedClient,
    body: UpdateHeartbeatInput,
) -> HeartbeatSchema | OpsdutyApiV1HeartbeatsUpdateHeartbeatResponse401 | OpsdutyApiV1HeartbeatsUpdateHeartbeatResponse404 | OpsdutyApiV1HeartbeatsUpdateHeartbeatResponse422 | None:
    """Update a heartbeat

     Change a heartbeat's details.

    Every field is replaced, so send the whole heartbeat. This covers what the
    job is and who hears about it; the schedule it checks in on lives on each
    environment.

    Args:
        heartbeat_id (int):
        body (UpdateHeartbeatInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HeartbeatSchema | OpsdutyApiV1HeartbeatsUpdateHeartbeatResponse401 | OpsdutyApiV1HeartbeatsUpdateHeartbeatResponse404 | OpsdutyApiV1HeartbeatsUpdateHeartbeatResponse422
    """

    return sync_detailed(
        heartbeat_id=heartbeat_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    heartbeat_id: int,
    *,
    client: AuthenticatedClient,
    body: UpdateHeartbeatInput,
) -> Response[HeartbeatSchema | OpsdutyApiV1HeartbeatsUpdateHeartbeatResponse401 | OpsdutyApiV1HeartbeatsUpdateHeartbeatResponse404 | OpsdutyApiV1HeartbeatsUpdateHeartbeatResponse422]:
    """Update a heartbeat

     Change a heartbeat's details.

    Every field is replaced, so send the whole heartbeat. This covers what the
    job is and who hears about it; the schedule it checks in on lives on each
    environment.

    Args:
        heartbeat_id (int):
        body (UpdateHeartbeatInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HeartbeatSchema | OpsdutyApiV1HeartbeatsUpdateHeartbeatResponse401 | OpsdutyApiV1HeartbeatsUpdateHeartbeatResponse404 | OpsdutyApiV1HeartbeatsUpdateHeartbeatResponse422]
    """

    kwargs = _get_kwargs(
        heartbeat_id=heartbeat_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    heartbeat_id: int,
    *,
    client: AuthenticatedClient,
    body: UpdateHeartbeatInput,
) -> HeartbeatSchema | OpsdutyApiV1HeartbeatsUpdateHeartbeatResponse401 | OpsdutyApiV1HeartbeatsUpdateHeartbeatResponse404 | OpsdutyApiV1HeartbeatsUpdateHeartbeatResponse422 | None:
    """Update a heartbeat

     Change a heartbeat's details.

    Every field is replaced, so send the whole heartbeat. This covers what the
    job is and who hears about it; the schedule it checks in on lives on each
    environment.

    Args:
        heartbeat_id (int):
        body (UpdateHeartbeatInput):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HeartbeatSchema | OpsdutyApiV1HeartbeatsUpdateHeartbeatResponse401 | OpsdutyApiV1HeartbeatsUpdateHeartbeatResponse404 | OpsdutyApiV1HeartbeatsUpdateHeartbeatResponse422
    """

    return (
        await asyncio_detailed(
            heartbeat_id=heartbeat_id,
            client=client,
            body=body,
        )
    ).parsed
