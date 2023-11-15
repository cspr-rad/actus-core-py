# **********************************
# N.B. Auto-generated using actus-mp
# **********************************
import dataclasses
import datetime
import typing

from pyactus.types import core
from pyactus.types import enums


@dataclasses.dataclass
class CashTermset(core.ContractTermset):
    """Set of applicable terms: CSH -> Cash.

    Cash or cash equivalent position

    """
    # Contract Identifier.
    contract_id: str = None

    # Contract Role.
    contract_role: enums.ContractRole = None

    # Contract Type :: The ContractType is the most important information. It defines the cash flow generating pattern of a defn. The ContractType information in combination with a given state of the risk factors will produce a deterministic sequence of cash flows which are the basis of any financial analysis.
    contract_type: enums.ContractType = enums.ContractType.CSH

    # Creator Identifier.
    creator_id: str = None

    # Currency.
    currency: str = None

    # Notional Principal.
    notional_principal: float = None

    # Status Date.
    status_date: datetime.datetime = None

