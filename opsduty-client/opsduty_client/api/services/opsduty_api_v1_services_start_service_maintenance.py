from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.opsduty_api_v1_services_start_service_maintenance_response_401 import OpsdutyApiV1ServicesStartServiceMaintenanceResponse401
from ...models.opsduty_api_v1_services_start_service_maintenance_response_404 import OpsdutyApiV1ServicesStartServiceMaintenanceResponse404
from ...models.opsduty_api_v1_services_start_service_maintenance_response_422 import OpsdutyApiV1ServicesStartServiceMaintenanceResponse422
from ...models.service_schema import ServiceSchema
from ...models.start_maintenance_input_schema import StartMaintenanceInputSchema
from ...types import UNSET, Response, Unset


def _get_kwargs(
    service_id: int,
    *,
    body: None | StartMaintenanceInputSchema | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/services/{service_id}/maintenance/".format(
            service_id=quote(str(service_id), safe=""),
        ),
    }

    if isinstance(body, StartMaintenanceInputSchema):
        _kwargs["json"] = body.to_dict()
    else:
        _kwargs["json"] = body

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> OpsdutyApiV1ServicesStartServiceMaintenanceResponse401 | OpsdutyApiV1ServicesStartServiceMaintenanceResponse404 | OpsdutyApiV1ServicesStartServiceMaintenanceResponse422 | ServiceSchema | None:
    if response.status_code == 200:
        response_200 = ServiceSchema.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = OpsdutyApiV1ServicesStartServiceMaintenanceResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = OpsdutyApiV1ServicesStartServiceMaintenanceResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = OpsdutyApiV1ServicesStartServiceMaintenanceResponse422.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[OpsdutyApiV1ServicesStartServiceMaintenanceResponse401 | OpsdutyApiV1ServicesStartServiceMaintenanceResponse404 | OpsdutyApiV1ServicesStartServiceMaintenanceResponse422 | ServiceSchema]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    service_id: int,
    *,
    client: AuthenticatedClient,
    body: None | StartMaintenanceInputSchema | Unset = UNSET,
) -> Response[OpsdutyApiV1ServicesStartServiceMaintenanceResponse401 | OpsdutyApiV1ServicesStartServiceMaintenanceResponse404 | OpsdutyApiV1ServicesStartServiceMaintenanceResponse422 | ServiceSchema]:
    """Start maintenance mode

     Put a service into maintenance mode so a planned change does not page
    anyone. Maintenance mode ends by itself once the duration elapses, and
    starting it on a service that is already in maintenance is rejected.

    Args:
        service_id (int):
        body (None | StartMaintenanceInputSchema | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OpsdutyApiV1ServicesStartServiceMaintenanceResponse401 | OpsdutyApiV1ServicesStartServiceMaintenanceResponse404 | OpsdutyApiV1ServicesStartServiceMaintenanceResponse422 | ServiceSchema]
    """

    kwargs = _get_kwargs(
        service_id=service_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    service_id: int,
    *,
    client: AuthenticatedClient,
    body: None | StartMaintenanceInputSchema | Unset = UNSET,
) -> OpsdutyApiV1ServicesStartServiceMaintenanceResponse401 | OpsdutyApiV1ServicesStartServiceMaintenanceResponse404 | OpsdutyApiV1ServicesStartServiceMaintenanceResponse422 | ServiceSchema | None:
    """Start maintenance mode

     Put a service into maintenance mode so a planned change does not page
    anyone. Maintenance mode ends by itself once the duration elapses, and
    starting it on a service that is already in maintenance is rejected.

    Args:
        service_id (int):
        body (None | StartMaintenanceInputSchema | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OpsdutyApiV1ServicesStartServiceMaintenanceResponse401 | OpsdutyApiV1ServicesStartServiceMaintenanceResponse404 | OpsdutyApiV1ServicesStartServiceMaintenanceResponse422 | ServiceSchema
    """

    return sync_detailed(
        service_id=service_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    service_id: int,
    *,
    client: AuthenticatedClient,
    body: None | StartMaintenanceInputSchema | Unset = UNSET,
) -> Response[OpsdutyApiV1ServicesStartServiceMaintenanceResponse401 | OpsdutyApiV1ServicesStartServiceMaintenanceResponse404 | OpsdutyApiV1ServicesStartServiceMaintenanceResponse422 | ServiceSchema]:
    """Start maintenance mode

     Put a service into maintenance mode so a planned change does not page
    anyone. Maintenance mode ends by itself once the duration elapses, and
    starting it on a service that is already in maintenance is rejected.

    Args:
        service_id (int):
        body (None | StartMaintenanceInputSchema | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OpsdutyApiV1ServicesStartServiceMaintenanceResponse401 | OpsdutyApiV1ServicesStartServiceMaintenanceResponse404 | OpsdutyApiV1ServicesStartServiceMaintenanceResponse422 | ServiceSchema]
    """

    kwargs = _get_kwargs(
        service_id=service_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    service_id: int,
    *,
    client: AuthenticatedClient,
    body: None | StartMaintenanceInputSchema | Unset = UNSET,
) -> OpsdutyApiV1ServicesStartServiceMaintenanceResponse401 | OpsdutyApiV1ServicesStartServiceMaintenanceResponse404 | OpsdutyApiV1ServicesStartServiceMaintenanceResponse422 | ServiceSchema | None:
    """Start maintenance mode

     Put a service into maintenance mode so a planned change does not page
    anyone. Maintenance mode ends by itself once the duration elapses, and
    starting it on a service that is already in maintenance is rejected.

    Args:
        service_id (int):
        body (None | StartMaintenanceInputSchema | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OpsdutyApiV1ServicesStartServiceMaintenanceResponse401 | OpsdutyApiV1ServicesStartServiceMaintenanceResponse404 | OpsdutyApiV1ServicesStartServiceMaintenanceResponse422 | ServiceSchema
    """

    return (
        await asyncio_detailed(
            service_id=service_id,
            client=client,
            body=body,
        )
    ).parsed
