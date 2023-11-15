import inspect

from pyactus.utils.convertor import to_datetime
from pyactus.utils.time.business_day_calendar import BusinessDayCalendarType
from pyactus.utils.time.business_day_calendar import is_business_day


_FIXTURES = [
    [
        BusinessDayCalendarType.NO_HOLIDAYS,
        "2020-02-02T02:02:02",
        True
    ],
    [
        BusinessDayCalendarType.NO_HOLIDAYS,
        "2020-02-03T02:02:02",
        True
    ],
    [
        BusinessDayCalendarType.MONDAY_TO_FRIDAY,
        "2020-02-02T02:02:02",
        False
    ],
    [
        BusinessDayCalendarType.MONDAY_TO_FRIDAY,
        "2020-02-03T02:02:02",
        True
    ],
]


def test_that_business_day_calendar_is_importable():
    assert inspect.isclass(BusinessDayCalendarType)
    assert inspect.isfunction(is_business_day)


def test_that_business_day_calendar_calculates_is_business_day_correctly():
    for calendar_type, ts, expected in _FIXTURES:
        assert is_business_day(calendar_type, to_datetime(ts)) is expected
