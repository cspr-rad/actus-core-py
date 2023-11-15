import datetime
import enum
import typing


class WeekDay(enum.Enum):
	"""Enumeration over days of the week.  Monday = 1, Tuesday = 2 ...etc.

	"""
	MON = 1
	TUE = 2
	WED = 3
	THU = 4
	FRI = 5
	SAT = 6
	SUN = 7


class CycleStub(enum.Enum):
	"""Enumeration over time cycle stubs.

	"""
	LONG = 0
	SHORT = 1


# Time cycle.
Cycle = typing.NewType("A period of time before/after which a state transition occurs.", datetime.timedelta)

# Time period.
Period = typing.NewType("A period of time before/after which a state transition occurs.", datetime.timedelta)


class TimePeriod():
	"""A period of time associated with a financial contract.
	
	"""
	def __init__(self, days: int, months: int, years: int):
		"""Instance constructor.
		
		"""
		self.days = days
		self.months = months
		self.years = years
