import datetime
import sched
import typing

from pyactus.types.core import Event
from pyactus.types.core import FnPayoff
from pyactus.types.core import FnStateTransition
from pyactus.types.enums import EndOfMonthConvention
from pyactus.types.enums import EventType


# LocalDateTime scheduleTime
# LocalDateTime eventTime
# EventType eventType
# String currency
# PayOffFunction payOff
# StateTransitionFunction stateTrans
# String contractID


def create_event(
    contract_id: str,
    convention: bool,
    currency: str,
    event_type: EventType,
    fn_payoff: FnPayoff,
    fn_state_transition: FnStateTransition,
    ts_scheduled: datetime.datetime
) -> Event:
    """Create a contract event.

    :param contract_id: Contract identifier.
    :param convention: Business day convention to be used.
    :param currency: Event currency.
    :param event_type: Event type.
    :param fn_payoff: Event pay-off function.
    :param fn_state_transition: Event state-transition function.
    :param ts_scheduled: Scheduled timestamp for updating event payoff and post-event state.
    :returns: A contract event.

    """
    if convention is None:
        ts_event = ts_scheduled
    else:
        print("TODO: derive ts_event from business day convention")
        ts_event = None

    return Event(
        contract_id=contract_id,
        currency=currency,
        event_type=event_type,
        fn_payoff=fn_payoff,
        fn_state_transition=fn_state_transition,
        ts_event=ts_event,
        ts_scheduled=ts_scheduled
    )


def create_event_sequence(
    contract_id: str,
    convention: bool,
    currency: str,
    event_type: EventType,
    fn_payoff: FnPayoff,
    fn_state_transition: FnStateTransition,
    schedule: typing.List[datetime.datetime]
) -> typing.List[Event]:
    """Create a sequence of contract events from a time schedule shifting the 
    event times according to a business day convention.

    Depending on which schedule parameters are provided, a set of
    dates is generated from (including) startTime to (including)
    endTime with a periodic {cycle} (if provided).

    Parameter {append_end_time} allows for specifying whether or not
    an additional time should be added to the schedule at the schedule {ts_end}.

    :param contract_id: Contract identifier.
    :param convention: Business day convention to be used.
    :param currency: Event currency.
    :param event_type: Event type.
    :param fn_payoff: Event pay-off function.
    :param fn_state_transition: Event state-transition function.
    :param schedule: An unordered set of schedule times.
    :returns: An unordered set of contract events.

    """
    def _map_event(ts_scheduled: datetime.datetime):
        return Event(
            contract_id=contract_id,
            currency=currency,
            event_type=event_type,
            fn_payoff=fn_payoff,
            fn_state_transition=fn_state_transition,
            ts_event=None,
            ts_scheduled=ts_scheduled
        )

    return [_map_event(i) for i in schedule]


def create_schedule(
    ts_start: datetime.datetime,
    ts_end: datetime.datetime,
    cycle: str,
    end_of_month_convention: EndOfMonthConvention,
    append_end_time: bool
) -> typing.List[datetime.datetime]:
    """Create a schedule of dates including or not the schedule end time.

    Depending on which schedule parameters are provided, a set of
    dates is generated from (including) startTime to (including)
    endTime with a periodic {cycle} (if provided).

    Parameter {append_end_time} allows for specifying whether or not
    an additional time should be added to the schedule at the schedule {ts_end}.

    :param ts_start: Start timestamp of the schedule.
    :param ts_end: End timestamp of the schedule.
    :param cycle: the schedule cycle
    :param end_of_month_convention: The convention to be applied in respect of end of month.
    :param append_end_time: Flag indicating whether an additional time be generated at end time.
    :returns: An unordered set of schedule times

    """
    result: typing.List[datetime.datetime] = []

    return [ts_start, ts_end]
