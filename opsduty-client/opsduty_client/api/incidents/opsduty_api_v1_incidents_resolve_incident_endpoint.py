from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.incident_group_detail_schema import IncidentGroupDetailSchema
from ...models.opsduty_api_v1_incidents_resolve_incident_endpoint_response_401 import OpsdutyApiV1IncidentsResolveIncidentEndpointResponse401
from ...models.opsduty_api_v1_incidents_resolve_incident_endpoint_response_404 import OpsdutyApiV1IncidentsResolveIncidentEndpointResponse404
from ...models.opsduty_api_v1_incidents_resolve_incident_endpoint_response_422 import OpsdutyApiV1IncidentsResolveIncidentEndpointResponse422
from ...models.resolve_incident_input_schema import ResolveIncidentInputSchema
from ...types import UNSET, Response, Unset


def _get_kwargs(
    incident_group_id: int,
    *,
    body: None | ResolveIncidentInputSchema | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/incidents/{incident_group_id}/resolve/".format(
            incident_group_id=quote(str(incident_group_id), safe=""),
        ),
    }

    if isinstance(body, ResolveIncidentInputSchema):
        _kwargs["json"] = body.to_dict()
    else:
        _kwargs["json"] = body

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> IncidentGroupDetailSchema | OpsdutyApiV1IncidentsResolveIncidentEndpointResponse401 | OpsdutyApiV1IncidentsResolveIncidentEndpointResponse404 | OpsdutyApiV1IncidentsResolveIncidentEndpointResponse422 | None:
    if response.status_code == 200:
        response_200 = IncidentGroupDetailSchema.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = OpsdutyApiV1IncidentsResolveIncidentEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = OpsdutyApiV1IncidentsResolveIncidentEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = OpsdutyApiV1IncidentsResolveIncidentEndpointResponse422.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[IncidentGroupDetailSchema | OpsdutyApiV1IncidentsResolveIncidentEndpointResponse401 | OpsdutyApiV1IncidentsResolveIncidentEndpointResponse404 | OpsdutyApiV1IncidentsResolveIncidentEndpointResponse422]:
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
    body: None | ResolveIncidentInputSchema | Unset = UNSET,
) -> Response[IncidentGroupDetailSchema | OpsdutyApiV1IncidentsResolveIncidentEndpointResponse401 | OpsdutyApiV1IncidentsResolveIncidentEndpointResponse404 | OpsdutyApiV1IncidentsResolveIncidentEndpointResponse422]:
    """Resolve an incident

     Close the incident. Pass an optional note to record why it was resolved on
    the incident timeline.

    Args:
        incident_group_id (int):
        body (None | ResolveIncidentInputSchema | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IncidentGroupDetailSchema | OpsdutyApiV1IncidentsResolveIncidentEndpointResponse401 | OpsdutyApiV1IncidentsResolveIncidentEndpointResponse404 | OpsdutyApiV1IncidentsResolveIncidentEndpointResponse422]
    """

    kwargs = _get_kwargs(
        incident_group_id=incident_group_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    incident_group_id: int,
    *,
    client: AuthenticatedClient,
    body: None | ResolveIncidentInputSchema | Unset = UNSET,
) -> IncidentGroupDetailSchema | OpsdutyApiV1IncidentsResolveIncidentEndpointResponse401 | OpsdutyApiV1IncidentsResolveIncidentEndpointResponse404 | OpsdutyApiV1IncidentsResolveIncidentEndpointResponse422 | None:
    """Resolve an incident

     Close the incident. Pass an optional note to record why it was resolved on
    the incident timeline.

    Args:
        incident_group_id (int):
        body (None | ResolveIncidentInputSchema | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IncidentGroupDetailSchema | OpsdutyApiV1IncidentsResolveIncidentEndpointResponse401 | OpsdutyApiV1IncidentsResolveIncidentEndpointResponse404 | OpsdutyApiV1IncidentsResolveIncidentEndpointResponse422
    """

    return sync_detailed(
        incident_group_id=incident_group_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    incident_group_id: int,
    *,
    client: AuthenticatedClient,
    body: None | ResolveIncidentInputSchema | Unset = UNSET,
) -> Response[IncidentGroupDetailSchema | OpsdutyApiV1IncidentsResolveIncidentEndpointResponse401 | OpsdutyApiV1IncidentsResolveIncidentEndpointResponse404 | OpsdutyApiV1IncidentsResolveIncidentEndpointResponse422]:
    """Resolve an incident

     Close the incident. Pass an optional note to record why it was resolved on
    the incident timeline.

    Args:
        incident_group_id (int):
        body (None | ResolveIncidentInputSchema | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IncidentGroupDetailSchema | OpsdutyApiV1IncidentsResolveIncidentEndpointResponse401 | OpsdutyApiV1IncidentsResolveIncidentEndpointResponse404 | OpsdutyApiV1IncidentsResolveIncidentEndpointResponse422]
    """

    kwargs = _get_kwargs(
        incident_group_id=incident_group_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    incident_group_id: int,
    *,
    client: AuthenticatedClient,
    body: None | ResolveIncidentInputSchema | Unset = UNSET,
) -> IncidentGroupDetailSchema | OpsdutyApiV1IncidentsResolveIncidentEndpointResponse401 | OpsdutyApiV1IncidentsResolveIncidentEndpointResponse404 | OpsdutyApiV1IncidentsResolveIncidentEndpointResponse422 | None:
    """Resolve an incident

     Close the incident. Pass an optional note to record why it was resolved on
    the incident timeline.

    Args:
        incident_group_id (int):
        body (None | ResolveIncidentInputSchema | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IncidentGroupDetailSchema | OpsdutyApiV1IncidentsResolveIncidentEndpointResponse401 | OpsdutyApiV1IncidentsResolveIncidentEndpointResponse404 | OpsdutyApiV1IncidentsResolveIncidentEndpointResponse422
    """

    return (
        await asyncio_detailed(
            incident_group_id=incident_group_id,
            client=client,
            body=body,
        )
    ).parsed
