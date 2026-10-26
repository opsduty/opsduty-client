from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.declare_incident_schema import DeclareIncidentSchema
from ...models.incident_schema import IncidentSchema
from ...models.opsduty_api_v1_statuspages_declare_status_page_incident_response_401 import OpsdutyApiV1StatuspagesDeclareStatusPageIncidentResponse401
from ...models.opsduty_api_v1_statuspages_declare_status_page_incident_response_404 import OpsdutyApiV1StatuspagesDeclareStatusPageIncidentResponse404
from ...models.opsduty_api_v1_statuspages_declare_status_page_incident_response_422 import OpsdutyApiV1StatuspagesDeclareStatusPageIncidentResponse422
from ...types import Response


def _get_kwargs(
    status_page_id: int,
    *,
    body: DeclareIncidentSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/statuspages/{status_page_id}/incidents/".format(
            status_page_id=quote(str(status_page_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> IncidentSchema | OpsdutyApiV1StatuspagesDeclareStatusPageIncidentResponse401 | OpsdutyApiV1StatuspagesDeclareStatusPageIncidentResponse404 | OpsdutyApiV1StatuspagesDeclareStatusPageIncidentResponse422 | None:
    if response.status_code == 200:
        response_200 = IncidentSchema.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = OpsdutyApiV1StatuspagesDeclareStatusPageIncidentResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = OpsdutyApiV1StatuspagesDeclareStatusPageIncidentResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = OpsdutyApiV1StatuspagesDeclareStatusPageIncidentResponse422.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[IncidentSchema | OpsdutyApiV1StatuspagesDeclareStatusPageIncidentResponse401 | OpsdutyApiV1StatuspagesDeclareStatusPageIncidentResponse404 | OpsdutyApiV1StatuspagesDeclareStatusPageIncidentResponse422]:
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
    body: DeclareIncidentSchema,
) -> Response[IncidentSchema | OpsdutyApiV1StatuspagesDeclareStatusPageIncidentResponse401 | OpsdutyApiV1StatuspagesDeclareStatusPageIncidentResponse404 | OpsdutyApiV1StatuspagesDeclareStatusPageIncidentResponse422]:
    """Declare a status page incident

     Publish an incident to a status page. It is visible to customers as soon
    as this returns, so send the wording you want them to read.

    Pass `incident_group_id` to tie it to the operational incident your team is
    already working on. The two then stay linked in OpsDuty, and the incident's
    timeline records that customers were told.

    Add `derive_affected_components` to have the affected components worked out
    from that incident's service, the same way the web app does, instead of
    looking them up and listing them yourself.

    Add `sync_component_status` to have those components report the impact you
    set while this is open, and go back to operational when you resolve it.

    Pass `published: false` to save a draft instead. Customers see nothing of
    it, and its components are left alone, until you publish it.

    Args:
        status_page_id (int):
        body (DeclareIncidentSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IncidentSchema | OpsdutyApiV1StatuspagesDeclareStatusPageIncidentResponse401 | OpsdutyApiV1StatuspagesDeclareStatusPageIncidentResponse404 | OpsdutyApiV1StatuspagesDeclareStatusPageIncidentResponse422]
    """

    kwargs = _get_kwargs(
        status_page_id=status_page_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    status_page_id: int,
    *,
    client: AuthenticatedClient,
    body: DeclareIncidentSchema,
) -> IncidentSchema | OpsdutyApiV1StatuspagesDeclareStatusPageIncidentResponse401 | OpsdutyApiV1StatuspagesDeclareStatusPageIncidentResponse404 | OpsdutyApiV1StatuspagesDeclareStatusPageIncidentResponse422 | None:
    """Declare a status page incident

     Publish an incident to a status page. It is visible to customers as soon
    as this returns, so send the wording you want them to read.

    Pass `incident_group_id` to tie it to the operational incident your team is
    already working on. The two then stay linked in OpsDuty, and the incident's
    timeline records that customers were told.

    Add `derive_affected_components` to have the affected components worked out
    from that incident's service, the same way the web app does, instead of
    looking them up and listing them yourself.

    Add `sync_component_status` to have those components report the impact you
    set while this is open, and go back to operational when you resolve it.

    Pass `published: false` to save a draft instead. Customers see nothing of
    it, and its components are left alone, until you publish it.

    Args:
        status_page_id (int):
        body (DeclareIncidentSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IncidentSchema | OpsdutyApiV1StatuspagesDeclareStatusPageIncidentResponse401 | OpsdutyApiV1StatuspagesDeclareStatusPageIncidentResponse404 | OpsdutyApiV1StatuspagesDeclareStatusPageIncidentResponse422
    """

    return sync_detailed(
        status_page_id=status_page_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    status_page_id: int,
    *,
    client: AuthenticatedClient,
    body: DeclareIncidentSchema,
) -> Response[IncidentSchema | OpsdutyApiV1StatuspagesDeclareStatusPageIncidentResponse401 | OpsdutyApiV1StatuspagesDeclareStatusPageIncidentResponse404 | OpsdutyApiV1StatuspagesDeclareStatusPageIncidentResponse422]:
    """Declare a status page incident

     Publish an incident to a status page. It is visible to customers as soon
    as this returns, so send the wording you want them to read.

    Pass `incident_group_id` to tie it to the operational incident your team is
    already working on. The two then stay linked in OpsDuty, and the incident's
    timeline records that customers were told.

    Add `derive_affected_components` to have the affected components worked out
    from that incident's service, the same way the web app does, instead of
    looking them up and listing them yourself.

    Add `sync_component_status` to have those components report the impact you
    set while this is open, and go back to operational when you resolve it.

    Pass `published: false` to save a draft instead. Customers see nothing of
    it, and its components are left alone, until you publish it.

    Args:
        status_page_id (int):
        body (DeclareIncidentSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IncidentSchema | OpsdutyApiV1StatuspagesDeclareStatusPageIncidentResponse401 | OpsdutyApiV1StatuspagesDeclareStatusPageIncidentResponse404 | OpsdutyApiV1StatuspagesDeclareStatusPageIncidentResponse422]
    """

    kwargs = _get_kwargs(
        status_page_id=status_page_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    status_page_id: int,
    *,
    client: AuthenticatedClient,
    body: DeclareIncidentSchema,
) -> IncidentSchema | OpsdutyApiV1StatuspagesDeclareStatusPageIncidentResponse401 | OpsdutyApiV1StatuspagesDeclareStatusPageIncidentResponse404 | OpsdutyApiV1StatuspagesDeclareStatusPageIncidentResponse422 | None:
    """Declare a status page incident

     Publish an incident to a status page. It is visible to customers as soon
    as this returns, so send the wording you want them to read.

    Pass `incident_group_id` to tie it to the operational incident your team is
    already working on. The two then stay linked in OpsDuty, and the incident's
    timeline records that customers were told.

    Add `derive_affected_components` to have the affected components worked out
    from that incident's service, the same way the web app does, instead of
    looking them up and listing them yourself.

    Add `sync_component_status` to have those components report the impact you
    set while this is open, and go back to operational when you resolve it.

    Pass `published: false` to save a draft instead. Customers see nothing of
    it, and its components are left alone, until you publish it.

    Args:
        status_page_id (int):
        body (DeclareIncidentSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IncidentSchema | OpsdutyApiV1StatuspagesDeclareStatusPageIncidentResponse401 | OpsdutyApiV1StatuspagesDeclareStatusPageIncidentResponse404 | OpsdutyApiV1StatuspagesDeclareStatusPageIncidentResponse422
    """

    return (
        await asyncio_detailed(
            status_page_id=status_page_id,
            client=client,
            body=body,
        )
    ).parsed
