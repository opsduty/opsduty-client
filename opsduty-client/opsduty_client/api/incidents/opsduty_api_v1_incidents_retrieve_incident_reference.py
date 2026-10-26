from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.incident_reference_schema import IncidentReferenceSchema
from ...models.opsduty_api_v1_incidents_retrieve_incident_reference_response_401 import OpsdutyApiV1IncidentsRetrieveIncidentReferenceResponse401
from ...models.opsduty_api_v1_incidents_retrieve_incident_reference_response_404 import OpsdutyApiV1IncidentsRetrieveIncidentReferenceResponse404
from ...models.opsduty_api_v1_incidents_retrieve_incident_reference_response_422 import OpsdutyApiV1IncidentsRetrieveIncidentReferenceResponse422
from ...types import Response


def _get_kwargs(
    incident_reference_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/incidents/incident-reference/{incident_reference_id}/".format(
            incident_reference_id=quote(str(incident_reference_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> IncidentReferenceSchema | OpsdutyApiV1IncidentsRetrieveIncidentReferenceResponse401 | OpsdutyApiV1IncidentsRetrieveIncidentReferenceResponse404 | OpsdutyApiV1IncidentsRetrieveIncidentReferenceResponse422 | None:
    if response.status_code == 200:
        response_200 = IncidentReferenceSchema.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = OpsdutyApiV1IncidentsRetrieveIncidentReferenceResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = OpsdutyApiV1IncidentsRetrieveIncidentReferenceResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = OpsdutyApiV1IncidentsRetrieveIncidentReferenceResponse422.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[IncidentReferenceSchema | OpsdutyApiV1IncidentsRetrieveIncidentReferenceResponse401 | OpsdutyApiV1IncidentsRetrieveIncidentReferenceResponse404 | OpsdutyApiV1IncidentsRetrieveIncidentReferenceResponse422]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    incident_reference_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[IncidentReferenceSchema | OpsdutyApiV1IncidentsRetrieveIncidentReferenceResponse401 | OpsdutyApiV1IncidentsRetrieveIncidentReferenceResponse404 | OpsdutyApiV1IncidentsRetrieveIncidentReferenceResponse422]:
    """Look up an incident by reference

     Find the incident an event you sent ended up in.

    Submitting an event returns an incident reference. Events are processed in
    the background, so the reference resolves to an incident once that work
    finishes rather than the moment you send it.

    Args:
        incident_reference_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IncidentReferenceSchema | OpsdutyApiV1IncidentsRetrieveIncidentReferenceResponse401 | OpsdutyApiV1IncidentsRetrieveIncidentReferenceResponse404 | OpsdutyApiV1IncidentsRetrieveIncidentReferenceResponse422]
    """

    kwargs = _get_kwargs(
        incident_reference_id=incident_reference_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    incident_reference_id: str,
    *,
    client: AuthenticatedClient,
) -> IncidentReferenceSchema | OpsdutyApiV1IncidentsRetrieveIncidentReferenceResponse401 | OpsdutyApiV1IncidentsRetrieveIncidentReferenceResponse404 | OpsdutyApiV1IncidentsRetrieveIncidentReferenceResponse422 | None:
    """Look up an incident by reference

     Find the incident an event you sent ended up in.

    Submitting an event returns an incident reference. Events are processed in
    the background, so the reference resolves to an incident once that work
    finishes rather than the moment you send it.

    Args:
        incident_reference_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IncidentReferenceSchema | OpsdutyApiV1IncidentsRetrieveIncidentReferenceResponse401 | OpsdutyApiV1IncidentsRetrieveIncidentReferenceResponse404 | OpsdutyApiV1IncidentsRetrieveIncidentReferenceResponse422
    """

    return sync_detailed(
        incident_reference_id=incident_reference_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    incident_reference_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[IncidentReferenceSchema | OpsdutyApiV1IncidentsRetrieveIncidentReferenceResponse401 | OpsdutyApiV1IncidentsRetrieveIncidentReferenceResponse404 | OpsdutyApiV1IncidentsRetrieveIncidentReferenceResponse422]:
    """Look up an incident by reference

     Find the incident an event you sent ended up in.

    Submitting an event returns an incident reference. Events are processed in
    the background, so the reference resolves to an incident once that work
    finishes rather than the moment you send it.

    Args:
        incident_reference_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IncidentReferenceSchema | OpsdutyApiV1IncidentsRetrieveIncidentReferenceResponse401 | OpsdutyApiV1IncidentsRetrieveIncidentReferenceResponse404 | OpsdutyApiV1IncidentsRetrieveIncidentReferenceResponse422]
    """

    kwargs = _get_kwargs(
        incident_reference_id=incident_reference_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    incident_reference_id: str,
    *,
    client: AuthenticatedClient,
) -> IncidentReferenceSchema | OpsdutyApiV1IncidentsRetrieveIncidentReferenceResponse401 | OpsdutyApiV1IncidentsRetrieveIncidentReferenceResponse404 | OpsdutyApiV1IncidentsRetrieveIncidentReferenceResponse422 | None:
    """Look up an incident by reference

     Find the incident an event you sent ended up in.

    Submitting an event returns an incident reference. Events are processed in
    the background, so the reference resolves to an incident once that work
    finishes rather than the moment you send it.

    Args:
        incident_reference_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IncidentReferenceSchema | OpsdutyApiV1IncidentsRetrieveIncidentReferenceResponse401 | OpsdutyApiV1IncidentsRetrieveIncidentReferenceResponse404 | OpsdutyApiV1IncidentsRetrieveIncidentReferenceResponse422
    """

    return (
        await asyncio_detailed(
            incident_reference_id=incident_reference_id,
            client=client,
        )
    ).parsed
