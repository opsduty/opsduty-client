from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.opsduty_api_v1_services_stop_service_maintenance_response_401 import OpsdutyApiV1ServicesStopServiceMaintenanceResponse401
from ...models.opsduty_api_v1_services_stop_service_maintenance_response_404 import OpsdutyApiV1ServicesStopServiceMaintenanceResponse404
from ...models.opsduty_api_v1_services_stop_service_maintenance_response_422 import OpsdutyApiV1ServicesStopServiceMaintenanceResponse422
from ...models.service_schema import ServiceSchema
from ...types import Response


def _get_kwargs(
    service_id: int,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/v1/services/{service_id}/maintenance/".format(
            service_id=quote(str(service_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> OpsdutyApiV1ServicesStopServiceMaintenanceResponse401 | OpsdutyApiV1ServicesStopServiceMaintenanceResponse404 | OpsdutyApiV1ServicesStopServiceMaintenanceResponse422 | ServiceSchema | None:
    if response.status_code == 200:
        response_200 = ServiceSchema.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = OpsdutyApiV1ServicesStopServiceMaintenanceResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = OpsdutyApiV1ServicesStopServiceMaintenanceResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = OpsdutyApiV1ServicesStopServiceMaintenanceResponse422.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[OpsdutyApiV1ServicesStopServiceMaintenanceResponse401 | OpsdutyApiV1ServicesStopServiceMaintenanceResponse404 | OpsdutyApiV1ServicesStopServiceMaintenanceResponse422 | ServiceSchema]:
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
) -> Response[OpsdutyApiV1ServicesStopServiceMaintenanceResponse401 | OpsdutyApiV1ServicesStopServiceMaintenanceResponse404 | OpsdutyApiV1ServicesStopServiceMaintenanceResponse422 | ServiceSchema]:
    """End maintenance mode

     End maintenance mode early, before its duration has elapsed. Ending
    maintenance on a service that is not in maintenance does nothing.

    Args:
        service_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OpsdutyApiV1ServicesStopServiceMaintenanceResponse401 | OpsdutyApiV1ServicesStopServiceMaintenanceResponse404 | OpsdutyApiV1ServicesStopServiceMaintenanceResponse422 | ServiceSchema]
    """

    kwargs = _get_kwargs(
        service_id=service_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    service_id: int,
    *,
    client: AuthenticatedClient,
) -> OpsdutyApiV1ServicesStopServiceMaintenanceResponse401 | OpsdutyApiV1ServicesStopServiceMaintenanceResponse404 | OpsdutyApiV1ServicesStopServiceMaintenanceResponse422 | ServiceSchema | None:
    """End maintenance mode

     End maintenance mode early, before its duration has elapsed. Ending
    maintenance on a service that is not in maintenance does nothing.

    Args:
        service_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OpsdutyApiV1ServicesStopServiceMaintenanceResponse401 | OpsdutyApiV1ServicesStopServiceMaintenanceResponse404 | OpsdutyApiV1ServicesStopServiceMaintenanceResponse422 | ServiceSchema
    """

    return sync_detailed(
        service_id=service_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    service_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[OpsdutyApiV1ServicesStopServiceMaintenanceResponse401 | OpsdutyApiV1ServicesStopServiceMaintenanceResponse404 | OpsdutyApiV1ServicesStopServiceMaintenanceResponse422 | ServiceSchema]:
    """End maintenance mode

     End maintenance mode early, before its duration has elapsed. Ending
    maintenance on a service that is not in maintenance does nothing.

    Args:
        service_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OpsdutyApiV1ServicesStopServiceMaintenanceResponse401 | OpsdutyApiV1ServicesStopServiceMaintenanceResponse404 | OpsdutyApiV1ServicesStopServiceMaintenanceResponse422 | ServiceSchema]
    """

    kwargs = _get_kwargs(
        service_id=service_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    service_id: int,
    *,
    client: AuthenticatedClient,
) -> OpsdutyApiV1ServicesStopServiceMaintenanceResponse401 | OpsdutyApiV1ServicesStopServiceMaintenanceResponse404 | OpsdutyApiV1ServicesStopServiceMaintenanceResponse422 | ServiceSchema | None:
    """End maintenance mode

     End maintenance mode early, before its duration has elapsed. Ending
    maintenance on a service that is not in maintenance does nothing.

    Args:
        service_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OpsdutyApiV1ServicesStopServiceMaintenanceResponse401 | OpsdutyApiV1ServicesStopServiceMaintenanceResponse404 | OpsdutyApiV1ServicesStopServiceMaintenanceResponse422 | ServiceSchema
    """

    return (
        await asyncio_detailed(
            service_id=service_id,
            client=client,
        )
    ).parsed
