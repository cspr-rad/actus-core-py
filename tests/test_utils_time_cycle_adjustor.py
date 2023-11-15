import inspect

from pyactus.utils.convertor import to_datetime
from pyactus.utils.time.cycle_adjustor import CycleAdjustorType
from pyactus.utils.time.cycle_adjustor import decrement
from pyactus.utils.time.cycle_adjustor import increment


_FIXTURES = [
    [
        CycleAdjustorType.PERIOD,
        "P1ML0",
        "2020-02-02T02:02:02",
        "2020-01-02T02:02:02",
        "2020-03-02T02:02:02",
    ],
    [
        CycleAdjustorType.PERIOD,
        "P2ML0",
        "2020-02-02T02:02:02",
        "2019-12-02T02:02:02",
        "2020-04-02T02:02:02",
    ],
    [
        CycleAdjustorType.PERIOD,
        "P10DL0",
        "2020-02-02T02:02:02",
        "2020-01-23T02:02:02",
        "2020-02-12T02:02:02",
    ],
    [
        CycleAdjustorType.PERIOD,
        "P1M10DL0",
        "2020-02-02T02:02:02",
        "2019-12-23T02:02:02",
        "2020-03-12T02:02:02",
    ],
    [
        CycleAdjustorType.WEEKDAY,
        "1MonL1",
        "2019-01-01T00:00:00",
        "2018-12-03T00:00:00",
        "2019-02-04T00:00:00",
    ],
]


        # // instantiate adjuster
        # WeekdayCycleAdjuster adjuster = new WeekdayCycleAdjuster("1MonL1");

        # // original and expected shifted time
        # LocalDateTime t0 = LocalDateTime.parse("2019-01-01T00:00:00");
        # LocalDateTime t1 = LocalDateTime.parse("2019-02-04T00:00:00");
        
        # // finally compare expected and generated times
        # assertEquals(t1, adjuster.plusCycle(t0));


def test_that_cycle_adjustor_is_importable():
    assert inspect.isclass(CycleAdjustorType)
    assert inspect.isfunction(decrement)
    assert inspect.isfunction(increment)


def test_that_cycle_adjustor_calculates_adjustment_correctly():
    for adjustment_type, cycle, ts, ts_decremented, ts_incremented in _FIXTURES:
        ts = to_datetime(ts)
        assert decrement(adjustment_type, cycle, ts) == to_datetime(ts_decremented)
        assert increment(adjustment_type, cycle, ts) == to_datetime(ts_incremented)
