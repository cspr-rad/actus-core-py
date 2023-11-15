import datetime
import typing

from pyactus import algos
from pyactus import codecs
from pyactus.types.core import ContractTermset
from pyactus.types.core import Event
from pyactus.types.enums import ContractType
from tests.fixtures.model import ContractTestData


def test_that_a_contract_event_sequence_is_correctly_calculated(test_contracts1: typing.List[ContractTestData]):
    for fixture in test_contracts1:
        if fixture.contract_type != ContractType.ANN:
            continue

        to_date: datetime.datetime = fixture.to_date
        term_set: ContractTermset = \
            codecs.decode(ContractTermset, fixture.term_set, codecs.EncodingType.DICTIONARY)
        event_sequence_expected: typing.List[Event] = \
            codecs.decode(Event, fixture.event_sequence, codecs.EncodingType.DICTIONARY)

        # for i in algos.get_schedule(to_date, term_set):
        #     print(i)  

        assert algos.get_schedule(to_date, term_set) == event_sequence_expected

    raise ValueError()
