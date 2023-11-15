import datetime
import typing

from pyactus.types.enums import ContractType
from tests.fixtures.model import ContractTestData


def test_that_test_contracts_can_be_read_from_fsys(test_contracts1: typing.List[ContractTestData]):
    for fixture in test_contracts1:
        assert isinstance(fixture, ContractTestData)
        for name, typeof, is_mandatory in (
            ("contract_id", str, True),
            ("contract_type", ContractType, True),
            ("event_sequence", list, True),
            ("observed_data", dict, False),
            ("observed_events", list, True),
            ("term_set", dict, True),
            ("to_date", datetime.datetime, False)
        ):
            assert hasattr(fixture, name)
            attrval = getattr(fixture, name)
            if is_mandatory or attrval:
                assert isinstance(attrval, typeof)
