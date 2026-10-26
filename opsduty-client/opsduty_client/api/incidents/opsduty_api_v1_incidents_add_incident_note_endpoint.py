from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.add_incident_note_input_schema import AddIncidentNoteInputSchema
from ...models.incident_group_detail_note_schema import IncidentGroupDetailNoteSchema
from ...models.opsduty_api_v1_incidents_add_incident_note_endpoint_response_401 import OpsdutyApiV1IncidentsAddIncidentNoteEndpointResponse401
from ...models.opsduty_api_v1_incidents_add_incident_note_endpoint_response_404 import OpsdutyApiV1IncidentsAddIncidentNoteEndpointResponse404
from ...models.opsduty_api_v1_incidents_add_incident_note_endpoint_response_422 import OpsdutyApiV1IncidentsAddIncidentNoteEndpointResponse422
from ...types import Response


def _get_kwargs(
    incident_group_id: int,
    *,
    body: AddIncidentNoteInputSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/incidents/{incident_group_id}/notes/".format(
            incident_group_id=quote(str(incident_group_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> IncidentGroupDetailNoteSchema | OpsdutyApiV1IncidentsAddIncidentNoteEndpointResponse401 | OpsdutyApiV1IncidentsAddIncidentNoteEndpointResponse404 | OpsdutyApiV1IncidentsAddIncidentNoteEndpointResponse422 | None:
    if response.status_code == 200:
        response_200 = IncidentGroupDetailNoteSchema.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = OpsdutyApiV1IncidentsAddIncidentNoteEndpointResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = OpsdutyApiV1IncidentsAddIncidentNoteEndpointResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = OpsdutyApiV1IncidentsAddIncidentNoteEndpointResponse422.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[IncidentGroupDetailNoteSchema | OpsdutyApiV1IncidentsAddIncidentNoteEndpointResponse401 | OpsdutyApiV1IncidentsAddIncidentNoteEndpointResponse404 | OpsdutyApiV1IncidentsAddIncidentNoteEndpointResponse422]:
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
    body: AddIncidentNoteInputSchema,
) -> Response[IncidentGroupDetailNoteSchema | OpsdutyApiV1IncidentsAddIncidentNoteEndpointResponse401 | OpsdutyApiV1IncidentsAddIncidentNoteEndpointResponse404 | OpsdutyApiV1IncidentsAddIncidentNoteEndpointResponse422]:
    """Add a note to an incident

     Record context on the incident timeline without changing its status, for
    example what an automation did or where the investigation got to. The note
    is attributed to the account the token belongs to.

    Args:
        incident_group_id (int):
        body (AddIncidentNoteInputSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IncidentGroupDetailNoteSchema | OpsdutyApiV1IncidentsAddIncidentNoteEndpointResponse401 | OpsdutyApiV1IncidentsAddIncidentNoteEndpointResponse404 | OpsdutyApiV1IncidentsAddIncidentNoteEndpointResponse422]
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
    body: AddIncidentNoteInputSchema,
) -> IncidentGroupDetailNoteSchema | OpsdutyApiV1IncidentsAddIncidentNoteEndpointResponse401 | OpsdutyApiV1IncidentsAddIncidentNoteEndpointResponse404 | OpsdutyApiV1IncidentsAddIncidentNoteEndpointResponse422 | None:
    """Add a note to an incident

     Record context on the incident timeline without changing its status, for
    example what an automation did or where the investigation got to. The note
    is attributed to the account the token belongs to.

    Args:
        incident_group_id (int):
        body (AddIncidentNoteInputSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IncidentGroupDetailNoteSchema | OpsdutyApiV1IncidentsAddIncidentNoteEndpointResponse401 | OpsdutyApiV1IncidentsAddIncidentNoteEndpointResponse404 | OpsdutyApiV1IncidentsAddIncidentNoteEndpointResponse422
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
    body: AddIncidentNoteInputSchema,
) -> Response[IncidentGroupDetailNoteSchema | OpsdutyApiV1IncidentsAddIncidentNoteEndpointResponse401 | OpsdutyApiV1IncidentsAddIncidentNoteEndpointResponse404 | OpsdutyApiV1IncidentsAddIncidentNoteEndpointResponse422]:
    """Add a note to an incident

     Record context on the incident timeline without changing its status, for
    example what an automation did or where the investigation got to. The note
    is attributed to the account the token belongs to.

    Args:
        incident_group_id (int):
        body (AddIncidentNoteInputSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IncidentGroupDetailNoteSchema | OpsdutyApiV1IncidentsAddIncidentNoteEndpointResponse401 | OpsdutyApiV1IncidentsAddIncidentNoteEndpointResponse404 | OpsdutyApiV1IncidentsAddIncidentNoteEndpointResponse422]
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
    body: AddIncidentNoteInputSchema,
) -> IncidentGroupDetailNoteSchema | OpsdutyApiV1IncidentsAddIncidentNoteEndpointResponse401 | OpsdutyApiV1IncidentsAddIncidentNoteEndpointResponse404 | OpsdutyApiV1IncidentsAddIncidentNoteEndpointResponse422 | None:
    """Add a note to an incident

     Record context on the incident timeline without changing its status, for
    example what an automation did or where the investigation got to. The note
    is attributed to the account the token belongs to.

    Args:
        incident_group_id (int):
        body (AddIncidentNoteInputSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IncidentGroupDetailNoteSchema | OpsdutyApiV1IncidentsAddIncidentNoteEndpointResponse401 | OpsdutyApiV1IncidentsAddIncidentNoteEndpointResponse404 | OpsdutyApiV1IncidentsAddIncidentNoteEndpointResponse422
    """

    return (
        await asyncio_detailed(
            incident_group_id=incident_group_id,
            client=client,
            body=body,
        )
    ).parsed
