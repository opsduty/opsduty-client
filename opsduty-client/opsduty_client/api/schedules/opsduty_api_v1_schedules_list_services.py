from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paged_schedule_schema import PagedScheduleSchema
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    page_size: Union[None, Unset, int] = UNSET,
    before: Union[None, Unset, str] = UNSET,
    after: Union[None, Unset, str] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    json_page_size: Union[None, Unset, int]
    if isinstance(page_size, Unset):
        json_page_size = UNSET
    else:
        json_page_size = page_size
    params["page_size"] = json_page_size

    json_before: Union[None, Unset, str]
    if isinstance(before, Unset):
        json_before = UNSET
    else:
        json_before = before
    params["before"] = json_before

    json_after: Union[None, Unset, str]
    if isinstance(after, Unset):
        json_after = UNSET
    else:
        json_after = after
    params["after"] = json_after

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/schedules/",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[PagedScheduleSchema]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PagedScheduleSchema.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[PagedScheduleSchema]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    page_size: Union[None, Unset, int] = UNSET,
    before: Union[None, Unset, str] = UNSET,
    after: Union[None, Unset, str] = UNSET,
) -> Response[PagedScheduleSchema]:
    """List Services

    Args:
        page_size (Union[None, Unset, int]):
        before (Union[None, Unset, str]):
        after (Union[None, Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PagedScheduleSchema]
    """

    kwargs = _get_kwargs(
        page_size=page_size,
        before=before,
        after=after,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    page_size: Union[None, Unset, int] = UNSET,
    before: Union[None, Unset, str] = UNSET,
    after: Union[None, Unset, str] = UNSET,
) -> Optional[PagedScheduleSchema]:
    """List Services

    Args:
        page_size (Union[None, Unset, int]):
        before (Union[None, Unset, str]):
        after (Union[None, Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PagedScheduleSchema
    """

    return sync_detailed(
        client=client,
        page_size=page_size,
        before=before,
        after=after,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    page_size: Union[None, Unset, int] = UNSET,
    before: Union[None, Unset, str] = UNSET,
    after: Union[None, Unset, str] = UNSET,
) -> Response[PagedScheduleSchema]:
    """List Services

    Args:
        page_size (Union[None, Unset, int]):
        before (Union[None, Unset, str]):
        after (Union[None, Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PagedScheduleSchema]
    """

    kwargs = _get_kwargs(
        page_size=page_size,
        before=before,
        after=after,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    page_size: Union[None, Unset, int] = UNSET,
    before: Union[None, Unset, str] = UNSET,
    after: Union[None, Unset, str] = UNSET,
) -> Optional[PagedScheduleSchema]:
    """List Services

    Args:
        page_size (Union[None, Unset, int]):
        before (Union[None, Unset, str]):
        after (Union[None, Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PagedScheduleSchema
    """

    return (
        await asyncio_detailed(
            client=client,
            page_size=page_size,
            before=before,
            after=after,
        )
    ).parsed
