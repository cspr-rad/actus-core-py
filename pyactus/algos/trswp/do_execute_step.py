# ************************************
# N.B. Auto-initialised using actus-mp
# ************************************
import typing

from pyactus.types.core import Event
from pyactus.types.terms import TotalReturnSwapTermset as ContractTermset


def execute_step(events: typing.List[Event], term_set: ContractTermset, observer: object) -> typing.List[Event]:
    """Applies a set of contract events to the current state of a defn.

    :param events: A list of contract events that should be applied in time sequence.
    :param term_set: The contract term set.
    :param observer: The observer for external events & data.
    :returns: The evaluated events and post-event contract states.

    """
    pass
