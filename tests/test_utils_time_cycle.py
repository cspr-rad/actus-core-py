import datetime

import pytest

from pyactus.utils.time import cycle_parser as parser


def test_that_is_period_returns_true():
	assert parser.is_period("P1ML1") == True


def test_that_is_period_returns_false():
	assert parser.is_period("1FriL1") == False


def test_that_parse_period_returns_1M():
	parsed: datetime.timedelta = parser.parse_period("P1ML1")
	assert parsed.months == 1

	print(parsed)

	raise ValueError()


def test_that_parse_period_returns_2W():
	parsed: datetime.timedelta = parser.parse_period("P2WL1")
	assert parsed.days == 14


def test_that_parse_period_returns_10Y():
	parsed: datetime.timedelta = parser.parse_period("P10YL1")
	assert parsed.years == 10


def test_that_parse_period_throws_1():
	with pytest.raises(ValueError):
		parser.parse_period("P1XL1")


def test_that_parse_period_throws_2():
	with pytest.raises(ValueError):
		parser.parse_period("0.5ML1")


def test_that_parse_position_returns_1():
	assert parser.parse_position("1FriL1") == 1


def test_that_parse_position_returns_4():
	assert parser.parse_position("4MonL1") == 4
