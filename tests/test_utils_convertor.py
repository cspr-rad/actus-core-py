import inspect

import isodate

from pyactus.utils import convertor


# Test data.
_INTERVAL_ONE_MONTH = isodate.parse_duration("P1M")
_INTERVAL_ONE_MONTH_ONE_DAY = isodate.parse_duration("P1M1D")


def test_that_convertor_can_be_imported():
    assert inspect.ismodule(convertor)


def test_that_convertor_exposes_conversion_functions():
    for fn in (
        convertor.to_camel_case,
        convertor.to_datetime,
        convertor.to_enum,
        convertor.to_float,
        convertor.to_interest_rate,
        convertor.to_iso_datetime,
        convertor.to_iso_datetime_T00,
        convertor.to_iso_datetime_T24,
        convertor.to_iso_time_interval,
        convertor.to_pascal_case,
        convertor.to_str,
        convertor.to_time_cycle,
        convertor.to_time_period,
        convertor.to_underscore_case
    ):
        assert inspect.isfunction(fn)


def test_conversion_of_a_string():
    for val, expected in (
        (123, "123"),
        (1.123, "1.123"),
        (True, "true")
    ):
        assert convertor.to_str(val) == expected


def test_conversion_of_a_time_period():
    for val, expected in (
        ("P1ML0", _INTERVAL_ONE_MONTH),
        ("P1M1DL0", _INTERVAL_ONE_MONTH_ONE_DAY),
    ):
        assert convertor.to_time_period(val) == expected
