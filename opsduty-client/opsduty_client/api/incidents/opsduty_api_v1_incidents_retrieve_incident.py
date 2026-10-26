from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.incident_group_detail_schema import IncidentGroupDetailSchema
from ...models.opsduty_api_v1_incidents_retrieve_incident_response_401 import OpsdutyApiV1IncidentsRetrieveIncidentResponse401
from ...models.opsduty_api_v1_incidents_retrieve_incident_response_404 import OpsdutyApiV1IncidentsRetrieveIncidentResponse404
from ...models.opsduty_api_v1_incidents_retrieve_incident_response_422 import OpsdutyApiV1IncidentsRetrieveIncidentResponse422
from ...types import Response


def _get_kwargs(
    incident_group_id: int,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/incidents/{incident_group_id}/".format(
            incident_group_id=quote(str(incident_group_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> IncidentGroupDetailSchema | OpsdutyApiV1IncidentsRetrieveIncidentResponse401 | OpsdutyApiV1IncidentsRetrieveIncidentResponse404 | OpsdutyApiV1IncidentsRetrieveIncidentResponse422 | None:
    if response.status_code == 200:
        response_200 = IncidentGroupDetailSchema.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = OpsdutyApiV1IncidentsRetrieveIncidentResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = OpsdutyApiV1IncidentsRetrieveIncidentResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = OpsdutyApiV1IncidentsRetrieveIncidentResponse422.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[IncidentGroupDetailSchema | OpsdutyApiV1IncidentsRetrieveIncidentResponse401 | OpsdutyApiV1IncidentsRetrieveIncidentResponse404 | OpsdutyApiV1IncidentsRetrieveIncidentResponse422]:
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
) -> Response[IncidentGroupDetailSchema | OpsdutyApiV1IncidentsRetrieveIncidentResponse401 | OpsdutyApiV1IncidentsRetrieveIncidentResponse404 | OpsdutyApiV1IncidentsRetrieveIncidentResponse422]:
    """Read an incident

     Read one incident, including its service and its notes.

    Args:
        incident_group_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IncidentGroupDetailSchema | OpsdutyApiV1IncidentsRetrieveIncidentResponse401 | OpsdutyApiV1IncidentsRetrieveIncidentResponse404 | OpsdutyApiV1IncidentsRetrieveIncidentResponse422]
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
) -> IncidentGroupDetailSchema | OpsdutyApiV1IncidentsRetrieveIncidentResponse401 | OpsdutyApiV1IncidentsRetrieveIncidentResponse404 | OpsdutyApiV1IncidentsRetrieveIncidentResponse422 | None:
    """Read an incident

     Read one incident, including its service and its notes.

    Args:
        incident_group_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IncidentGroupDetailSchema | OpsdutyApiV1IncidentsRetrieveIncidentResponse401 | OpsdutyApiV1IncidentsRetrieveIncidentResponse404 | OpsdutyApiV1IncidentsRetrieveIncidentResponse422
    """

    return sync_detailed(
        incident_group_id=incident_group_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    incident_group_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[IncidentGroupDetailSchema | OpsdutyApiV1IncidentsRetrieveIncidentResponse401 | OpsdutyApiV1IncidentsRetrieveIncidentResponse404 | OpsdutyApiV1IncidentsRetrieveIncidentResponse422]:
    """Read an incident

     Read one incident, including its service and its notes.

    Args:
        incident_group_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IncidentGroupDetailSchema | OpsdutyApiV1IncidentsRetrieveIncidentResponse401 | OpsdutyApiV1IncidentsRetrieveIncidentResponse404 | OpsdutyApiV1IncidentsRetrieveIncidentResponse422]
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
) -> IncidentGroupDetailSchema | OpsdutyApiV1IncidentsRetrieveIncidentResponse401 | OpsdutyApiV1IncidentsRetrieveIncidentResponse404 | OpsdutyApiV1IncidentsRetrieveIncidentResponse422 | None:
    """Read an incident

     Read one incident, including its service and its notes.

    Args:
        incident_group_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IncidentGroupDetailSchema | OpsdutyApiV1IncidentsRetrieveIncidentResponse401 | OpsdutyApiV1IncidentsRetrieveIncidentResponse404 | OpsdutyApiV1IncidentsRetrieveIncidentResponse422
    """

    return (
        await asyncio_detailed(
            incident_group_id=incident_group_id,
            client=client,
        )
    ).parsed
