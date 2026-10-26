from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.incident_group_detail_schema import IncidentGroupDetailSchema
from ...models.opsduty_api_v1_incidents_un_resolve_incident_endpoint_response_401 import OpsdutyApiV1IncidentsUnResolveIncidentEndpointResponse401
from ...models.opsduty_api_v1_incidents_un_resolve_incident_endpoint_response_404 import OpsdutyApiV1IncidentsUnResolveIncidentEndpointResponse404
from ...models.opsduty_api_v1_incidents_un_resolve_incident_endpoint_response_422 import OpsdutyApiV1IncidentsUnResolveIncidentEndpointResponse422
from ...types import Response


def _get_kwargs(
    incident_group_id: int,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/incidents/{incident_group_id}/unresolve/".format(
            incident_group_id=quote(str(incident_group_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> IncidentGroupDetailSchema | OpsdutyApiV1IncidentsUnResolveIncidentEndpointResponse401 | OpsdutyApiV1IncidentsUnResolveIncidentEndpointResponse404 | OpsdutyApiV1IncidentsUnResolveIncidentEndpointResponse422 | None:
    if response.status_code == 200:
        response_200 = IncidentGroupDetailSchema.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = OpsdutyApiV1IncidentsUnResolveIncidentEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = OpsdutyApiV1IncidentsUnResolveIncidentEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = OpsdutyApiV1IncidentsUnResolveIncidentEndpointResponse422.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[IncidentGroupDetailSchema | OpsdutyApiV1IncidentsUnResolveIncidentEndpointResponse401 | OpsdutyApiV1IncidentsUnResolveIncidentEndpointResponse404 | OpsdutyApiV1IncidentsUnResolveIncidentEndpointResponse422]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    incident_group_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[IncidentGroupDetailSchema | OpsdutyApiV1IncidentsUnResolveIncidentEndpointResponse401 | OpsdutyApiV1IncidentsUnResolveIncidentEndpointResponse404 | OpsdutyApiV1IncidentsUnResolveIncidentEndpointResponse422]:
    """Re-open a resolved incident

     Re-open an incident that was resolved too early. Rejected if the incident is
    not resolved.

    Args:
        incident_group_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IncidentGroupDetailSchema | OpsdutyApiV1IncidentsUnResolveIncidentEndpointResponse401 | OpsdutyApiV1IncidentsUnResolveIncidentEndpointResponse404 | OpsdutyApiV1IncidentsUnResolveIncidentEndpointResponse422]
    """

    kwargs = _get_kwargs(
        incident_group_id=incident_group_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    incident_group_id: int,
    *,
    client: AuthenticatedClient,
) -> IncidentGroupDetailSchema | OpsdutyApiV1IncidentsUnResolveIncidentEndpointResponse401 | OpsdutyApiV1IncidentsUnResolveIncidentEndpointResponse404 | OpsdutyApiV1IncidentsUnResolveIncidentEndpointResponse422 | None:
    """Re-open a resolved incident

     Re-open an incident that was resolved too early. Rejected if the incident is
    not resolved.

    Args:
        incident_group_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IncidentGroupDetailSchema | OpsdutyApiV1IncidentsUnResolveIncidentEndpointResponse401 | OpsdutyApiV1IncidentsUnResolveIncidentEndpointResponse404 | OpsdutyApiV1IncidentsUnResolveIncidentEndpointResponse422
    """

    return sync_detailed(
        incident_group_id=incident_group_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    incident_group_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[IncidentGroupDetailSchema | OpsdutyApiV1IncidentsUnResolveIncidentEndpointResponse401 | OpsdutyApiV1IncidentsUnResolveIncidentEndpointResponse404 | OpsdutyApiV1IncidentsUnResolveIncidentEndpointResponse422]:
    """Re-open a resolved incident

     Re-open an incident that was resolved too early. Rejected if the incident is
    not resolved.

    Args:
        incident_group_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IncidentGroupDetailSchema | OpsdutyApiV1IncidentsUnResolveIncidentEndpointResponse401 | OpsdutyApiV1IncidentsUnResolveIncidentEndpointResponse404 | OpsdutyApiV1IncidentsUnResolveIncidentEndpointResponse422]
    """

    kwargs = _get_kwargs(
        incident_group_id=incident_group_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    incident_group_id: int,
    *,
    client: AuthenticatedClient,
) -> IncidentGroupDetailSchema | OpsdutyApiV1IncidentsUnResolveIncidentEndpointResponse401 | OpsdutyApiV1IncidentsUnResolveIncidentEndpointResponse404 | OpsdutyApiV1IncidentsUnResolveIncidentEndpointResponse422 | None:
    """Re-open a resolved incident

     Re-open an incident that was resolved too early. Rejected if the incident is
    not resolved.

    Args:
        incident_group_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IncidentGroupDetailSchema | OpsdutyApiV1IncidentsUnResolveIncidentEndpointResponse401 | OpsdutyApiV1IncidentsUnResolveIncidentEndpointResponse404 | OpsdutyApiV1IncidentsUnResolveIncidentEndpointResponse422
    """

    return (
        await asyncio_detailed(
            incident_group_id=incident_group_id,
            client=client,
        )
    ).parsed
