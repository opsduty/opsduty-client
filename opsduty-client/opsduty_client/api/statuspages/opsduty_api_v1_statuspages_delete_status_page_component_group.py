from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.opsduty_api_v1_statuspages_delete_status_page_component_group_response_401 import OpsdutyApiV1StatuspagesDeleteStatusPageComponentGroupResponse401
from ...models.opsduty_api_v1_statuspages_delete_status_page_component_group_response_404 import OpsdutyApiV1StatuspagesDeleteStatusPageComponentGroupResponse404
from ...models.opsduty_api_v1_statuspages_delete_status_page_component_group_response_422 import OpsdutyApiV1StatuspagesDeleteStatusPageComponentGroupResponse422
from ...types import Response


def _get_kwargs(
    component_group_id: int,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/v1/statuspages/component-groups/{component_group_id}/".format(
            component_group_id=quote(str(component_group_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | OpsdutyApiV1StatuspagesDeleteStatusPageComponentGroupResponse401 | OpsdutyApiV1StatuspagesDeleteStatusPageComponentGroupResponse404 | OpsdutyApiV1StatuspagesDeleteStatusPageComponentGroupResponse422 | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

    if response.status_code == 401:
        response_401 = OpsdutyApiV1StatuspagesDeleteStatusPageComponentGroupResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = OpsdutyApiV1StatuspagesDeleteStatusPageComponentGroupResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = OpsdutyApiV1StatuspagesDeleteStatusPageComponentGroupResponse422.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | OpsdutyApiV1StatuspagesDeleteStatusPageComponentGroupResponse401 | OpsdutyApiV1StatuspagesDeleteStatusPageComponentGroupResponse404 | OpsdutyApiV1StatuspagesDeleteStatusPageComponentGroupResponse422]:
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
) -> Response[Any | OpsdutyApiV1StatuspagesDeleteStatusPageComponentGroupResponse401 | OpsdutyApiV1StatuspagesDeleteStatusPageComponentGroupResponse404 | OpsdutyApiV1StatuspagesDeleteStatusPageComponentGroupResponse422]:
    """Delete a status page component group

     Delete a component group and every component in it. Customers stop seeing
    them straight away, and incidents no longer list them as affected.

    Args:
        component_group_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | OpsdutyApiV1StatuspagesDeleteStatusPageComponentGroupResponse401 | OpsdutyApiV1StatuspagesDeleteStatusPageComponentGroupResponse404 | OpsdutyApiV1StatuspagesDeleteStatusPageComponentGroupResponse422]
    """

    kwargs = _get_kwargs(
        component_group_id=component_group_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    component_group_id: int,
    *,
    client: AuthenticatedClient,
) -> Any | OpsdutyApiV1StatuspagesDeleteStatusPageComponentGroupResponse401 | OpsdutyApiV1StatuspagesDeleteStatusPageComponentGroupResponse404 | OpsdutyApiV1StatuspagesDeleteStatusPageComponentGroupResponse422 | None:
    """Delete a status page component group

     Delete a component group and every component in it. Customers stop seeing
    them straight away, and incidents no longer list them as affected.

    Args:
        component_group_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | OpsdutyApiV1StatuspagesDeleteStatusPageComponentGroupResponse401 | OpsdutyApiV1StatuspagesDeleteStatusPageComponentGroupResponse404 | OpsdutyApiV1StatuspagesDeleteStatusPageComponentGroupResponse422
    """

    return sync_detailed(
        component_group_id=component_group_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    component_group_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Any | OpsdutyApiV1StatuspagesDeleteStatusPageComponentGroupResponse401 | OpsdutyApiV1StatuspagesDeleteStatusPageComponentGroupResponse404 | OpsdutyApiV1StatuspagesDeleteStatusPageComponentGroupResponse422]:
    """Delete a status page component group

     Delete a component group and every component in it. Customers stop seeing
    them straight away, and incidents no longer list them as affected.

    Args:
        component_group_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | OpsdutyApiV1StatuspagesDeleteStatusPageComponentGroupResponse401 | OpsdutyApiV1StatuspagesDeleteStatusPageComponentGroupResponse404 | OpsdutyApiV1StatuspagesDeleteStatusPageComponentGroupResponse422]
    """

    kwargs = _get_kwargs(
        component_group_id=component_group_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    component_group_id: int,
    *,
    client: AuthenticatedClient,
) -> Any | OpsdutyApiV1StatuspagesDeleteStatusPageComponentGroupResponse401 | OpsdutyApiV1StatuspagesDeleteStatusPageComponentGroupResponse404 | OpsdutyApiV1StatuspagesDeleteStatusPageComponentGroupResponse422 | None:
    """Delete a status page component group

     Delete a component group and every component in it. Customers stop seeing
    them straight away, and incidents no longer list them as affected.

    Args:
        component_group_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | OpsdutyApiV1StatuspagesDeleteStatusPageComponentGroupResponse401 | OpsdutyApiV1StatuspagesDeleteStatusPageComponentGroupResponse404 | OpsdutyApiV1StatuspagesDeleteStatusPageComponentGroupResponse422
    """

    return (
        await asyncio_detailed(
            component_group_id=component_group_id,
            client=client,
        )
    ).parsed
