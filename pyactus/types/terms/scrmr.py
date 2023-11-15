# **********************************
# N.B. Auto-generated using actus-mp
# **********************************
import dataclasses
import datetime
import typing

from pyactus.types import core
from pyactus.types import enums


@dataclasses.dataclass
class SecuritizationMarketRiskTermset(core.ContractTermset):
    """Set of applicable terms: SCRMR -> Securitization Market Risk.

    Securitiazion contracts where all underlying contracts are treated equal. The buyer of a tranche gets a part of the cash-flows.

    """
    # Contract Identifier.
    contract_id: str = None

    # Contract Role.
    contract_role: enums.ContractRole = None

    # Contract Type :: The ContractType is the most important information. It defines the cash flow generating pattern of a defn. The ContractType information in combination with a given state of the risk factors will produce a deterministic sequence of cash flows which are the basis of any financial analysis.
    contract_type: enums.ContractType = enums.ContractType.SCRMR

    # WARNING:: This contract type has not yet been formally defined.  This class is thus simply a placeholder.
    # raise NotImplementedError("WARNING: Standard does not yet support this contract type.")
