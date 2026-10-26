from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.incident_postmortem_schema import IncidentPostmortemSchema
from ...models.opsduty_api_v1_statuspages_write_status_page_incident_postmortem_response_401 import OpsdutyApiV1StatuspagesWriteStatusPageIncidentPostmortemResponse401
from ...models.opsduty_api_v1_statuspages_write_status_page_incident_postmortem_response_404 import OpsdutyApiV1StatuspagesWriteStatusPageIncidentPostmortemResponse404
from ...models.opsduty_api_v1_statuspages_write_status_page_incident_postmortem_response_422 import OpsdutyApiV1StatuspagesWriteStatusPageIncidentPostmortemResponse422
from ...models.set_incident_postmortem_schema import SetIncidentPostmortemSchema
from ...types import Response


def _get_kwargs(
    incident_id: int,
    *,
    body: SetIncidentPostmortemSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/api/v1/statuspages/incidents/{incident_id}/postmortem/".format(
            incident_id=quote(str(incident_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> IncidentPostmortemSchema | OpsdutyApiV1StatuspagesWriteStatusPageIncidentPostmortemResponse401 | OpsdutyApiV1StatuspagesWriteStatusPageIncidentPostmortemResponse404 | OpsdutyApiV1StatuspagesWriteStatusPageIncidentPostmortemResponse422 | None:
    if response.status_code == 200:
        response_200 = IncidentPostmortemSchema.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = OpsdutyApiV1StatuspagesWriteStatusPageIncidentPostmortemResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = OpsdutyApiV1StatuspagesWriteStatusPageIncidentPostmortemResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = OpsdutyApiV1StatuspagesWriteStatusPageIncidentPostmortemResponse422.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[IncidentPostmortemSchema | OpsdutyApiV1StatuspagesWriteStatusPageIncidentPostmortemResponse401 | OpsdutyApiV1StatuspagesWriteStatusPageIncidentPostmortemResponse404 | OpsdutyApiV1StatuspagesWriteStatusPageIncidentPostmortemResponse422]:
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
    body: SetIncidentPostmortemSchema,
) -> Response[IncidentPostmortemSchema | OpsdutyApiV1StatuspagesWriteStatusPageIncidentPostmortemResponse401 | OpsdutyApiV1StatuspagesWriteStatusPageIncidentPostmortemResponse404 | OpsdutyApiV1StatuspagesWriteStatusPageIncidentPostmortemResponse422]:
    """Write a status page incident's postmortem

     Write the postmortem for an incident, creating it or replacing what is
    there. Publishing it puts it on the public incident page and in the feed,
    and it lands on the operational incident's timeline when this incident was
    declared from one.

    Args:
        incident_id (int):
        body (SetIncidentPostmortemSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IncidentPostmortemSchema | OpsdutyApiV1StatuspagesWriteStatusPageIncidentPostmortemResponse401 | OpsdutyApiV1StatuspagesWriteStatusPageIncidentPostmortemResponse404 | OpsdutyApiV1StatuspagesWriteStatusPageIncidentPostmortemResponse422]
    """

    kwargs = _get_kwargs(
        incident_id=incident_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    incident_id: int,
    *,
    client: AuthenticatedClient,
    body: SetIncidentPostmortemSchema,
) -> IncidentPostmortemSchema | OpsdutyApiV1StatuspagesWriteStatusPageIncidentPostmortemResponse401 | OpsdutyApiV1StatuspagesWriteStatusPageIncidentPostmortemResponse404 | OpsdutyApiV1StatuspagesWriteStatusPageIncidentPostmortemResponse422 | None:
    """Write a status page incident's postmortem

     Write the postmortem for an incident, creating it or replacing what is
    there. Publishing it puts it on the public incident page and in the feed,
    and it lands on the operational incident's timeline when this incident was
    declared from one.

    Args:
        incident_id (int):
        body (SetIncidentPostmortemSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IncidentPostmortemSchema | OpsdutyApiV1StatuspagesWriteStatusPageIncidentPostmortemResponse401 | OpsdutyApiV1StatuspagesWriteStatusPageIncidentPostmortemResponse404 | OpsdutyApiV1StatuspagesWriteStatusPageIncidentPostmortemResponse422
    """

    return sync_detailed(
        incident_id=incident_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    incident_id: int,
    *,
    client: AuthenticatedClient,
    body: SetIncidentPostmortemSchema,
) -> Response[IncidentPostmortemSchema | OpsdutyApiV1StatuspagesWriteStatusPageIncidentPostmortemResponse401 | OpsdutyApiV1StatuspagesWriteStatusPageIncidentPostmortemResponse404 | OpsdutyApiV1StatuspagesWriteStatusPageIncidentPostmortemResponse422]:
    """Write a status page incident's postmortem

     Write the postmortem for an incident, creating it or replacing what is
    there. Publishing it puts it on the public incident page and in the feed,
    and it lands on the operational incident's timeline when this incident was
    declared from one.

    Args:
        incident_id (int):
        body (SetIncidentPostmortemSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IncidentPostmortemSchema | OpsdutyApiV1StatuspagesWriteStatusPageIncidentPostmortemResponse401 | OpsdutyApiV1StatuspagesWriteStatusPageIncidentPostmortemResponse404 | OpsdutyApiV1StatuspagesWriteStatusPageIncidentPostmortemResponse422]
    """

    kwargs = _get_kwargs(
        incident_id=incident_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    incident_id: int,
    *,
    client: AuthenticatedClient,
    body: SetIncidentPostmortemSchema,
) -> IncidentPostmortemSchema | OpsdutyApiV1StatuspagesWriteStatusPageIncidentPostmortemResponse401 | OpsdutyApiV1StatuspagesWriteStatusPageIncidentPostmortemResponse404 | OpsdutyApiV1StatuspagesWriteStatusPageIncidentPostmortemResponse422 | None:
    """Write a status page incident's postmortem

     Write the postmortem for an incident, creating it or replacing what is
    there. Publishing it puts it on the public incident page and in the feed,
    and it lands on the operational incident's timeline when this incident was
    declared from one.

    Args:
        incident_id (int):
        body (SetIncidentPostmortemSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IncidentPostmortemSchema | OpsdutyApiV1StatuspagesWriteStatusPageIncidentPostmortemResponse401 | OpsdutyApiV1StatuspagesWriteStatusPageIncidentPostmortemResponse404 | OpsdutyApiV1StatuspagesWriteStatusPageIncidentPostmortemResponse422
    """

    return (
        await asyncio_detailed(
            incident_id=incident_id,
            client=client,
            body=body,
        )
    ).parsed
