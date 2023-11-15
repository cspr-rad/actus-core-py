import typing

from pyactus import codecs
from pyactus.types.core import Event
from pyactus.types.core import ContractTermset
from pyactus.types.terms import CONTRACT_TERMSETS
from tests.fixtures.model import ContractTestData


def test_that_contract_termsets_can_be_decoded_from_a_dictionary(test_contracts1: typing.List[ContractTestData]):
    for fixture in test_contracts1:
        encoded: dict = fixture.term_set
        decoded: ContractTermset = codecs.decode(ContractTermset, encoded, codecs.EncodingType.DICTIONARY)
        assert isinstance(decoded, CONTRACT_TERMSETS[fixture.contract_type])


def test_that_event_sequences_can_be_decoded_from_a_dictionary(test_contracts1: typing.List[ContractTestData]):
    for fixture in test_contracts1:
        encoded: typing.List[dict] = fixture.event_sequence
        decoded: typing.List[Event] = codecs.decode(Event, encoded, codecs.EncodingType.DICTIONARY)
        assert isinstance(decoded, list)
        assert len(decoded) == len(encoded)
        for item in decoded:
            assert isinstance(item, Event)
