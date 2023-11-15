import dataclasses
import datetime
import typing

from pyactus.types.enums import EventType
from pyactus.types.core.funcs import FnPayoff
from pyactus.types.core.funcs import FnStateTransition
from pyactus.types.core.states import StateSpace


@dataclasses.dataclass
class Event():
    """Represent a single event generated during the lifetime of a contract.  Such events
    represent the atomic analytical elements comprising all events that possibly
    occur during the lifetime of a contract.  That is, contract events mark specific
    times at which either a state transition, a payoff, or both is generated from a contract.

    Contract events are a generic representation of a specific state transition function and
    pay off function with an event time according to which all events in a contract are ordered
    (in an series) and processed sequentially.  Thereby, processing an event in fact means that 
    it's state transition and payoff functions are evaluated.

    """
    # The Contract ID of the contract which created the event.
    contract_id: str = None

    # The currency in which the event payoff is scheduled.
    currency: str = None

    # Time offset within context of an epoch.
    epoch_offset: float = None

    # The type of the event. Different types have their own business logic in terms of payoff and state transition functions.
    event_type: EventType = None

    # The event state-transition function.
    fn_state_transition: FnStateTransition = None

    # The event pay-off function.
    fn_payoff: FnPayoff = None

    # The event payoff (if any). Is zero if no payoff needs be settled for the event.
    payoff: float = None

    # The actual timestamp at which event occurred.
    ts_event: datetime.datetime = datetime.datetime.utcnow()

    # The scheduled timestamp for updating event payoff and post-event state.
    ts_scheduled: datetime.datetime = None

    # The post-event state. Results from applying the event’s state transition function to the pre-event state. 
    state: StateSpace = None
