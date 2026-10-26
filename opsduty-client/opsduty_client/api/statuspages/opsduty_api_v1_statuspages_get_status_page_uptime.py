from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.opsduty_api_v1_statuspages_get_status_page_uptime_response_401 import OpsdutyApiV1StatuspagesGetStatusPageUptimeResponse401
from ...models.opsduty_api_v1_statuspages_get_status_page_uptime_response_404 import OpsdutyApiV1StatuspagesGetStatusPageUptimeResponse404
from ...models.opsduty_api_v1_statuspages_get_status_page_uptime_response_422 import OpsdutyApiV1StatuspagesGetStatusPageUptimeResponse422
from ...models.status_page_uptime_schema import StatusPageUptimeSchema
from ...types import Response


def _get_kwargs(
    status_page_id: int,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/statuspages/{status_page_id}/uptime/".format(
            status_page_id=quote(str(status_page_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> OpsdutyApiV1StatuspagesGetStatusPageUptimeResponse401 | OpsdutyApiV1StatuspagesGetStatusPageUptimeResponse404 | OpsdutyApiV1StatuspagesGetStatusPageUptimeResponse422 | StatusPageUptimeSchema | None:
    if response.status_code == 200:
        response_200 = StatusPageUptimeSchema.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = OpsdutyApiV1StatuspagesGetStatusPageUptimeResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = OpsdutyApiV1StatuspagesGetStatusPageUptimeResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = OpsdutyApiV1StatuspagesGetStatusPageUptimeResponse422.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[OpsdutyApiV1StatuspagesGetStatusPageUptimeResponse401 | OpsdutyApiV1StatuspagesGetStatusPageUptimeResponse404 | OpsdutyApiV1StatuspagesGetStatusPageUptimeResponse422 | StatusPageUptimeSchema]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    status_page_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[OpsdutyApiV1StatuspagesGetStatusPageUptimeResponse401 | OpsdutyApiV1StatuspagesGetStatusPageUptimeResponse404 | OpsdutyApiV1StatuspagesGetStatusPageUptimeResponse422 | StatusPageUptimeSchema]:
    """Read a status page's component uptime

     The ninety day uptime this page reports for each of its components.

    This is the same figure the public page shows, so a dashboard built on it
    agrees with what customers read rather than recomputing it and drifting.
    Downtime is any period a component was showing degraded performance or
    worse, whether an incident explained it or somebody set the status
    directly.

    Args:
        status_page_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OpsdutyApiV1StatuspagesGetStatusPageUptimeResponse401 | OpsdutyApiV1StatuspagesGetStatusPageUptimeResponse404 | OpsdutyApiV1StatuspagesGetStatusPageUptimeResponse422 | StatusPageUptimeSchema]
    """

    kwargs = _get_kwargs(
        status_page_id=status_page_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    status_page_id: int,
    *,
    client: AuthenticatedClient,
) -> OpsdutyApiV1StatuspagesGetStatusPageUptimeResponse401 | OpsdutyApiV1StatuspagesGetStatusPageUptimeResponse404 | OpsdutyApiV1StatuspagesGetStatusPageUptimeResponse422 | StatusPageUptimeSchema | None:
    """Read a status page's component uptime

     The ninety day uptime this page reports for each of its components.

    This is the same figure the public page shows, so a dashboard built on it
    agrees with what customers read rather than recomputing it and drifting.
    Downtime is any period a component was showing degraded performance or
    worse, whether an incident explained it or somebody set the status
    directly.

    Args:
        status_page_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OpsdutyApiV1StatuspagesGetStatusPageUptimeResponse401 | OpsdutyApiV1StatuspagesGetStatusPageUptimeResponse404 | OpsdutyApiV1StatuspagesGetStatusPageUptimeResponse422 | StatusPageUptimeSchema
    """

    return sync_detailed(
        status_page_id=status_page_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    status_page_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[OpsdutyApiV1StatuspagesGetStatusPageUptimeResponse401 | OpsdutyApiV1StatuspagesGetStatusPageUptimeResponse404 | OpsdutyApiV1StatuspagesGetStatusPageUptimeResponse422 | StatusPageUptimeSchema]:
    """Read a status page's component uptime

     The ninety day uptime this page reports for each of its components.

    This is the same figure the public page shows, so a dashboard built on it
    agrees with what customers read rather than recomputing it and drifting.
    Downtime is any period a component was showing degraded performance or
    worse, whether an incident explained it or somebody set the status
    directly.

    Args:
        status_page_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OpsdutyApiV1StatuspagesGetStatusPageUptimeResponse401 | OpsdutyApiV1StatuspagesGetStatusPageUptimeResponse404 | OpsdutyApiV1StatuspagesGetStatusPageUptimeResponse422 | StatusPageUptimeSchema]
    """

    kwargs = _get_kwargs(
        status_page_id=status_page_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    status_page_id: int,
    *,
    client: AuthenticatedClient,
) -> OpsdutyApiV1StatuspagesGetStatusPageUptimeResponse401 | OpsdutyApiV1StatuspagesGetStatusPageUptimeResponse404 | OpsdutyApiV1StatuspagesGetStatusPageUptimeResponse422 | StatusPageUptimeSchema | None:
    """Read a status page's component uptime

     The ninety day uptime this page reports for each of its components.

    This is the same figure the public page shows, so a dashboard built on it
    agrees with what customers read rather than recomputing it and drifting.
    Downtime is any period a component was showing degraded performance or
    worse, whether an incident explained it or somebody set the status
    directly.

    Args:
        status_page_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OpsdutyApiV1StatuspagesGetStatusPageUptimeResponse401 | OpsdutyApiV1StatuspagesGetStatusPageUptimeResponse404 | OpsdutyApiV1StatuspagesGetStatusPageUptimeResponse422 | StatusPageUptimeSchema
    """

    return (
        await asyncio_detailed(
            status_page_id=status_page_id,
            client=client,
        )
    ).parsed
