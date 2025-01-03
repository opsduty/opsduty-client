from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.incident_group_detail_schema import IncidentGroupDetailSchema
from ...types import Response


def _get_kwargs(
    incident_group_id: int,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/incidents/{incident_group_id}/".format(
            incident_group_id=incident_group_id,
        ),
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[IncidentGroupDetailSchema]:
    if response.status_code == HTTPStatus.OK:
        response_200 = IncidentGroupDetailSchema.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[IncidentGroupDetailSchema]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    incident_group_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[IncidentGroupDetailSchema]:
    """Retrieve Incident

    Args:
        incident_group_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IncidentGroupDetailSchema]
    """

    kwargs = _get_kwargs(
        incident_group_id=incident_group_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    incident_group_id: int,
    *,
    client: AuthenticatedClient,
) -> Optional[IncidentGroupDetailSchema]:
    """Retrieve Incident

    Args:
        incident_group_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IncidentGroupDetailSchema
    """

    return sync_detailed(
        incident_group_id=incident_group_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    incident_group_id: int,
    *,
    client: AuthenticatedClient,
) -> Response[IncidentGroupDetailSchema]:
    """Retrieve Incident

    Args:
        incident_group_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[IncidentGroupDetailSchema]
    """

    kwargs = _get_kwargs(
        incident_group_id=incident_group_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    incident_group_id: int,
    *,
    client: AuthenticatedClient,
) -> Optional[IncidentGroupDetailSchema]:
    """Retrieve Incident

    Args:
        incident_group_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        IncidentGroupDetailSchema
    """

    return (
        await asyncio_detailed(
            incident_group_id=incident_group_id,
            client=client,
        )
    ).parsed
