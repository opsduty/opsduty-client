from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.component_group_schema import ComponentGroupSchema
from ...models.move_component_group_schema import MoveComponentGroupSchema
from ...models.opsduty_api_v1_statuspages_move_status_page_component_group_response_401 import OpsdutyApiV1StatuspagesMoveStatusPageComponentGroupResponse401
from ...models.opsduty_api_v1_statuspages_move_status_page_component_group_response_404 import OpsdutyApiV1StatuspagesMoveStatusPageComponentGroupResponse404
from ...models.opsduty_api_v1_statuspages_move_status_page_component_group_response_422 import OpsdutyApiV1StatuspagesMoveStatusPageComponentGroupResponse422
from ...types import Response


def _get_kwargs(
    component_group_id: int,
    *,
    body: MoveComponentGroupSchema,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/statuspages/component-groups/{component_group_id}/move/".format(
            component_group_id=quote(str(component_group_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ComponentGroupSchema | OpsdutyApiV1StatuspagesMoveStatusPageComponentGroupResponse401 | OpsdutyApiV1StatuspagesMoveStatusPageComponentGroupResponse404 | OpsdutyApiV1StatuspagesMoveStatusPageComponentGroupResponse422 | None:
    if response.status_code == 200:
        response_200 = ComponentGroupSchema.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = OpsdutyApiV1StatuspagesMoveStatusPageComponentGroupResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = OpsdutyApiV1StatuspagesMoveStatusPageComponentGroupResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = OpsdutyApiV1StatuspagesMoveStatusPageComponentGroupResponse422.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ComponentGroupSchema | OpsdutyApiV1StatuspagesMoveStatusPageComponentGroupResponse401 | OpsdutyApiV1StatuspagesMoveStatusPageComponentGroupResponse404 | OpsdutyApiV1StatuspagesMoveStatusPageComponentGroupResponse422]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    component_group_id: int,
    *,
    client: AuthenticatedClient,
    body: MoveComponentGroupSchema,
) -> Response[ComponentGroupSchema | OpsdutyApiV1StatuspagesMoveStatusPageComponentGroupResponse401 | OpsdutyApiV1StatuspagesMoveStatusPageComponentGroupResponse404 | OpsdutyApiV1StatuspagesMoveStatusPageComponentGroupResponse422]:
    """Move a status page component group

     Move a component group up, down, to the top or to the bottom of the page.

    Args:
        component_group_id (int):
        body (MoveComponentGroupSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ComponentGroupSchema | OpsdutyApiV1StatuspagesMoveStatusPageComponentGroupResponse401 | OpsdutyApiV1StatuspagesMoveStatusPageComponentGroupResponse404 | OpsdutyApiV1StatuspagesMoveStatusPageComponentGroupResponse422]
    """

    kwargs = _get_kwargs(
        component_group_id=component_group_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    component_group_id: int,
    *,
    client: AuthenticatedClient,
    body: MoveComponentGroupSchema,
) -> ComponentGroupSchema | OpsdutyApiV1StatuspagesMoveStatusPageComponentGroupResponse401 | OpsdutyApiV1StatuspagesMoveStatusPageComponentGroupResponse404 | OpsdutyApiV1StatuspagesMoveStatusPageComponentGroupResponse422 | None:
    """Move a status page component group

     Move a component group up, down, to the top or to the bottom of the page.

    Args:
        component_group_id (int):
        body (MoveComponentGroupSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ComponentGroupSchema | OpsdutyApiV1StatuspagesMoveStatusPageComponentGroupResponse401 | OpsdutyApiV1StatuspagesMoveStatusPageComponentGroupResponse404 | OpsdutyApiV1StatuspagesMoveStatusPageComponentGroupResponse422
    """

    return sync_detailed(
        component_group_id=component_group_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    component_group_id: int,
    *,
    client: AuthenticatedClient,
    body: MoveComponentGroupSchema,
) -> Response[ComponentGroupSchema | OpsdutyApiV1StatuspagesMoveStatusPageComponentGroupResponse401 | OpsdutyApiV1StatuspagesMoveStatusPageComponentGroupResponse404 | OpsdutyApiV1StatuspagesMoveStatusPageComponentGroupResponse422]:
    """Move a status page component group

     Move a component group up, down, to the top or to the bottom of the page.

    Args:
        component_group_id (int):
        body (MoveComponentGroupSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ComponentGroupSchema | OpsdutyApiV1StatuspagesMoveStatusPageComponentGroupResponse401 | OpsdutyApiV1StatuspagesMoveStatusPageComponentGroupResponse404 | OpsdutyApiV1StatuspagesMoveStatusPageComponentGroupResponse422]
    """

    kwargs = _get_kwargs(
        component_group_id=component_group_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    component_group_id: int,
    *,
    client: AuthenticatedClient,
    body: MoveComponentGroupSchema,
) -> ComponentGroupSchema | OpsdutyApiV1StatuspagesMoveStatusPageComponentGroupResponse401 | OpsdutyApiV1StatuspagesMoveStatusPageComponentGroupResponse404 | OpsdutyApiV1StatuspagesMoveStatusPageComponentGroupResponse422 | None:
    """Move a status page component group

     Move a component group up, down, to the top or to the bottom of the page.

    Args:
        component_group_id (int):
        body (MoveComponentGroupSchema):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ComponentGroupSchema | OpsdutyApiV1StatuspagesMoveStatusPageComponentGroupResponse401 | OpsdutyApiV1StatuspagesMoveStatusPageComponentGroupResponse404 | OpsdutyApiV1StatuspagesMoveStatusPageComponentGroupResponse422
    """

    return (
        await asyncio_detailed(
            component_group_id=component_group_id,
            client=client,
            body=body,
        )
    ).parsed
