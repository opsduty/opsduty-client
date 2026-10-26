from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.opsduty_api_v1_statuspages_list_status_page_incident_updates_response_401 import OpsdutyApiV1StatuspagesListStatusPageIncidentUpdatesResponse401
from ...models.opsduty_api_v1_statuspages_list_status_page_incident_updates_response_404 import OpsdutyApiV1StatuspagesListStatusPageIncidentUpdatesResponse404
from ...models.opsduty_api_v1_statuspages_list_status_page_incident_updates_response_422 import OpsdutyApiV1StatuspagesListStatusPageIncidentUpdatesResponse422
from ...models.paged_incident_update_schema import PagedIncidentUpdateSchema
from ...types import UNSET, Response, Unset


def _get_kwargs(
    incident_id: int,
    *,
    first: int | None | Unset = UNSET,
    last: int | None | Unset = UNSET,
    before: None | str | Unset = UNSET,
    after: None | str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_first: int | None | Unset
    if isinstance(first, Unset):
        json_first = UNSET
    else:
        json_first = first
    params["first"] = json_first

    json_last: int | None | Unset
    if isinstance(last, Unset):
        json_last = UNSET
    else:
        json_last = last
    params["last"] = json_last

    json_before: None | str | Unset
    if isinstance(before, Unset):
        json_before = UNSET
    else:
        json_before = before
    params["before"] = json_before

    json_after: None | str | Unset
    if isinstance(after, Unset):
        json_after = UNSET
    else:
        json_after = after
    params["after"] = json_after

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/statuspages/incidents/{incident_id}/updates/".format(
            incident_id=quote(str(incident_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> OpsdutyApiV1StatuspagesListStatusPageIncidentUpdatesResponse401 | OpsdutyApiV1StatuspagesListStatusPageIncidentUpdatesResponse404 | OpsdutyApiV1StatuspagesListStatusPageIncidentUpdatesResponse422 | PagedIncidentUpdateSchema | None:
    if response.status_code == 200:
        response_200 = PagedIncidentUpdateSchema.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = OpsdutyApiV1StatuspagesListStatusPageIncidentUpdatesResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = OpsdutyApiV1StatuspagesListStatusPageIncidentUpdatesResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = OpsdutyApiV1StatuspagesListStatusPageIncidentUpdatesResponse422.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[OpsdutyApiV1StatuspagesListStatusPageIncidentUpdatesResponse401 | OpsdutyApiV1StatuspagesListStatusPageIncidentUpdatesResponse404 | OpsdutyApiV1StatuspagesListStatusPageIncidentUpdatesResponse422 | PagedIncidentUpdateSchema]:
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
    first: int | None | Unset = UNSET,
    last: int | None | Unset = UNSET,
    before: None | str | Unset = UNSET,
    after: None | str | Unset = UNSET,
) -> Response[OpsdutyApiV1StatuspagesListStatusPageIncidentUpdatesResponse401 | OpsdutyApiV1StatuspagesListStatusPageIncidentUpdatesResponse404 | OpsdutyApiV1StatuspagesListStatusPageIncidentUpdatesResponse422 | PagedIncidentUpdateSchema]:
    """List status page incident updates

     List the updates posted to an incident, newest first.

    Args:
        incident_id (int):
        first (int | None | Unset): How many items to return from the start of the list, or after
            `after`.
        last (int | None | Unset): How many items to return from the end of the list, or before
            `before`. They are still in list order.
        before (None | str | Unset): A `start_cursor` to page back from.
        after (None | str | Unset): An `end_cursor` to page on from.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OpsdutyApiV1StatuspagesListStatusPageIncidentUpdatesResponse401 | OpsdutyApiV1StatuspagesListStatusPageIncidentUpdatesResponse404 | OpsdutyApiV1StatuspagesListStatusPageIncidentUpdatesResponse422 | PagedIncidentUpdateSchema]
    """

    kwargs = _get_kwargs(
        incident_id=incident_id,
        first=first,
        last=last,
        before=before,
        after=after,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    incident_id: int,
    *,
    client: AuthenticatedClient,
    first: int | None | Unset = UNSET,
    last: int | None | Unset = UNSET,
    before: None | str | Unset = UNSET,
    after: None | str | Unset = UNSET,
) -> OpsdutyApiV1StatuspagesListStatusPageIncidentUpdatesResponse401 | OpsdutyApiV1StatuspagesListStatusPageIncidentUpdatesResponse404 | OpsdutyApiV1StatuspagesListStatusPageIncidentUpdatesResponse422 | PagedIncidentUpdateSchema | None:
    """List status page incident updates

     List the updates posted to an incident, newest first.

    Args:
        incident_id (int):
        first (int | None | Unset): How many items to return from the start of the list, or after
            `after`.
        last (int | None | Unset): How many items to return from the end of the list, or before
            `before`. They are still in list order.
        before (None | str | Unset): A `start_cursor` to page back from.
        after (None | str | Unset): An `end_cursor` to page on from.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OpsdutyApiV1StatuspagesListStatusPageIncidentUpdatesResponse401 | OpsdutyApiV1StatuspagesListStatusPageIncidentUpdatesResponse404 | OpsdutyApiV1StatuspagesListStatusPageIncidentUpdatesResponse422 | PagedIncidentUpdateSchema
    """

    return sync_detailed(
        incident_id=incident_id,
        client=client,
        first=first,
        last=last,
        before=before,
        after=after,
    ).parsed


async def asyncio_detailed(
    incident_id: int,
    *,
    client: AuthenticatedClient,
    first: int | None | Unset = UNSET,
    last: int | None | Unset = UNSET,
    before: None | str | Unset = UNSET,
    after: None | str | Unset = UNSET,
) -> Response[OpsdutyApiV1StatuspagesListStatusPageIncidentUpdatesResponse401 | OpsdutyApiV1StatuspagesListStatusPageIncidentUpdatesResponse404 | OpsdutyApiV1StatuspagesListStatusPageIncidentUpdatesResponse422 | PagedIncidentUpdateSchema]:
    """List status page incident updates

     List the updates posted to an incident, newest first.

    Args:
        incident_id (int):
        first (int | None | Unset): How many items to return from the start of the list, or after
            `after`.
        last (int | None | Unset): How many items to return from the end of the list, or before
            `before`. They are still in list order.
        before (None | str | Unset): A `start_cursor` to page back from.
        after (None | str | Unset): An `end_cursor` to page on from.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[OpsdutyApiV1StatuspagesListStatusPageIncidentUpdatesResponse401 | OpsdutyApiV1StatuspagesListStatusPageIncidentUpdatesResponse404 | OpsdutyApiV1StatuspagesListStatusPageIncidentUpdatesResponse422 | PagedIncidentUpdateSchema]
    """

    kwargs = _get_kwargs(
        incident_id=incident_id,
        first=first,
        last=last,
        before=before,
        after=after,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    incident_id: int,
    *,
    client: AuthenticatedClient,
    first: int | None | Unset = UNSET,
    last: int | None | Unset = UNSET,
    before: None | str | Unset = UNSET,
    after: None | str | Unset = UNSET,
) -> OpsdutyApiV1StatuspagesListStatusPageIncidentUpdatesResponse401 | OpsdutyApiV1StatuspagesListStatusPageIncidentUpdatesResponse404 | OpsdutyApiV1StatuspagesListStatusPageIncidentUpdatesResponse422 | PagedIncidentUpdateSchema | None:
    """List status page incident updates

     List the updates posted to an incident, newest first.

    Args:
        incident_id (int):
        first (int | None | Unset): How many items to return from the start of the list, or after
            `after`.
        last (int | None | Unset): How many items to return from the end of the list, or before
            `before`. They are still in list order.
        before (None | str | Unset): A `start_cursor` to page back from.
        after (None | str | Unset): An `end_cursor` to page on from.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        OpsdutyApiV1StatuspagesListStatusPageIncidentUpdatesResponse401 | OpsdutyApiV1StatuspagesListStatusPageIncidentUpdatesResponse404 | OpsdutyApiV1StatuspagesListStatusPageIncidentUpdatesResponse422 | PagedIncidentUpdateSchema
    """

    return (
        await asyncio_detailed(
            incident_id=incident_id,
            client=client,
            first=first,
            last=last,
            before=before,
            after=after,
        )
    ).parsed
