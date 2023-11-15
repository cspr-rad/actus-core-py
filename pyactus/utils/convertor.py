import datetime
import enum
import re
import typing

import isodate

from pyactus.types.core.time import Cycle
from pyactus.types.core.time import Period
from pyactus.types.core.time import TimePeriod


def to_camel_case(name: str, separator: str = '_') -> str:
    """Converts passed name to camel case.

    :param name: A name as specified in ontology specification.
    :param separator: Separator to use in order to split name into constituent parts.
    :returns: A string converted to camel case.

    """
    r = ''
    if name is not None:
        s = name.split(separator)
        for s in s:
            if (len(s) > 0):
                r += s[0].upper()
                if (len(s) > 1):
                    r += s[1:]
    return r


def to_datetime(val: str) -> datetime.datetime:
    """Converts an arbitrary value into a datetime representation.

    :param val: An arbitrary value being converted.
    :returns: A datetime representation.

    """
    # TODO: refactor using isodate
    _DATETIME_FORMATS = {
        "%Y",
        "%Y-%m-%d",
        "%Y-%m-%d %H:%M",
        "%Y-%m-%d %H:%M:%S",
        "%Y-%m-%d %H:%M:%S",
        "%Y-%m-%dT%H:%M",
        "%Y-%m-%dT%H:%M:%S",
        "%Y-%m-%dT%H:%M:%S"
    }

    if val is None:
        return datetime.datetime.utcnow()

    for format in _DATETIME_FORMATS:
        try:
            val = datetime.datetime.strptime(val, format)
        except BaseException:
            pass
        else:
            return val

    raise ValueError(f"Invalid value: cannot parse to a datetime :: {val}")


def to_enum(val: object, enum_type: type) -> enum.Enum:
    """Converts an arbitrary value into an enumeration member.

    :param val: An arbitrary value being converted.
    :param enum_type: Type of target enum.
    :returns: Pointer to an enum member.

    """
    if isinstance(val, int):
        try:
            return enum_type(val)
        except BaseException:
            raise ValueError(f"Could not parse option ({val}) to an enum ({enum_type})")
    else:
        try:
            return enum_type[str(val)]
        except BaseException:
            try:
                return enum_type[f"_{val}"]
            except BaseException:
                raise ValueError(f"Could not parse value ({val}) to an enum ({enum_type})")


def to_float(val: object) -> float:
    """Converts an arbitrary value into a float representation.

    :param val: An arbitrary value being converted.
    :returns: A float representation.

    """
    try:
        return float(val)
    except ValueError as err:
        raise err


def to_integer(val: object) -> int:
    """Converts an arbitrary value into an integer representation.

    :param val: An arbitrary value being converted.
    :returns: An integer representation.

    """
    try:
        return int(val)
    except ValueError as err:
        raise err


def to_interest_rate(val: str) -> float:
    """Converts passed value to an interest rate.

    :returns: An interest rate.

    """
    return float(val) / 100


def to_iso_datetime(val: str) -> datetime.datetime:
    """Converts passed value to an ISO date time.

    :param val: A character encoded representation of an ISO 3601date time.
    :returns: An ISO compliant datetime.

    """
    return datetime.datetime.fromisoformat(val)


def to_iso_datetime_T00(val: str) -> datetime.datetime:
    """Converts passed value to an ISO date time with time set to 00:00:00.000.

    :param val: A character encoded representation of an ISO 3601 date time.
    :returns: An ISO compliant datetime.

    """
    return to_iso_datetime(val).replace(hour=0, minute=0, second=0, microsecond=0)


def to_iso_datetime_T24(val: str) -> datetime.datetime:
    """Converts passed value to an ISO date time with time set to 23:59:59.000.

    :param val: A character encoded representation of an ISO 3601 date time.
    :returns: An ISO compliant datetime.

    """
    return to_iso_datetime(val).replace(hour=23, minute=59, second=59, microsecond=0)


def to_iso_time_interval(val: str) -> datetime.timedelta:
    """Converts passed value to an ISO time interval.

    :param val: A character encoded representation of an ISO 3601 time interval.
    :returns: An ISO compliant datetime.

    """
    parsed = isodate.parse_duration(val)
    if isinstance(parsed, datetime.timedelta):
        return TimePeriod(parsed.days, 0, 0)

    return TimePeriod(parsed.days, parsed.months, parsed.years)


def to_pascal_case(name: str, separator: str = '_') -> str:
    """Converts passed name to pascal case.

    :param name: A name as specified in ontology specification.
    :param separator: Separator to use in order to split name into constituent parts.
    :returns: A string converted to pascal case.

    """
    r = ''
    s = to_camel_case(name, separator)
    if (len(s) > 0):
        r += s[0].lower()
        if (len(s) > 1):
            r += s[1:]
    return r


def to_str(val: object) -> str:
    """Converts an arbitrary value into a string representation.

    :param val: An arbitrary value being converted.
    :returns: A string representation.

    """
    if isinstance(val, bool):
        return str(val).lower()
    else:
        return str(val)


def to_time_cycle(val: str) -> Cycle:
    """Decodes a domain time cycle from a string representation, e.g. P1ML0.

    """
    val = val.split("L")[0]

    return to_iso_time_interval(val)


def to_time_period(val: str) -> TimePeriod:
    """Decodes a domain time period from a string representation, e.g. P2D.

    """
    val = val.split("L")[0]
    parsed: typing.Union[datetime.timedelta, isodate] = isodate.parse_duration(val)
    if isinstance(parsed, datetime.timedelta):
        return TimePeriod(parsed.days, 0, 0)

    return TimePeriod(parsed.days, parsed.months, parsed.years)


def to_underscore_case(target: str) -> str:
    """Helper function to convert a from camel case string to an underscore case string.

    :param target: A string for conversion.
    :returns: A string converted to underscore case, e.g. account_number.

    """
    if target is None or not len(target):
        return ''

    r = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', target)
    r = re.sub('([a-z0-9])([A-Z])', r'\1_\2', r)
    r = r.lower()

    return r


__all__ = [
    to_camel_case,
    to_datetime,
    to_enum,
    to_float,
    to_interest_rate,
    to_iso_datetime,
    to_iso_datetime_T00,
    to_iso_datetime_T24,
    to_iso_time_interval,
    to_pascal_case,
    to_str,
    to_time_cycle,
    to_time_period,
    to_underscore_case
]
