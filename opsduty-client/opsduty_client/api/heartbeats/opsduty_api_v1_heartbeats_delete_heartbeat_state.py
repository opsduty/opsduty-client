from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.opsduty_api_v1_heartbeats_delete_heartbeat_state_response_401 import OpsdutyApiV1HeartbeatsDeleteHeartbeatStateResponse401
from ...models.opsduty_api_v1_heartbeats_delete_heartbeat_state_response_404 import OpsdutyApiV1HeartbeatsDeleteHeartbeatStateResponse404
from ...models.opsduty_api_v1_heartbeats_delete_heartbeat_state_response_422 import OpsdutyApiV1HeartbeatsDeleteHeartbeatStateResponse422
from ...types import Response


def _get_kwargs(
    heartbeat_state_id: int,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/v1/heartbeats/states/{heartbeat_state_id}/".format(
            heartbeat_state_id=quote(str(heartbeat_state_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | OpsdutyApiV1HeartbeatsDeleteHeartbeatStateResponse401 | OpsdutyApiV1HeartbeatsDeleteHeartbeatStateResponse404 | OpsdutyApiV1HeartbeatsDeleteHeartbeatStateResponse422 | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 401:
        response_401 = OpsdutyApiV1HeartbeatsDeleteHeartbeatStateResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = OpsdutyApiV1HeartbeatsDeleteHeartbeatStateResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = OpsdutyApiV1HeartbeatsDeleteHeartbeatStateResponse422.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | OpsdutyApiV1HeartbeatsDeleteHeartbeatStateResponse401 | OpsdutyApiV1HeartbeatsDeleteHeartbeatStateResponse404 | OpsdutyApiV1HeartbeatsDeleteHeartbeatStateResponse422]:
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
) -> Response[Any | OpsdutyApiV1HeartbeatsDeleteHeartbeatStateResponse401 | OpsdutyApiV1HeartbeatsDeleteHeartbeatStateResponse404 | OpsdutyApiV1HeartbeatsDeleteHeartbeatStateResponse422]:
    """Remove an environment from a heartbeat

     Stop watching one environment, and drop its check-in history with it.

    Check-ins sent to that environment's URL afterwards are answered with a
    404. To stop the alerts but keep the history, update the state and set
    `muted` instead.

    Args:
        heartbeat_state_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | OpsdutyApiV1HeartbeatsDeleteHeartbeatStateResponse401 | OpsdutyApiV1HeartbeatsDeleteHeartbeatStateResponse404 | OpsdutyApiV1HeartbeatsDeleteHeartbeatStateResponse422]
    """

    kwargs = _get_kwargs(
        heartbeat_state_id=heartbeat_state_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    heartbeat_state_id: int,
    *,
    client: AuthenticatedClient,
) -> Any | OpsdutyApiV1HeartbeatsDeleteHeartbeatStateResponse401 | OpsdutyApiV1HeartbeatsDeleteHeartbeatStateResponse404 | OpsdutyApiV1HeartbeatsDeleteHeartbeatStateResponse422 | None:
    """Remove an environment from a heartbeat

     Stop watching one environment, and drop its check-in history with it.

    Check-ins sent to that environment's URL afterwards are answered with a
    404. To stop the alerts but keep the history, update the state and set
    `muted` instead.

    Args:
        heartbeat_state_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | OpsdutyApiV1HeartbeatsDeleteHeartbeatStateResponse401 | OpsdutyApiV1HeartbeatsDeleteHeartbeatStateResponse404 | OpsdutyApiV1HeartbeatsDeleteHeartbeatStateResponse422
    """

    return sync_detailed(
        heartbeat_state_id=heartbeat_state_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    heartbeat_state_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Any | OpsdutyApiV1HeartbeatsDeleteHeartbeatStateResponse401 | OpsdutyApiV1HeartbeatsDeleteHeartbeatStateResponse404 | OpsdutyApiV1HeartbeatsDeleteHeartbeatStateResponse422]:
    """Remove an environment from a heartbeat

     Stop watching one environment, and drop its check-in history with it.

    Check-ins sent to that environment's URL afterwards are answered with a
    404. To stop the alerts but keep the history, update the state and set
    `muted` instead.

    Args:
        heartbeat_state_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | OpsdutyApiV1HeartbeatsDeleteHeartbeatStateResponse401 | OpsdutyApiV1HeartbeatsDeleteHeartbeatStateResponse404 | OpsdutyApiV1HeartbeatsDeleteHeartbeatStateResponse422]
    """

    kwargs = _get_kwargs(
        heartbeat_state_id=heartbeat_state_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    heartbeat_state_id: int,
    *,
    client: AuthenticatedClient,
) -> Any | OpsdutyApiV1HeartbeatsDeleteHeartbeatStateResponse401 | OpsdutyApiV1HeartbeatsDeleteHeartbeatStateResponse404 | OpsdutyApiV1HeartbeatsDeleteHeartbeatStateResponse422 | None:
    """Remove an environment from a heartbeat

     Stop watching one environment, and drop its check-in history with it.

    Check-ins sent to that environment's URL afterwards are answered with a
    404. To stop the alerts but keep the history, update the state and set
    `muted` instead.

    Args:
        heartbeat_state_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | OpsdutyApiV1HeartbeatsDeleteHeartbeatStateResponse401 | OpsdutyApiV1HeartbeatsDeleteHeartbeatStateResponse404 | OpsdutyApiV1HeartbeatsDeleteHeartbeatStateResponse422
    """

    return (
        await asyncio_detailed(
            heartbeat_state_id=heartbeat_state_id,
            client=client,
        )
    ).parsed
