import datetime
from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.incident_status import IncidentStatus
from ...models.opsduty_api_v1_statuspages_list_status_page_incidents_response_401 import OpsdutyApiV1StatuspagesListStatusPageIncidentsResponse401
from ...models.opsduty_api_v1_statuspages_list_status_page_incidents_response_404 import OpsdutyApiV1StatuspagesListStatusPageIncidentsResponse404
from ...models.opsduty_api_v1_statuspages_list_status_page_incidents_response_422 import OpsdutyApiV1StatuspagesListStatusPageIncidentsResponse422
from ...models.opsduty_api_v1_statuspages_list_status_page_incidents_type_type_0 import OpsdutyApiV1StatuspagesListStatusPageIncidentsTypeType0
from ...models.paged_incident_schema import PagedIncidentSchema
from ...types import UNSET, Response, Unset


def _get_kwargs(
    status_page_id: int,
    *,
    status: list[IncidentStatus] | None | Unset = UNSET,
    type_: None | OpsdutyApiV1StatuspagesListStatusPageIncidentsTypeType0 | Unset = UNSET,
    created_after: datetime.datetime | None | Unset = UNSET,
    created_before: datetime.datetime | None | Unset = UNSET,
    component_id: int | None | Unset = UNSET,
    first: int | None | Unset = UNSET,
    last: int | None | Unset = UNSET,
    before: None | str | Unset = UNSET,
    after: None | str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_status: list[str] | None | Unset
    if isinstance(status, Unset):
        json_status = UNSET
    elif isinstance(status, list):
        json_status = []
        for status_type_0_item_data in status:
            status_type_0_item = status_type_0_item_data.value
            json_status.append(status_type_0_item)

    else:
        json_status = status
    params["status"] = json_status

    json_type_: None | str | Unset
    if isinstance(type_, Unset):
        json_type_ = UNSET
    elif isinstance(type_, OpsdutyApiV1StatuspagesListStatusPageIncidentsTypeType0):
        json_type_ = type_.value
    else:
        json_type_ = type_
    params["type"] = json_type_

    json_created_after: None | str | Unset
    if isinstance(created_after, Unset):
        json_created_after = UNSET
    elif isinstance(created_after, datetime.datetime):
        json_created_after = created_after.isoformat()
    else:
        json_created_after = created_after
    params["created_after"] = json_created_after

    json_created_before: None | str | Unset
    if isinstance(created_before, Unset):
        json_created_before = UNSET
    elif isinstance(created_before, datetime.datetime):
        json_created_before = created_before.isoformat()
    else:
        json_created_before = created_before
    params["created_before"] = json_created_before

    json_component_id: int | None | Unset
    if isinstance(component_id, Unset):
        json_component_id = UNSET
    else:
        json_component_id = component_id
    params["component_id"] = json_component_id

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
        "url": "/api/v1/statuspages/{status_page_id}/incidents/".format(
            status_page_id=quote(str(status_page_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> OpsdutyApiV1StatuspagesListStatusPageIncidentsResponse401 | OpsdutyApiV1StatuspagesListStatusPageIncidentsResponse404 | OpsdutyApiV1StatuspagesListStatusPageIncidentsResponse422 | PagedIncidentSchema | None:
    if response.status_code == 200:
        response_200 = PagedIncidentSchema.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = OpsdutyApiV1StatuspagesListStatusPageIncidentsResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = OpsdutyApiV1StatuspagesListStatusPageIncidentsResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = OpsdutyApiV1StatuspagesListStatusPageIncidentsResponse422.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[OpsdutyApiV1StatuspagesListStatusPageIncidentsResponse401 | OpsdutyApiV1StatuspagesListStatusPageIncidentsResponse404 | OpsdutyApiV1StatuspagesListStatusPageIncidentsResponse422 | PagedIncidentSchema]:
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
    status: list[IncidentStatus] | None | Unset = UNSET,
    type_: None | OpsdutyApiV1StatuspagesListStatusPageIncidentsTypeType0 | Unset = UNSET,
    created_after: datetime.datetime | None | Unset = UNSET,
    created_before: datetime.datetime | None | Unset = UNSET,
    component_id: int | None | Unset = UNSET,
    first: int | None | Unset = UNSET,
    last: int | None | Unset = UNSET,
    before: None | str | Unset = UNSET,
    after: None | str | Unset = UNSET,
) -> Response[OpsdutyApiV1StatuspagesListStatusPageIncidentsResponse401 | OpsdutyApiV1StatuspagesListStatusPageIncidentsResponse404 | OpsdutyApiV1StatuspagesListStatusPageIncidentsResponse422 | PagedIncidentSchema]:
    """List status page incidents

     List the incidents on a status page, newest first, drafts included.

    Narrow the list by status, by planned or unplanned work, by when incidents
    were declared, or to the ones affecting a component.

    Args:
        status_page_id (int):
        status (list[IncidentStatus] | None | Unset): Only incidents in one of these statuses.
        type_ (None | OpsdutyApiV1StatuspagesListStatusPageIncidentsTypeType0 | Unset): Only
            planned work (scheduled, in progress or completed), or only unplanned incidents.
        created_after (datetime.datetime | None | Unset): Only incidents declared at or after this
            time.
        created_before (datetime.datetime | None | Unset): Only incidents declared before this
            time.
        component_id (int | None | Unset): Only incidents affecting this component.
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
        Response[OpsdutyApiV1StatuspagesListStatusPageIncidentsResponse401 | OpsdutyApiV1StatuspagesListStatusPageIncidentsResponse404 | OpsdutyApiV1StatuspagesListStatusPageIncidentsResponse422 | PagedIncidentSchema]
    """

    kwargs = _get_kwargs(
        status_page_id=status_page_id,
        status=status,
        type_=type_,
        created_after=created_after,
        created_before=created_before,
        component_id=component_id,
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
    status_page_id: int,
    *,
    client: AuthenticatedClient,
    status: list[IncidentStatus] | None | Unset = UNSET,
    type_: None | OpsdutyApiV1StatuspagesListStatusPageIncidentsTypeType0 | Unset = UNSET,
    created_after: datetime.datetime | None | Unset = UNSET,
    created_before: datetime.datetime | None | Unset = UNSET,
    component_id: int | None | Unset = UNSET,
    first: int | None | Unset = UNSET,
    last: int | None | Unset = UNSET,
    before: None | str | Unset = UNSET,
    after: None | str | Unset = UNSET,
) -> OpsdutyApiV1StatuspagesListStatusPageIncidentsResponse401 | OpsdutyApiV1StatuspagesListStatusPageIncidentsResponse404 | OpsdutyApiV1StatuspagesListStatusPageIncidentsResponse422 | PagedIncidentSchema | None:
    """List status page incidents

     List the incidents on a status page, newest first, drafts included.

    Narrow the list by status, by planned or unplanned work, by when incidents
    were declared, or to the ones affecting a component.

    Args:
        status_page_id (int):
        status (list[IncidentStatus] | None | Unset): Only incidents in one of these statuses.
        type_ (None | OpsdutyApiV1StatuspagesListStatusPageIncidentsTypeType0 | Unset): Only
            planned work (scheduled, in progress or completed), or only unplanned incidents.
        created_after (datetime.datetime | None | Unset): Only incidents declared at or after this
            time.
        created_before (datetime.datetime | None | Unset): Only incidents declared before this
            time.
        component_id (int | None | Unset): Only incidents affecting this component.
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
        OpsdutyApiV1StatuspagesListStatusPageIncidentsResponse401 | OpsdutyApiV1StatuspagesListStatusPageIncidentsResponse404 | OpsdutyApiV1StatuspagesListStatusPageIncidentsResponse422 | PagedIncidentSchema
    """

    return sync_detailed(
        status_page_id=status_page_id,
        client=client,
        status=status,
        type_=type_,
        created_after=created_after,
        created_before=created_before,
        component_id=component_id,
        first=first,
        last=last,
        before=before,
        after=after,
    ).parsed


async def asyncio_detailed(
    status_page_id: int,
    *,
    client: AuthenticatedClient,
    status: list[IncidentStatus] | None | Unset = UNSET,
    type_: None | OpsdutyApiV1StatuspagesListStatusPageIncidentsTypeType0 | Unset = UNSET,
    created_after: datetime.datetime | None | Unset = UNSET,
    created_before: datetime.datetime | None | Unset = UNSET,
    component_id: int | None | Unset = UNSET,
    first: int | None | Unset = UNSET,
    last: int | None | Unset = UNSET,
    before: None | str | Unset = UNSET,
    after: None | str | Unset = UNSET,
) -> Response[OpsdutyApiV1StatuspagesListStatusPageIncidentsResponse401 | OpsdutyApiV1StatuspagesListStatusPageIncidentsResponse404 | OpsdutyApiV1StatuspagesListStatusPageIncidentsResponse422 | PagedIncidentSchema]:
    """List status page incidents

     List the incidents on a status page, newest first, drafts included.

    Narrow the list by status, by planned or unplanned work, by when incidents
    were declared, or to the ones affecting a component.

    Args:
        status_page_id (int):
        status (list[IncidentStatus] | None | Unset): Only incidents in one of these statuses.
        type_ (None | OpsdutyApiV1StatuspagesListStatusPageIncidentsTypeType0 | Unset): Only
            planned work (scheduled, in progress or completed), or only unplanned incidents.
        created_after (datetime.datetime | None | Unset): Only incidents declared at or after this
            time.
        created_before (datetime.datetime | None | Unset): Only incidents declared before this
            time.
        component_id (int | None | Unset): Only incidents affecting this component.
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
        Response[OpsdutyApiV1StatuspagesListStatusPageIncidentsResponse401 | OpsdutyApiV1StatuspagesListStatusPageIncidentsResponse404 | OpsdutyApiV1StatuspagesListStatusPageIncidentsResponse422 | PagedIncidentSchema]
    """

    kwargs = _get_kwargs(
        status_page_id=status_page_id,
        status=status,
        type_=type_,
        created_after=created_after,
        created_before=created_before,
        component_id=component_id,
        first=first,
        last=last,
        before=before,
        after=after,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    status_page_id: int,
    *,
    client: AuthenticatedClient,
    status: list[IncidentStatus] | None | Unset = UNSET,
    type_: None | OpsdutyApiV1StatuspagesListStatusPageIncidentsTypeType0 | Unset = UNSET,
    created_after: datetime.datetime | None | Unset = UNSET,
    created_before: datetime.datetime | None | Unset = UNSET,
    component_id: int | None | Unset = UNSET,
    first: int | None | Unset = UNSET,
    last: int | None | Unset = UNSET,
    before: None | str | Unset = UNSET,
    after: None | str | Unset = UNSET,
) -> OpsdutyApiV1StatuspagesListStatusPageIncidentsResponse401 | OpsdutyApiV1StatuspagesListStatusPageIncidentsResponse404 | OpsdutyApiV1StatuspagesListStatusPageIncidentsResponse422 | PagedIncidentSchema | None:
    """List status page incidents

     List the incidents on a status page, newest first, drafts included.

    Narrow the list by status, by planned or unplanned work, by when incidents
    were declared, or to the ones affecting a component.

    Args:
        status_page_id (int):
        status (list[IncidentStatus] | None | Unset): Only incidents in one of these statuses.
        type_ (None | OpsdutyApiV1StatuspagesListStatusPageIncidentsTypeType0 | Unset): Only
            planned work (scheduled, in progress or completed), or only unplanned incidents.
        created_after (datetime.datetime | None | Unset): Only incidents declared at or after this
            time.
        created_before (datetime.datetime | None | Unset): Only incidents declared before this
            time.
        component_id (int | None | Unset): Only incidents affecting this component.
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
        OpsdutyApiV1StatuspagesListStatusPageIncidentsResponse401 | OpsdutyApiV1StatuspagesListStatusPageIncidentsResponse404 | OpsdutyApiV1StatuspagesListStatusPageIncidentsResponse422 | PagedIncidentSchema
    """

    return (
        await asyncio_detailed(
            status_page_id=status_page_id,
            client=client,
            status=status,
            type_=type_,
            created_after=created_after,
            created_before=created_before,
            component_id=component_id,
            first=first,
            last=last,
            before=before,
            after=after,
        )
    ).parsed
