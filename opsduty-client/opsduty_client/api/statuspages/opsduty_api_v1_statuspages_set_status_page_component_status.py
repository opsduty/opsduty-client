from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.component_schema import ComponentSchema
from ...models.opsduty_api_v1_statuspages_set_status_page_component_status_response_401 import OpsdutyApiV1StatuspagesSetStatusPageComponentStatusResponse401
from ...models.opsduty_api_v1_statuspages_set_status_page_component_status_response_404 import OpsdutyApiV1StatuspagesSetStatusPageComponentStatusResponse404
from ...models.opsduty_api_v1_statuspages_set_status_page_component_status_response_422 import OpsdutyApiV1StatuspagesSetStatusPageComponentStatusResponse422
from ...models.set_component_status_schema import SetComponentStatusSchema
from ...types import Response


def _get_kwargs(
    component_id: int,
    *,
    body: SetComponentStatusSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/statuspages/components/{component_id}/status/".format(
            component_id=quote(str(component_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ComponentSchema | OpsdutyApiV1StatuspagesSetStatusPageComponentStatusResponse401 | OpsdutyApiV1StatuspagesSetStatusPageComponentStatusResponse404 | OpsdutyApiV1StatuspagesSetStatusPageComponentStatusResponse422 | None:
    if response.status_code == 200:
        response_200 = ComponentSchema.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = OpsdutyApiV1StatuspagesSetStatusPageComponentStatusResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = OpsdutyApiV1StatuspagesSetStatusPageComponentStatusResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = OpsdutyApiV1StatuspagesSetStatusPageComponentStatusResponse422.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ComponentSchema | OpsdutyApiV1StatuspagesSetStatusPageComponentStatusResponse401 | OpsdutyApiV1StatuspagesSetStatusPageComponentStatusResponse404 | OpsdutyApiV1StatuspagesSetStatusPageComponentStatusResponse422]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    component_id: int,
    *,
    client: AuthenticatedClient,
    body: SetComponentStatusSchema,
) -> Response[ComponentSchema | OpsdutyApiV1StatuspagesSetStatusPageComponentStatusResponse401 | OpsdutyApiV1StatuspagesSetStatusPageComponentStatusResponse404 | OpsdutyApiV1StatuspagesSetStatusPageComponentStatusResponse422]:
    """Set a status page component's status

     Say what a component is doing right now, without declaring an incident.

    Customers see this immediately, on the component and in the headline the
    page rolls up from every component.

    An incident that was told to keep this component in step with its impact
    still wins while it is open, because that is what somebody asked it to do.
    Use this for a component nothing has declared an incident about.

    Args:
        component_id (int):
        body (SetComponentStatusSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ComponentSchema | OpsdutyApiV1StatuspagesSetStatusPageComponentStatusResponse401 | OpsdutyApiV1StatuspagesSetStatusPageComponentStatusResponse404 | OpsdutyApiV1StatuspagesSetStatusPageComponentStatusResponse422]
    """

    kwargs = _get_kwargs(
        component_id=component_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    component_id: int,
    *,
    client: AuthenticatedClient,
    body: SetComponentStatusSchema,
) -> ComponentSchema | OpsdutyApiV1StatuspagesSetStatusPageComponentStatusResponse401 | OpsdutyApiV1StatuspagesSetStatusPageComponentStatusResponse404 | OpsdutyApiV1StatuspagesSetStatusPageComponentStatusResponse422 | None:
    """Set a status page component's status

     Say what a component is doing right now, without declaring an incident.

    Customers see this immediately, on the component and in the headline the
    page rolls up from every component.

    An incident that was told to keep this component in step with its impact
    still wins while it is open, because that is what somebody asked it to do.
    Use this for a component nothing has declared an incident about.

    Args:
        component_id (int):
        body (SetComponentStatusSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ComponentSchema | OpsdutyApiV1StatuspagesSetStatusPageComponentStatusResponse401 | OpsdutyApiV1StatuspagesSetStatusPageComponentStatusResponse404 | OpsdutyApiV1StatuspagesSetStatusPageComponentStatusResponse422
    """

    return sync_detailed(
        component_id=component_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    component_id: int,
    *,
    client: AuthenticatedClient,
    body: SetComponentStatusSchema,
) -> Response[ComponentSchema | OpsdutyApiV1StatuspagesSetStatusPageComponentStatusResponse401 | OpsdutyApiV1StatuspagesSetStatusPageComponentStatusResponse404 | OpsdutyApiV1StatuspagesSetStatusPageComponentStatusResponse422]:
    """Set a status page component's status

     Say what a component is doing right now, without declaring an incident.

    Customers see this immediately, on the component and in the headline the
    page rolls up from every component.

    An incident that was told to keep this component in step with its impact
    still wins while it is open, because that is what somebody asked it to do.
    Use this for a component nothing has declared an incident about.

    Args:
        component_id (int):
        body (SetComponentStatusSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ComponentSchema | OpsdutyApiV1StatuspagesSetStatusPageComponentStatusResponse401 | OpsdutyApiV1StatuspagesSetStatusPageComponentStatusResponse404 | OpsdutyApiV1StatuspagesSetStatusPageComponentStatusResponse422]
    """

    kwargs = _get_kwargs(
        component_id=component_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    component_id: int,
    *,
    client: AuthenticatedClient,
    body: SetComponentStatusSchema,
) -> ComponentSchema | OpsdutyApiV1StatuspagesSetStatusPageComponentStatusResponse401 | OpsdutyApiV1StatuspagesSetStatusPageComponentStatusResponse404 | OpsdutyApiV1StatuspagesSetStatusPageComponentStatusResponse422 | None:
    """Set a status page component's status

     Say what a component is doing right now, without declaring an incident.

    Customers see this immediately, on the component and in the headline the
    page rolls up from every component.

    An incident that was told to keep this component in step with its impact
    still wins while it is open, because that is what somebody asked it to do.
    Use this for a component nothing has declared an incident about.

    Args:
        component_id (int):
        body (SetComponentStatusSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ComponentSchema | OpsdutyApiV1StatuspagesSetStatusPageComponentStatusResponse401 | OpsdutyApiV1StatuspagesSetStatusPageComponentStatusResponse404 | OpsdutyApiV1StatuspagesSetStatusPageComponentStatusResponse422
    """

    return (
        await asyncio_detailed(
            component_id=component_id,
            client=client,
            body=body,
        )
    ).parsed
