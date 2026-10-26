from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.opsduty_api_v1_incidents_list_incident_responders_response_401 import OpsdutyApiV1IncidentsListIncidentRespondersResponse401
from ...models.opsduty_api_v1_incidents_list_incident_responders_response_404 import OpsdutyApiV1IncidentsListIncidentRespondersResponse404
from ...models.opsduty_api_v1_incidents_list_incident_responders_response_422 import OpsdutyApiV1IncidentsListIncidentRespondersResponse422
from ...models.paged_incident_group_responder_schema import PagedIncidentGroupResponderSchema
from ...types import UNSET, Response, Unset


def _get_kwargs(
    incident_group_id: int,
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
        "url": "/api/v1/incidents/{incident_group_id}/responders/".format(
            incident_group_id=quote(str(incident_group_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> OpsdutyApiV1IncidentsListIncidentRespondersResponse401 | OpsdutyApiV1IncidentsListIncidentRespondersResponse404 | OpsdutyApiV1IncidentsListIncidentRespondersResponse422 | PagedIncidentGroupResponderSchema | None:
    if response.status_code == 200:
        response_200 = PagedIncidentGroupResponderSchema.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = OpsdutyApiV1IncidentsListIncidentRespondersResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = OpsdutyApiV1IncidentsListIncidentRespondersResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = OpsdutyApiV1IncidentsListIncidentRespondersResponse422.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[OpsdutyApiV1IncidentsListIncidentRespondersResponse401 | OpsdutyApiV1IncidentsListIncidentRespondersResponse404 | OpsdutyApiV1IncidentsListIncidentRespondersResponse422 | PagedIncidentGroupResponderSchema]:
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
    first: int | None | Unset = UNSET,
    last: int | None | Unset = UNSET,
    before: None | str | Unset = UNSET,
    after: None | str | Unset = UNSET,
) -> Response[OpsdutyApiV1IncidentsListIncidentRespondersResponse401 | OpsdutyApiV1IncidentsListIncidentRespondersResponse404 | OpsdutyApiV1IncidentsListIncidentRespondersResponse422 | PagedIncidentGroupResponderSchema]:
    """List an incident's responders

     List who this incident has reached, and whether they responded.

    Args:
        incident_group_id (int):
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
        Response[OpsdutyApiV1IncidentsListIncidentRespondersResponse401 | OpsdutyApiV1IncidentsListIncidentRespondersResponse404 | OpsdutyApiV1IncidentsListIncidentRespondersResponse422 | PagedIncidentGroupResponderSchema]
    """

    kwargs = _get_kwargs(
        incident_group_id=incident_group_id,
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
    incident_group_id: int,
    *,
    client: AuthenticatedClient,
    first: int | None | Unset = UNSET,
    last: int | None | Unset = UNSET,
    before: None | str | Unset = UNSET,
    after: None | str | Unset = UNSET,
) -> OpsdutyApiV1IncidentsListIncidentRespondersResponse401 | OpsdutyApiV1IncidentsListIncidentRespondersResponse404 | OpsdutyApiV1IncidentsListIncidentRespondersResponse422 | PagedIncidentGroupResponderSchema | None:
    """List an incident's responders

     List who this incident has reached, and whether they responded.

    Args:
        incident_group_id (int):
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
        OpsdutyApiV1IncidentsListIncidentRespondersResponse401 | OpsdutyApiV1IncidentsListIncidentRespondersResponse404 | OpsdutyApiV1IncidentsListIncidentRespondersResponse422 | PagedIncidentGroupResponderSchema
    """

    return sync_detailed(
        incident_group_id=incident_group_id,
        client=client,
        first=first,
        last=last,
        before=before,
        after=after,
    ).parsed


async def asyncio_detailed(
    incident_group_id: int,
    *,
    client: AuthenticatedClient,
    first: int | None | Unset = UNSET,
    last: int | None | Unset = UNSET,
    before: None | str | Unset = UNSET,
    after: None | str | Unset = UNSET,
) -> Response[OpsdutyApiV1IncidentsListIncidentRespondersResponse401 | OpsdutyApiV1IncidentsListIncidentRespondersResponse404 | OpsdutyApiV1IncidentsListIncidentRespondersResponse422 | PagedIncidentGroupResponderSchema]:
    """List an incident's responders

     List who this incident has reached, and whether they responded.

    Args:
        incident_group_id (int):
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
        Response[OpsdutyApiV1IncidentsListIncidentRespondersResponse401 | OpsdutyApiV1IncidentsListIncidentRespondersResponse404 | OpsdutyApiV1IncidentsListIncidentRespondersResponse422 | PagedIncidentGroupResponderSchema]
    """

    kwargs = _get_kwargs(
        incident_group_id=incident_group_id,
        first=first,
        last=last,
        before=before,
        after=after,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    incident_group_id: int,
    *,
    client: AuthenticatedClient,
    first: int | None | Unset = UNSET,
    last: int | None | Unset = UNSET,
    before: None | str | Unset = UNSET,
    after: None | str | Unset = UNSET,
) -> OpsdutyApiV1IncidentsListIncidentRespondersResponse401 | OpsdutyApiV1IncidentsListIncidentRespondersResponse404 | OpsdutyApiV1IncidentsListIncidentRespondersResponse422 | PagedIncidentGroupResponderSchema | None:
    """List an incident's responders

     List who this incident has reached, and whether they responded.

    Args:
        incident_group_id (int):
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
        OpsdutyApiV1IncidentsListIncidentRespondersResponse401 | OpsdutyApiV1IncidentsListIncidentRespondersResponse404 | OpsdutyApiV1IncidentsListIncidentRespondersResponse422 | PagedIncidentGroupResponderSchema
    """

    return (
        await asyncio_detailed(
            incident_group_id=incident_group_id,
            client=client,
            first=first,
            last=last,
            before=before,
            after=after,
        )
    ).parsed
