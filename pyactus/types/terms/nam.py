# **********************************
# N.B. Auto-generated using actus-mp
# **********************************
import dataclasses
import datetime
import typing

from pyactus.types import core
from pyactus.types import enums


@dataclasses.dataclass
class NegativeAmortizerTermset(core.ContractTermset):
    """Set of applicable terms: NAM -> Negative Amortizer.

    Similar as ANN. However when resetting rate, total amount (interest plus principal) stay constant. MD shifts. Only variable rates.

    """
    # Contract Identifier.
    contract_id: str = None

    # Contract Role.
    contract_role: enums.ContractRole = None

    # Contract Type :: The ContractType is the most important information. It defines the cash flow generating pattern of a defn. The ContractType information in combination with a given state of the risk factors will produce a deterministic sequence of cash flows which are the basis of any financial analysis.
    contract_type: enums.ContractType = enums.ContractType.NAM

    # Accrued Interest.
    accrued_interest: float = None

    # Business Day Convention.
    business_day_convention: enums.BusinessDayConvention = enums.BusinessDayConvention.NOS

    # Calendar.
    calendar: enums.Calendar = enums.Calendar.NC

    # Capitalization End Date.
    capitalization_end_date: datetime.datetime = None

    # Contract Deal Date.
    contract_deal_date: datetime.datetime = None

    # Contract Performance.
    contract_performance: enums.ContractPerformance = enums.ContractPerformance.PF

    # Counterparty Identifier.
    counterparty_id: str = None

    # Creator Identifier.
    creator_id: str = None

    # Credit Line Amount.
    credit_line_amount: float = None

    # Currency.
    currency: str = None

    # Cycle Anchor Date Of Fee.
    cycle_anchor_date_of_fee: datetime.datetime = None

    # Cycle Anchor Date Of Interest Calculation Base.
    cycle_anchor_date_of_interest_calculation_base: datetime.datetime = None

    # Cycle Anchor Date Of Interest Payment.
    cycle_anchor_date_of_interest_payment: datetime.datetime = None

    # Cycle Anchor Date Of Optionality.
    cycle_anchor_date_of_optionality: datetime.datetime = None

    # Cycle Anchor Date Of Principal Redemption.
    cycle_anchor_date_of_principal_redemption: datetime.datetime = None

    # Cycle Anchor Date Of Rate Reset.
    cycle_anchor_date_of_rate_reset: datetime.datetime = None

    # Cycle Anchor Date Of Scaling Index.
    cycle_anchor_date_of_scaling_index: datetime.datetime = None

    # Cycle Of Fee.
    cycle_of_fee: core.Cycle = None

    # Cycle Of Interest Calculation Base.
    cycle_of_interest_calculation_base: core.Cycle = None

    # Cycle Of Interest Payment.
    cycle_of_interest_payment: core.Cycle = None

    # Cycle Of Optionality.
    cycle_of_optionality: core.Cycle = None

    # Cycle Of Principal Redemption.
    cycle_of_principal_redemption: core.Cycle = None

    # Cycle Of Rate Reset.
    cycle_of_rate_reset: core.Cycle = None

    # Cycle Of Scaling Index.
    cycle_of_scaling_index: core.Cycle = None

    # Day Count Convention.
    day_count_convention: enums.DayCountConvention = None

    # Delinquency Period.
    delinquency_period: core.Period = None

    # Delinquency Rate.
    delinquency_rate: float = None

    # End Of Month Convention.
    end_of_month_convention: enums.EndOfMonthConvention = enums.EndOfMonthConvention.SD

    # Fee Accrued.
    fee_accrued: float = None

    # Fee Basis.
    fee_basis: enums.FeeBasis = None

    # Fee Rate.
    fee_rate: float = None

    # Fixing Period.
    fixing_period: core.Period = None

    # Grace Period.
    grace_period: core.Period = None

    # Initial Exchange Date.
    initial_exchange_date: datetime.datetime = None

    # Interest Calculation Base.
    interest_calculation_base: enums.InterestCalculationBase = enums.InterestCalculationBase.NT

    # Interest Calculation Base Amount.
    interest_calculation_base_amount: float = None

    # Interest Scaling Multiplier.
    interest_scaling_multiplier: float = 1.0

    # Life Cap.
    life_cap: float = None

    # Life Floor.
    life_floor: float = None

    # Market Object Code.
    market_object_code: str = None

    # Market Object Code Of Rate Reset.
    market_object_code_of_rate_reset: str = None

    # Market Object Code Of Scaling Index.
    market_object_code_of_scaling_index: str = None

    # Market Value Observed.
    market_value_observed: float = None

    # Maturity Date.
    maturity_date: datetime.datetime = None

    # Next Principal Redemption Payment.
    next_principal_redemption_payment: float = None

    # Next Reset Rate.
    next_reset_rate: float = None

    # Nominal Interest Rate.
    nominal_interest_rate: float = None

    # Non Performing Date.
    non_performing_date: datetime.datetime = None

    # Notional Principal.
    notional_principal: float = None

    # Notional Scaling Multiplier.
    notional_scaling_multiplier: float = 1.0

    # Option Exercise End Date.
    option_exercise_end_date: datetime.datetime = None

    # Penalty Rate.
    penalty_rate: float = None

    # Penalty Type.
    penalty_type: enums.PenaltyType = enums.PenaltyType.N

    # Period Cap.
    period_cap: float = None

    # Period Floor.
    period_floor: float = None

    # Premium Discount At IED.
    premium_discount_at_ied: float = None

    # Prepayment Effect.
    prepayment_effect: enums.PrepaymentEffect = enums.PrepaymentEffect.N

    # Prepayment Period.
    prepayment_period: core.Period = None

    # Price At Purchase Date.
    price_at_purchase_date: float = None

    # Price At Termination Date.
    price_at_termination_date: float = None

    # Purchase Date.
    purchase_date: datetime.datetime = None

    # Rate Multiplier.
    rate_multiplier: float = 1.0

    # Rate Spread.
    rate_spread: float = None

    # Scaling Effect.
    scaling_effect: enums.ScalingEffect = enums.ScalingEffect.OOO

    # Scaling Index At Contract Deal Date.
    scaling_index_at_contract_deal_date: float = None

    # Seniority.
    seniority: enums.Seniority = None

    # Settlement Currency.
    settlement_currency: str = None

    # Status Date.
    status_date: datetime.datetime = None

    # Termination Date.
    termination_date: datetime.datetime = None

