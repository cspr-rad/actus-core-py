# **********************************
# N.B. Auto-generated using actus-mp
# **********************************
import dataclasses
import datetime
import typing

from pyactus.types import core
from pyactus.types import enums


@dataclasses.dataclass
class CollateralTermset(core.ContractTermset):
    """Set of applicable terms: CEC -> Collateral.

    Collateral creates a relationship between a collateral an obligee and a debtor, covering the exposure from the debtor with the collateral.

    """
    # Contract Identifier.
    contract_id: str = None

    # Contract Role.
    contract_role: enums.ContractRole = None

    # Contract Type :: The ContractType is the most important information. It defines the cash flow generating pattern of a defn. The ContractType information in combination with a given state of the risk factors will produce a deterministic sequence of cash flows which are the basis of any financial analysis.
    contract_type: enums.ContractType = enums.ContractType.CEC

    # Business Day Convention.
    business_day_convention: enums.BusinessDayConvention = enums.BusinessDayConvention.NOS

    # Calendar.
    calendar: enums.Calendar = enums.Calendar.NC

    # Contract Deal Date.
    contract_deal_date: datetime.datetime = None

    # Contract Structure.
    contract_structure: typing.List[core.ContractReference] = None

    # Counterparty Identifier.
    counterparty_id: str = None

    # Coverage Of Credit Enhancement.
    coverage_of_credit_enhancement: float = 1.0

    # Creator Identifier.
    creator_id: str = None

    # Credit Event Type Covered.
    credit_event_type_covered: typing.List[enums.CreditEventTypeCovered] = enums.CreditEventTypeCovered.DF

    # End Of Month Convention.
    end_of_month_convention: enums.EndOfMonthConvention = enums.EndOfMonthConvention.SD

    # Exercise Amount.
    exercise_amount: float = None

    # Exercise Date.
    exercise_date: datetime.datetime = None

    # Guaranteed Exposure.
    guaranteed_exposure: enums.GuaranteedExposure = None

    # Settlement Period.
    settlement_period: core.Period = None

    # Status Date.
    status_date: datetime.datetime = None

