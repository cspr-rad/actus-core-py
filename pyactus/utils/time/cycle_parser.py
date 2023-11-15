from pyactus.types.core.time import CycleStub
from pyactus.types.core.time import Period
from pyactus.types.core.time import WeekDay
from pyactus.utils import convertor


def is_period(cycle: str) -> bool:
    """Returns flag indicating whether cycle declaration maps to a time period.
    
    :param cycle: A domain time cycle from a string representation, e.g. P1ML0.
    :returns: True if it represents a time period, false otherwise.
    
    """
    return len(cycle) > 0 and cycle[0] == "P"


def parse_period(cycle: str) -> Period:
    """Parses the character sequence following an 'L' in a cycle.

    :param cycle: A domain time cycle from a string representation, e.g. P1ML0.
    :returns: Parsed weekday.
    
    """
    return convertor.to_time_period(cycle)


def parse_position(cycle: str) -> int:
    """Parses character sequence prefixing a cycle declaration.

    :param cycle: A domain time cycle from a string representation, e.g. 1FriL1.
    :returns: Parsed weekday.
    
    """
    raw: str = cycle[0]

    return convertor.to_integer(raw)


def parse_stub(cycle: str) -> CycleStub:
    """Parses character sequence following an 'L' in a cycle declaration.

    :param cycle: A domain time cycle from a string representation, e.g. P1ML0.
    :returns: Parsed stub.
    
    """
    raw: int = int(cycle.split("L")[1][0])
    try:
        return CycleStub(raw)
    except:
        raise ValueError(raw)


def parse_weekday(cycle: str) -> int:
    """Parses the weekday preceding an 'L' in a cycle.

    :param cycle: A domain time cycle from a string representation, e.g. 1MonL1.
    :returns: Parsed weekday.
    
    """
    return WeekDay[cycle.split("L")[0][1:].upper()]


__all__ = [
    is_period,
    parse_period,
    parse_position,
    parse_stub,
    parse_weekday,
]
