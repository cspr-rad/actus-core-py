import datetime
import enum

from dateutil.relativedelta import relativedelta

from pyactus.types.core.time import WeekDay
from pyactus.utils import convertor
from pyactus.utils.time import cycle_parser

class CycleAdjustorType(enum.Enum):
    """Enumeration over set of supported cycle adjustors.

    """
    # Adjusts according to ISO 8601 time period.
    PERIOD = 0

    # Adjusts according to weekday time period.
    WEEKDAY = 1


def decrement(
    adjustor_type: CycleAdjustorType,
    cycle: str,
    val: datetime.datetime
) -> datetime.datetime:
    """Returns a negatively adjusted cycle timestamp.

    :param adjustor_type: The type of adjustor in scope.
    :param cycle: A domain time cycle from a string representation, e.g. P1ML0.
    :param val: A datetime value to be adjusted.
    :returns: A negatively adjusted datetime value.

    """
    if adjustor_type == CycleAdjustorType.PERIOD:
        return val - convertor.to_time_period(cycle)

    elif adjustor_type == CycleAdjustorType.WEEKDAY:
        val1 = val + relativedelta(months=-1)
        weekday: WeekDay = cycle_parser.parse_weekday(cycle)
        raise NotImplementedError(f"{val} :: {val1} :: {weekday}")

    else:
        raise ValueError("Invalid cycle adjustor.")


def increment(
    adjustor_type: CycleAdjustorType,
    cycle: str,
    val: datetime.datetime
) -> datetime.datetime:
    """Returns a positively adjusted cycle timestamp.

    :param adjustor_type: The type of adjustor in scope.
    :param cycle: A domain time cycle from a string representation, e.g. P1ML0.
    :param val: A datetime value to be adjusted.
    :returns: A positively adjusted datetime value.

    """
    if adjustor_type == CycleAdjustorType.PERIOD:
        return val + convertor.to_time_period(cycle)

    elif adjustor_type == CycleAdjustorType.WEEKDAY:
        val1 = val + relativedelta(months=1)
        weekday: WeekDay = cycle_parser.parse_weekday(cycle)
        raise NotImplementedError(f"{val} :: {val1} :: {weekday}")

    else:
        raise ValueError("Invalid cycle adjustor.")


__all__ = [
    CycleAdjustorType,
    decrement,
    increment
]
