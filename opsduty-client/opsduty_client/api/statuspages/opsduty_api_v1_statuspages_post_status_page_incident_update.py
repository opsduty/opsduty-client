from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.incident_update_schema import IncidentUpdateSchema
from ...models.opsduty_api_v1_statuspages_post_status_page_incident_update_response_401 import OpsdutyApiV1StatuspagesPostStatusPageIncidentUpdateResponse401
from ...models.opsduty_api_v1_statuspages_post_status_page_incident_update_response_404 import OpsdutyApiV1StatuspagesPostStatusPageIncidentUpdateResponse404
from ...models.opsduty_api_v1_statuspages_post_status_page_incident_update_response_422 import OpsdutyApiV1StatuspagesPostStatusPageIncidentUpdateResponse422
from ...models.post_incident_update_schema import PostIncidentUpdateSchema
from ...types import Response


def _get_kwargs(
    incident_id: int,
    *,
    body: PostIncidentUpdateSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/statuspages/incidents/{incident_id}/updates/".format(
            incident_id=quote(str(incident_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> IncidentUpdateSchema | OpsdutyApiV1StatuspagesPostStatusPageIncidentUpdateResponse401 | OpsdutyApiV1StatuspagesPostStatusPageIncidentUpdateResponse404 | OpsdutyApiV1StatuspagesPostStatusPageIncidentUpdateResponse422 | None:
    if response.status_code == 200:
        response_200 = IncidentUpdateSchema.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = OpsdutyApiV1StatuspagesPostStatusPageIncidentUpdateResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = OpsdutyApiV1StatuspagesPostStatusPageIncidentUpdateResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = OpsdutyApiV1StatuspagesPostStatusPageIncidentUpdateResponse422.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[IncidentUpdateSchema | OpsdutyApiV1StatuspagesPostStatusPageIncidentUpdateResponse401 | OpsdutyApiV1StatuspagesPostStatusPageIncidentUpdateResponse404 | OpsdutyApiV1StatuspagesPostStatusPageIncidentUpdateResponse422]:
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
    body: PostIncidentUpdateSchema,
) -> Response[IncidentUpdateSchema | OpsdutyApiV1StatuspagesPostStatusPageIncidentUpdateResponse401 | OpsdutyApiV1StatuspagesPostStatusPageIncidentUpdateResponse404 | OpsdutyApiV1StatuspagesPostStatusPageIncidentUpdateResponse422]:
    """Post a status page incident update

     Post an update to a published incident, optionally moving it to a new
    status. The update appears on the public timeline right away, unless
    `display_at` schedules it for later.

    Args:
        incident_id (int):
        body (PostIncidentUpdateSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IncidentUpdateSchema | OpsdutyApiV1StatuspagesPostStatusPageIncidentUpdateResponse401 | OpsdutyApiV1StatuspagesPostStatusPageIncidentUpdateResponse404 | OpsdutyApiV1StatuspagesPostStatusPageIncidentUpdateResponse422]
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
    body: PostIncidentUpdateSchema,
) -> IncidentUpdateSchema | OpsdutyApiV1StatuspagesPostStatusPageIncidentUpdateResponse401 | OpsdutyApiV1StatuspagesPostStatusPageIncidentUpdateResponse404 | OpsdutyApiV1StatuspagesPostStatusPageIncidentUpdateResponse422 | None:
    """Post a status page incident update

     Post an update to a published incident, optionally moving it to a new
    status. The update appears on the public timeline right away, unless
    `display_at` schedules it for later.

    Args:
        incident_id (int):
        body (PostIncidentUpdateSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IncidentUpdateSchema | OpsdutyApiV1StatuspagesPostStatusPageIncidentUpdateResponse401 | OpsdutyApiV1StatuspagesPostStatusPageIncidentUpdateResponse404 | OpsdutyApiV1StatuspagesPostStatusPageIncidentUpdateResponse422
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
    body: PostIncidentUpdateSchema,
) -> Response[IncidentUpdateSchema | OpsdutyApiV1StatuspagesPostStatusPageIncidentUpdateResponse401 | OpsdutyApiV1StatuspagesPostStatusPageIncidentUpdateResponse404 | OpsdutyApiV1StatuspagesPostStatusPageIncidentUpdateResponse422]:
    """Post a status page incident update

     Post an update to a published incident, optionally moving it to a new
    status. The update appears on the public timeline right away, unless
    `display_at` schedules it for later.

    Args:
        incident_id (int):
        body (PostIncidentUpdateSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IncidentUpdateSchema | OpsdutyApiV1StatuspagesPostStatusPageIncidentUpdateResponse401 | OpsdutyApiV1StatuspagesPostStatusPageIncidentUpdateResponse404 | OpsdutyApiV1StatuspagesPostStatusPageIncidentUpdateResponse422]
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
    body: PostIncidentUpdateSchema,
) -> IncidentUpdateSchema | OpsdutyApiV1StatuspagesPostStatusPageIncidentUpdateResponse401 | OpsdutyApiV1StatuspagesPostStatusPageIncidentUpdateResponse404 | OpsdutyApiV1StatuspagesPostStatusPageIncidentUpdateResponse422 | None:
    """Post a status page incident update

     Post an update to a published incident, optionally moving it to a new
    status. The update appears on the public timeline right away, unless
    `display_at` schedules it for later.

    Args:
        incident_id (int):
        body (PostIncidentUpdateSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IncidentUpdateSchema | OpsdutyApiV1StatuspagesPostStatusPageIncidentUpdateResponse401 | OpsdutyApiV1StatuspagesPostStatusPageIncidentUpdateResponse404 | OpsdutyApiV1StatuspagesPostStatusPageIncidentUpdateResponse422
    """

    return (
        await asyncio_detailed(
            incident_id=incident_id,
            client=client,
            body=body,
        )
    ).parsed
