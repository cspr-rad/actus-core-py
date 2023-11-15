import datetime
import inspect

import pytest

from pyactus.types.core.time import CycleStub
from pyactus.types.core.time import WeekDay
from pyactus.utils.time import cycle_parser as parser


_FIXTURES = [
    "P1ML0",
    "P10DL0",
    "P1M10DL0",
    "1MonL1",
    "1FriL1",
    "3SatL1",   
]


def test_that_parser_is_importable():
    assert inspect.ismodule(parser)
    assert inspect.isfunction(parser.is_period)
    assert inspect.isfunction(parser.parse_period)
    assert inspect.isfunction(parser.parse_position)
    assert inspect.isfunction(parser.parse_stub)
    assert inspect.isfunction(parser.parse_weekday)


def test_that_period_is_correctly_identified():
    for cycle in _FIXTURES[:3]:
        assert parser.is_period(cycle) == True
    for cycle in _FIXTURES[3:]:
        assert parser.is_period(cycle) == False


def test_that_period_is_correctly_parsed():
    for cycle in _FIXTURES[:3]:
        parsed = parser.parse_period(cycle)
        assert isinstance(parsed, datetime.timedelta)


def test_that_position_is_correctly_parsed_1():
    for cycle in _FIXTURES[3:]:
        assert parser.parse_position(cycle) == int(cycle[0])


def test_that_position_is_correctly_parsed_2():
    for cycle in _FIXTURES[:3]:
        with pytest.raises(ValueError):
            parser.parse_position(cycle)


def test_that_stub_is_correctly_parsed_1():
    for cycle in _FIXTURES:
        assert parser.parse_stub(cycle) == CycleStub(int(cycle[-1]))


def test_that_stub_is_correctly_parsed_2():
    for cycle in _FIXTURES:
        cycle = cycle[:-1] + "X"
        with pytest.raises(ValueError):
            parser.parse_stub(cycle)


def test_that_weekday_is_correctly_parsed_1():
    for cycle in _FIXTURES[3:]:
        assert parser.parse_weekday(cycle) in WeekDay


def test_that_weekday_is_correctly_parsed_2():
    with pytest.raises(KeyError):
        parser.parse_weekday("1FrrL1")
