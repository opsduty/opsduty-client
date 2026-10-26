from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.opsduty_api_v1_heartbeats_healthcheck_environment_checkin_response_401 import OpsdutyApiV1HeartbeatsHealthcheckEnvironmentCheckinResponse401
from ...models.opsduty_api_v1_heartbeats_healthcheck_environment_checkin_response_404 import OpsdutyApiV1HeartbeatsHealthcheckEnvironmentCheckinResponse404
from ...models.opsduty_api_v1_heartbeats_healthcheck_environment_checkin_response_422 import OpsdutyApiV1HeartbeatsHealthcheckEnvironmentCheckinResponse422
from ...types import Response


def _get_kwargs(
    service_id: int,
    name: str,
    environment: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/heartbeats/checkin/{service_id}/{name}/{environment}".format(
            service_id=quote(str(service_id), safe=""),
            name=quote(str(name), safe=""),
            environment=quote(str(environment), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | OpsdutyApiV1HeartbeatsHealthcheckEnvironmentCheckinResponse401 | OpsdutyApiV1HeartbeatsHealthcheckEnvironmentCheckinResponse404 | OpsdutyApiV1HeartbeatsHealthcheckEnvironmentCheckinResponse422 | None:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200

    if response.status_code == 401:
        response_401 = OpsdutyApiV1HeartbeatsHealthcheckEnvironmentCheckinResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = OpsdutyApiV1HeartbeatsHealthcheckEnvironmentCheckinResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = OpsdutyApiV1HeartbeatsHealthcheckEnvironmentCheckinResponse422.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Any | OpsdutyApiV1HeartbeatsHealthcheckEnvironmentCheckinResponse401 | OpsdutyApiV1HeartbeatsHealthcheckEnvironmentCheckinResponse404 | OpsdutyApiV1HeartbeatsHealthcheckEnvironmentCheckinResponse422]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    service_id: int,
    name: str,
    environment: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any | OpsdutyApiV1HeartbeatsHealthcheckEnvironmentCheckinResponse401 | OpsdutyApiV1HeartbeatsHealthcheckEnvironmentCheckinResponse404 | OpsdutyApiV1HeartbeatsHealthcheckEnvironmentCheckinResponse422]:
    """Send a check-in by name

     Send a check-in, naming the heartbeat instead of using its key.

    The public check-in URL identifies a heartbeat by a key that is awkward to
    hold in a deploy script. This one takes the service, the heartbeat name and
    the environment, which you already know, and needs a token instead.

    Rate limited to 5 check-ins a minute per heartbeat and environment.

    Args:
        service_id (int):
        name (str):
        environment (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | OpsdutyApiV1HeartbeatsHealthcheckEnvironmentCheckinResponse401 | OpsdutyApiV1HeartbeatsHealthcheckEnvironmentCheckinResponse404 | OpsdutyApiV1HeartbeatsHealthcheckEnvironmentCheckinResponse422]
    """

    kwargs = _get_kwargs(
        service_id=service_id,
        name=name,
        environment=environment,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    service_id: int,
    name: str,
    environment: str,
    *,
    client: AuthenticatedClient,
) -> Any | OpsdutyApiV1HeartbeatsHealthcheckEnvironmentCheckinResponse401 | OpsdutyApiV1HeartbeatsHealthcheckEnvironmentCheckinResponse404 | OpsdutyApiV1HeartbeatsHealthcheckEnvironmentCheckinResponse422 | None:
    """Send a check-in by name

     Send a check-in, naming the heartbeat instead of using its key.

    The public check-in URL identifies a heartbeat by a key that is awkward to
    hold in a deploy script. This one takes the service, the heartbeat name and
    the environment, which you already know, and needs a token instead.

    Rate limited to 5 check-ins a minute per heartbeat and environment.

    Args:
        service_id (int):
        name (str):
        environment (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | OpsdutyApiV1HeartbeatsHealthcheckEnvironmentCheckinResponse401 | OpsdutyApiV1HeartbeatsHealthcheckEnvironmentCheckinResponse404 | OpsdutyApiV1HeartbeatsHealthcheckEnvironmentCheckinResponse422
    """

    return sync_detailed(
        service_id=service_id,
        name=name,
        environment=environment,
        client=client,
    ).parsed


async def asyncio_detailed(
    service_id: int,
    name: str,
    environment: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any | OpsdutyApiV1HeartbeatsHealthcheckEnvironmentCheckinResponse401 | OpsdutyApiV1HeartbeatsHealthcheckEnvironmentCheckinResponse404 | OpsdutyApiV1HeartbeatsHealthcheckEnvironmentCheckinResponse422]:
    """Send a check-in by name

     Send a check-in, naming the heartbeat instead of using its key.

    The public check-in URL identifies a heartbeat by a key that is awkward to
    hold in a deploy script. This one takes the service, the heartbeat name and
    the environment, which you already know, and needs a token instead.

    Rate limited to 5 check-ins a minute per heartbeat and environment.

    Args:
        service_id (int):
        name (str):
        environment (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | OpsdutyApiV1HeartbeatsHealthcheckEnvironmentCheckinResponse401 | OpsdutyApiV1HeartbeatsHealthcheckEnvironmentCheckinResponse404 | OpsdutyApiV1HeartbeatsHealthcheckEnvironmentCheckinResponse422]
    """

    kwargs = _get_kwargs(
        service_id=service_id,
        name=name,
        environment=environment,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    service_id: int,
    name: str,
    environment: str,
    *,
    client: AuthenticatedClient,
) -> Any | OpsdutyApiV1HeartbeatsHealthcheckEnvironmentCheckinResponse401 | OpsdutyApiV1HeartbeatsHealthcheckEnvironmentCheckinResponse404 | OpsdutyApiV1HeartbeatsHealthcheckEnvironmentCheckinResponse422 | None:
    """Send a check-in by name

     Send a check-in, naming the heartbeat instead of using its key.

    The public check-in URL identifies a heartbeat by a key that is awkward to
    hold in a deploy script. This one takes the service, the heartbeat name and
    the environment, which you already know, and needs a token instead.

    Rate limited to 5 check-ins a minute per heartbeat and environment.

    Args:
        service_id (int):
        name (str):
        environment (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | OpsdutyApiV1HeartbeatsHealthcheckEnvironmentCheckinResponse401 | OpsdutyApiV1HeartbeatsHealthcheckEnvironmentCheckinResponse404 | OpsdutyApiV1HeartbeatsHealthcheckEnvironmentCheckinResponse422
    """

    return (
        await asyncio_detailed(
            service_id=service_id,
            name=name,
            environment=environment,
            client=client,
        )
    ).parsed
