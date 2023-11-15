import datetime
import enum


# Weekday ordinals mapped to literal. 
_SATURDAY: int = 6
_SUNDAY: int = 7


class BusinessDayCalendarType(enum.Enum):
    """Enumeration over set of supported business day calendars.

    """
    # Standard monday to friday business days.
    MONDAY_TO_FRIDAY = 0

    # All days are business days.
    NO_HOLIDAYS = 1


def is_business_day(calendar_type: BusinessDayCalendarType, ts: datetime.datetime) -> bool:
    """Returns flag indicating whether a date maps to a business day.
    
    :param ts: An arbitrary timestamp to be mapped to a business day.
    :param calendar_type: The type of business day calendar in scope.
    :returns: True if considered a business day, false otherwose.

    """
    if calendar_type == BusinessDayCalendarType.MONDAY_TO_FRIDAY:
        return ts.isoweekday() not in {_SATURDAY, _SUNDAY}
    elif calendar_type == BusinessDayCalendarType.NO_HOLIDAYS:
        return True
    else:
        raise ValueError(f"Invalid business day calendar type: {calendar_type}.")


__all__ = [
    BusinessDayCalendarType,
    is_business_day
]
