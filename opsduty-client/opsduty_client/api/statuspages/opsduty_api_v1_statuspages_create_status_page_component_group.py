from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.component_group_input_schema import ComponentGroupInputSchema
from ...models.component_group_schema import ComponentGroupSchema
from ...models.opsduty_api_v1_statuspages_create_status_page_component_group_response_401 import OpsdutyApiV1StatuspagesCreateStatusPageComponentGroupResponse401
from ...models.opsduty_api_v1_statuspages_create_status_page_component_group_response_404 import OpsdutyApiV1StatuspagesCreateStatusPageComponentGroupResponse404
from ...models.opsduty_api_v1_statuspages_create_status_page_component_group_response_422 import OpsdutyApiV1StatuspagesCreateStatusPageComponentGroupResponse422
from ...types import Response


def _get_kwargs(
    status_page_id: int,
    *,
    body: ComponentGroupInputSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/statuspages/{status_page_id}/component-groups/".format(
            status_page_id=quote(str(status_page_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ComponentGroupSchema | OpsdutyApiV1StatuspagesCreateStatusPageComponentGroupResponse401 | OpsdutyApiV1StatuspagesCreateStatusPageComponentGroupResponse404 | OpsdutyApiV1StatuspagesCreateStatusPageComponentGroupResponse422 | None:
    if response.status_code == 200:
        response_200 = ComponentGroupSchema.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = OpsdutyApiV1StatuspagesCreateStatusPageComponentGroupResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = OpsdutyApiV1StatuspagesCreateStatusPageComponentGroupResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = OpsdutyApiV1StatuspagesCreateStatusPageComponentGroupResponse422.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ComponentGroupSchema | OpsdutyApiV1StatuspagesCreateStatusPageComponentGroupResponse401 | OpsdutyApiV1StatuspagesCreateStatusPageComponentGroupResponse404 | OpsdutyApiV1StatuspagesCreateStatusPageComponentGroupResponse422]:
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
    body: ComponentGroupInputSchema,
) -> Response[ComponentGroupSchema | OpsdutyApiV1StatuspagesCreateStatusPageComponentGroupResponse401 | OpsdutyApiV1StatuspagesCreateStatusPageComponentGroupResponse404 | OpsdutyApiV1StatuspagesCreateStatusPageComponentGroupResponse422]:
    """Create a status page component group

     Add a group to the bottom of a status page. Customers see it once it has
    components in it.

    Args:
        status_page_id (int):
        body (ComponentGroupInputSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ComponentGroupSchema | OpsdutyApiV1StatuspagesCreateStatusPageComponentGroupResponse401 | OpsdutyApiV1StatuspagesCreateStatusPageComponentGroupResponse404 | OpsdutyApiV1StatuspagesCreateStatusPageComponentGroupResponse422]
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
    body: ComponentGroupInputSchema,
) -> ComponentGroupSchema | OpsdutyApiV1StatuspagesCreateStatusPageComponentGroupResponse401 | OpsdutyApiV1StatuspagesCreateStatusPageComponentGroupResponse404 | OpsdutyApiV1StatuspagesCreateStatusPageComponentGroupResponse422 | None:
    """Create a status page component group

     Add a group to the bottom of a status page. Customers see it once it has
    components in it.

    Args:
        status_page_id (int):
        body (ComponentGroupInputSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ComponentGroupSchema | OpsdutyApiV1StatuspagesCreateStatusPageComponentGroupResponse401 | OpsdutyApiV1StatuspagesCreateStatusPageComponentGroupResponse404 | OpsdutyApiV1StatuspagesCreateStatusPageComponentGroupResponse422
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
    body: ComponentGroupInputSchema,
) -> Response[ComponentGroupSchema | OpsdutyApiV1StatuspagesCreateStatusPageComponentGroupResponse401 | OpsdutyApiV1StatuspagesCreateStatusPageComponentGroupResponse404 | OpsdutyApiV1StatuspagesCreateStatusPageComponentGroupResponse422]:
    """Create a status page component group

     Add a group to the bottom of a status page. Customers see it once it has
    components in it.

    Args:
        status_page_id (int):
        body (ComponentGroupInputSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ComponentGroupSchema | OpsdutyApiV1StatuspagesCreateStatusPageComponentGroupResponse401 | OpsdutyApiV1StatuspagesCreateStatusPageComponentGroupResponse404 | OpsdutyApiV1StatuspagesCreateStatusPageComponentGroupResponse422]
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
    body: ComponentGroupInputSchema,
) -> ComponentGroupSchema | OpsdutyApiV1StatuspagesCreateStatusPageComponentGroupResponse401 | OpsdutyApiV1StatuspagesCreateStatusPageComponentGroupResponse404 | OpsdutyApiV1StatuspagesCreateStatusPageComponentGroupResponse422 | None:
    """Create a status page component group

     Add a group to the bottom of a status page. Customers see it once it has
    components in it.

    Args:
        status_page_id (int):
        body (ComponentGroupInputSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ComponentGroupSchema | OpsdutyApiV1StatuspagesCreateStatusPageComponentGroupResponse401 | OpsdutyApiV1StatuspagesCreateStatusPageComponentGroupResponse404 | OpsdutyApiV1StatuspagesCreateStatusPageComponentGroupResponse422
    """

    return (
        await asyncio_detailed(
            status_page_id=status_page_id,
            client=client,
            body=body,
        )
    ).parsed
