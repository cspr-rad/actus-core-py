# ************************************
# N.B. Auto-initialised using actus-mp
# ************************************
import datetime
import typing

from pyactus.types.core import Event
from pyactus.types.enums import EventType
from pyactus.types.terms import OptionTermset as ContractTermset


def get_schedule(to_date: datetime.datetime, term_set: ContractTermset) -> typing.List[Event]:
    """Evaluates next contract event sequence within a certain time period.

    The set of contract attributes are mapped to the stream of next contract events
    within a specified time period according to the legal logic of the respective
    Contract Type and contingent to the risk factor dynamics provided with the
    risk factor model.  The contract's status date is used as the reference time
    as from which the code period is evaluated.

    Note, the stream of the next non-contingent contract events matches the portion
    of the stream of the next contingent events up to the first contingent event.
    Furthermore, for a contract with purely non-contingent events
    (e.g. a PrincipalAtMaturity without a RateReset, Scaling, CreditDefault, etc.)
    contingent and non-contingent event streams are the same.

    :param to_date: The time up to which the events are to be evaluated.
    :param term_set: The contract term set.
    :returns: An event sequence upto to_date.

    """
    pass
