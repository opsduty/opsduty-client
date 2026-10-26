from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.incident_postmortem_schema import IncidentPostmortemSchema
from ...models.opsduty_api_v1_statuspages_read_status_page_incident_postmortem_response_401 import OpsdutyApiV1StatuspagesReadStatusPageIncidentPostmortemResponse401
from ...models.opsduty_api_v1_statuspages_read_status_page_incident_postmortem_response_404 import OpsdutyApiV1StatuspagesReadStatusPageIncidentPostmortemResponse404
from ...models.opsduty_api_v1_statuspages_read_status_page_incident_postmortem_response_422 import OpsdutyApiV1StatuspagesReadStatusPageIncidentPostmortemResponse422
from ...types import Response


def _get_kwargs(
    incident_id: int,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/statuspages/incidents/{incident_id}/postmortem/".format(
            incident_id=quote(str(incident_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> IncidentPostmortemSchema | OpsdutyApiV1StatuspagesReadStatusPageIncidentPostmortemResponse401 | OpsdutyApiV1StatuspagesReadStatusPageIncidentPostmortemResponse404 | OpsdutyApiV1StatuspagesReadStatusPageIncidentPostmortemResponse422 | None:
    if response.status_code == 200:
        response_200 = IncidentPostmortemSchema.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = OpsdutyApiV1StatuspagesReadStatusPageIncidentPostmortemResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = OpsdutyApiV1StatuspagesReadStatusPageIncidentPostmortemResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = OpsdutyApiV1StatuspagesReadStatusPageIncidentPostmortemResponse422.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[IncidentPostmortemSchema | OpsdutyApiV1StatuspagesReadStatusPageIncidentPostmortemResponse401 | OpsdutyApiV1StatuspagesReadStatusPageIncidentPostmortemResponse404 | OpsdutyApiV1StatuspagesReadStatusPageIncidentPostmortemResponse422]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    incident_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[IncidentPostmortemSchema | OpsdutyApiV1StatuspagesReadStatusPageIncidentPostmortemResponse401 | OpsdutyApiV1StatuspagesReadStatusPageIncidentPostmortemResponse404 | OpsdutyApiV1StatuspagesReadStatusPageIncidentPostmortemResponse422]:
    """Read a status page incident's postmortem

     Read the postmortem written for an incident, published or not.

    Raises a validation error when the incident has no postmortem yet.

    Args:
        incident_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IncidentPostmortemSchema | OpsdutyApiV1StatuspagesReadStatusPageIncidentPostmortemResponse401 | OpsdutyApiV1StatuspagesReadStatusPageIncidentPostmortemResponse404 | OpsdutyApiV1StatuspagesReadStatusPageIncidentPostmortemResponse422]
    """

    kwargs = _get_kwargs(
        incident_id=incident_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    incident_id: int,
    *,
    client: AuthenticatedClient,
) -> IncidentPostmortemSchema | OpsdutyApiV1StatuspagesReadStatusPageIncidentPostmortemResponse401 | OpsdutyApiV1StatuspagesReadStatusPageIncidentPostmortemResponse404 | OpsdutyApiV1StatuspagesReadStatusPageIncidentPostmortemResponse422 | None:
    """Read a status page incident's postmortem

     Read the postmortem written for an incident, published or not.

    Raises a validation error when the incident has no postmortem yet.

    Args:
        incident_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IncidentPostmortemSchema | OpsdutyApiV1StatuspagesReadStatusPageIncidentPostmortemResponse401 | OpsdutyApiV1StatuspagesReadStatusPageIncidentPostmortemResponse404 | OpsdutyApiV1StatuspagesReadStatusPageIncidentPostmortemResponse422
    """

    return sync_detailed(
        incident_id=incident_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    incident_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[IncidentPostmortemSchema | OpsdutyApiV1StatuspagesReadStatusPageIncidentPostmortemResponse401 | OpsdutyApiV1StatuspagesReadStatusPageIncidentPostmortemResponse404 | OpsdutyApiV1StatuspagesReadStatusPageIncidentPostmortemResponse422]:
    """Read a status page incident's postmortem

     Read the postmortem written for an incident, published or not.

    Raises a validation error when the incident has no postmortem yet.

    Args:
        incident_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IncidentPostmortemSchema | OpsdutyApiV1StatuspagesReadStatusPageIncidentPostmortemResponse401 | OpsdutyApiV1StatuspagesReadStatusPageIncidentPostmortemResponse404 | OpsdutyApiV1StatuspagesReadStatusPageIncidentPostmortemResponse422]
    """

    kwargs = _get_kwargs(
        incident_id=incident_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    incident_id: int,
    *,
    client: AuthenticatedClient,
) -> IncidentPostmortemSchema | OpsdutyApiV1StatuspagesReadStatusPageIncidentPostmortemResponse401 | OpsdutyApiV1StatuspagesReadStatusPageIncidentPostmortemResponse404 | OpsdutyApiV1StatuspagesReadStatusPageIncidentPostmortemResponse422 | None:
    """Read a status page incident's postmortem

     Read the postmortem written for an incident, published or not.

    Raises a validation error when the incident has no postmortem yet.

    Args:
        incident_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IncidentPostmortemSchema | OpsdutyApiV1StatuspagesReadStatusPageIncidentPostmortemResponse401 | OpsdutyApiV1StatuspagesReadStatusPageIncidentPostmortemResponse404 | OpsdutyApiV1StatuspagesReadStatusPageIncidentPostmortemResponse422
    """

    return (
        await asyncio_detailed(
            incident_id=incident_id,
            client=client,
        )
    ).parsed
