import datetime
from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.opsduty_api_v1_schedules_list_schedule_overrides_response_401 import OpsdutyApiV1SchedulesListScheduleOverridesResponse401
from ...models.opsduty_api_v1_schedules_list_schedule_overrides_response_404 import OpsdutyApiV1SchedulesListScheduleOverridesResponse404
from ...models.opsduty_api_v1_schedules_list_schedule_overrides_response_422 import OpsdutyApiV1SchedulesListScheduleOverridesResponse422
from ...models.paged_schedule_override_schema import PagedScheduleOverrideSchema
from ...types import UNSET, Response, Unset


def _get_kwargs(
    schedule_id: int,
    *,
    since: datetime.datetime | None | Unset = UNSET,
    until: datetime.datetime | None | Unset = UNSET,
    first: int | None | Unset = UNSET,
    last: int | None | Unset = UNSET,
    before: None | str | Unset = UNSET,
    after: None | str | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_since: None | str | Unset
    if isinstance(since, Unset):
        json_since = UNSET
    elif isinstance(since, datetime.datetime):
        json_since = since.isoformat()
    else:
        json_since = since
    params["since"] = json_since

    json_until: None | str | Unset
    if isinstance(until, Unset):
        json_until = UNSET
    elif isinstance(until, datetime.datetime):
        json_until = until.isoformat()
    else:
        json_until = until
    params["until"] = json_until

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
        "url": "/api/v1/schedules/{schedule_id}/overrides/".format(
            schedule_id=quote(str(schedule_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> OpsdutyApiV1SchedulesListScheduleOverridesResponse401 | OpsdutyApiV1SchedulesListScheduleOverridesResponse404 | OpsdutyApiV1SchedulesListScheduleOverridesResponse422 | PagedScheduleOverrideSchema | None:
    if response.status_code == 200:
        response_200 = PagedScheduleOverrideSchema.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = OpsdutyApiV1SchedulesListScheduleOverridesResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = OpsdutyApiV1SchedulesListScheduleOverridesResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = OpsdutyApiV1SchedulesListScheduleOverridesResponse422.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[OpsdutyApiV1SchedulesListScheduleOverridesResponse401 | OpsdutyApiV1SchedulesListScheduleOverridesResponse404 | OpsdutyApiV1SchedulesListScheduleOverridesResponse422 | PagedScheduleOverrideSchema]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    schedule_id: int,
    *,
    client: AuthenticatedClient,
    since: datetime.datetime | None | Unset = UNSET,
    until: datetime.datetime | None | Unset = UNSET,
    first: int | None | Unset = UNSET,
    last: int | None | Unset = UNSET,
    before: None | str | Unset = UNSET,
    after: None | str | Unset = UNSET,
) -> Response[OpsdutyApiV1SchedulesListScheduleOverridesResponse401 | OpsdutyApiV1SchedulesListScheduleOverridesResponse404 | OpsdutyApiV1SchedulesListScheduleOverridesResponse422 | PagedScheduleOverrideSchema]:
    """List schedule overrides

     List the overrides on a schedule, earliest first.

    An override hands a stretch of a rotation to one person, on top of the
    layers. Narrow the list with `since` to drop overrides that already ended,
    and `until` to drop ones that have not started.

    Args:
        schedule_id (int):
        since (datetime.datetime | None | Unset):
        until (datetime.datetime | None | Unset):
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
        Response[OpsdutyApiV1SchedulesListScheduleOverridesResponse401 | OpsdutyApiV1SchedulesListScheduleOverridesResponse404 | OpsdutyApiV1SchedulesListScheduleOverridesResponse422 | PagedScheduleOverrideSchema]
    """

    kwargs = _get_kwargs(
        schedule_id=schedule_id,
        since=since,
        until=until,
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
    schedule_id: int,
    *,
    client: AuthenticatedClient,
    since: datetime.datetime | None | Unset = UNSET,
    until: datetime.datetime | None | Unset = UNSET,
    first: int | None | Unset = UNSET,
    last: int | None | Unset = UNSET,
    before: None | str | Unset = UNSET,
    after: None | str | Unset = UNSET,
) -> OpsdutyApiV1SchedulesListScheduleOverridesResponse401 | OpsdutyApiV1SchedulesListScheduleOverridesResponse404 | OpsdutyApiV1SchedulesListScheduleOverridesResponse422 | PagedScheduleOverrideSchema | None:
    """List schedule overrides

     List the overrides on a schedule, earliest first.

    An override hands a stretch of a rotation to one person, on top of the
    layers. Narrow the list with `since` to drop overrides that already ended,
    and `until` to drop ones that have not started.

    Args:
        schedule_id (int):
        since (datetime.datetime | None | Unset):
        until (datetime.datetime | None | Unset):
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
        OpsdutyApiV1SchedulesListScheduleOverridesResponse401 | OpsdutyApiV1SchedulesListScheduleOverridesResponse404 | OpsdutyApiV1SchedulesListScheduleOverridesResponse422 | PagedScheduleOverrideSchema
    """

    return sync_detailed(
        schedule_id=schedule_id,
        client=client,
        since=since,
        until=until,
        first=first,
        last=last,
        before=before,
        after=after,
    ).parsed


async def asyncio_detailed(
    schedule_id: int,
    *,
    client: AuthenticatedClient,
    since: datetime.datetime | None | Unset = UNSET,
    until: datetime.datetime | None | Unset = UNSET,
    first: int | None | Unset = UNSET,
    last: int | None | Unset = UNSET,
    before: None | str | Unset = UNSET,
    after: None | str | Unset = UNSET,
) -> Response[OpsdutyApiV1SchedulesListScheduleOverridesResponse401 | OpsdutyApiV1SchedulesListScheduleOverridesResponse404 | OpsdutyApiV1SchedulesListScheduleOverridesResponse422 | PagedScheduleOverrideSchema]:
    """List schedule overrides

     List the overrides on a schedule, earliest first.

    An override hands a stretch of a rotation to one person, on top of the
    layers. Narrow the list with `since` to drop overrides that already ended,
    and `until` to drop ones that have not started.

    Args:
        schedule_id (int):
        since (datetime.datetime | None | Unset):
        until (datetime.datetime | None | Unset):
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
        Response[OpsdutyApiV1SchedulesListScheduleOverridesResponse401 | OpsdutyApiV1SchedulesListScheduleOverridesResponse404 | OpsdutyApiV1SchedulesListScheduleOverridesResponse422 | PagedScheduleOverrideSchema]
    """

    kwargs = _get_kwargs(
        schedule_id=schedule_id,
        since=since,
        until=until,
        first=first,
        last=last,
        before=before,
        after=after,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    schedule_id: int,
    *,
    client: AuthenticatedClient,
    since: datetime.datetime | None | Unset = UNSET,
    until: datetime.datetime | None | Unset = UNSET,
    first: int | None | Unset = UNSET,
    last: int | None | Unset = UNSET,
    before: None | str | Unset = UNSET,
    after: None | str | Unset = UNSET,
) -> OpsdutyApiV1SchedulesListScheduleOverridesResponse401 | OpsdutyApiV1SchedulesListScheduleOverridesResponse404 | OpsdutyApiV1SchedulesListScheduleOverridesResponse422 | PagedScheduleOverrideSchema | None:
    """List schedule overrides

     List the overrides on a schedule, earliest first.

    An override hands a stretch of a rotation to one person, on top of the
    layers. Narrow the list with `since` to drop overrides that already ended,
    and `until` to drop ones that have not started.

    Args:
        schedule_id (int):
        since (datetime.datetime | None | Unset):
        until (datetime.datetime | None | Unset):
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
        OpsdutyApiV1SchedulesListScheduleOverridesResponse401 | OpsdutyApiV1SchedulesListScheduleOverridesResponse404 | OpsdutyApiV1SchedulesListScheduleOverridesResponse422 | PagedScheduleOverrideSchema
    """

    return (
        await asyncio_detailed(
            schedule_id=schedule_id,
            client=client,
            since=since,
            until=until,
            first=first,
            last=last,
            before=before,
            after=after,
        )
    ).parsed
