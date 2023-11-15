import dataclasses
import datetime
import typing

from pyactus.types.enums import ContractType


@dataclasses.dataclass
class ContractTestData():
    """Test data associated with a financial contract.
    
    """
    # Contract Identifier.
    contract_id: str

    # Contract Type :: The ContractType is the most important information. It defines the cash flow generating pattern of a defn. The ContractType information in combination with a given state of the risk factors will produce a deterministic sequence of cash flows which are the basis of any financial analysis.
    contract_type: ContractType

    # The sequence of events emitted by associated contract algorithm.
    event_sequence: typing.List[dict]

    # ???
    observed_data: typing.Optional[dict]

    # ???
    observed_events: typing.List[dict]

    # Contract term set.
    term_set: dict

    # Contract expiration date.
    to_date: typing.Optional[datetime.datetime]
