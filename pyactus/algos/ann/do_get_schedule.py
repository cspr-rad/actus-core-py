# ************************************
# N.B. Auto-initialised using actus-mp
# ************************************
import datetime
import typing

from pyactus.algos import funcs
from pyactus.types import factory
from pyactus.types.core import Event
from pyactus.types.enums import EventType
from pyactus.types.enums import InterestCalculationBase
from pyactus.types.terms import AnnuityTermset as ContractTermset
from pyactus.utils.time import cycle_adjustor
from pyactus.utils.time import cycle_parser


def get_schedule(to_date: datetime.datetime, termset: ContractTermset) -> typing.List[Event]:
    """Evaluates next contract event sequence within a certain time period.

    The set of contract attributes are mapped to the stream of next contract events
    within a specified time period according to the legal logic of the respective
    Contract Type and contingent to the risk factor dynamics provided with the
    risk factor model.  The contract's status date is used as the reference time
    as from which the code period is evaluated.

    Note, the stream of the next non-contingent contract events matches the portion
    of the stream of the next contingent events up to the first contingent event.
    Furthermore, for a contract with purely non-contingent events
    (e.g. a PrincipalAtMaturity without a RateReset, Scaling, CreditDefault, etc.)
    contingent and non-contingent event streams are the same.

    :param to_date: The time up to which the events are to be evaluated.
    :param termset: The contract term set.
    :returns: An event sequence upto to_date.

    """
    events: typing.List[Event] = []

    # Maturity date.
    ts_maturity: datetime.datetime = _get_maturity(termset)

    # Initial exchange.
    events.append(factory.create_event(
        contract_id=termset.contract_id,
        convention=None,
        currency=termset.currency,
        event_type=EventType.IED,
        fn_payoff=funcs.POF_IED_PAM,
        fn_state_transition=funcs.STF_IED_LAM,
        ts_scheduled=termset.initial_exchange_date,   
    ))

    # Principal redemption.
    events.append(Event(
        contract_id=termset.contract_id,
        currency=termset.currency,
        event_type=EventType.MD,
        fn_payoff=funcs.POF_MD_PAM,
        fn_state_transition=funcs.STF_MD_LAM,
        ts_scheduled=ts_maturity,        
    ))

    # Principal redemption schedule.
    if termset.interest_calculation_base == InterestCalculationBase.NT:
        fn_state_transition = funcs.STF_PR2_NAM
    else:
        fn_state_transition = funcs.STF_PR_NAM
    factory.create_event_sequence(
        contract_id=termset.contract_id,
        convention=termset.business_day_convention,
        currency=termset.currency,
        event_type=EventType.PR,
        fn_payoff=funcs.POF_PR_NAM,
        fn_state_transition=fn_state_transition,
        schedule=factory.create_schedule(
            ts_start=termset.cycle_anchor_date_of_principal_redemption,
            ts_end=ts_maturity,
            cycle=termset.cycle_of_principal_redemption,
            end_of_month_convention=termset.end_of_month_convention,
            append_end_time=False
        )
    )

    if termset.next_principal_redemption_payment is None:
        events.append(Event(
            contract_id=termset.contract_id,
            currency=termset.currency,
            event_type=EventType.PRF,
            fn_payoff=funcs.POF_RR_PAM,
            fn_state_transition=funcs.STF_PRF_ANN,
            ts_event=termset.business_day_convention,
            ts_scheduled=termset.cycle_anchor_date_of_principal_redemption - datetime.timedelta(days=1),        
        ))

        # // initial principal redemption fixing event (if not already fixed)
        # if(model.getAs("NextPrincipalRedemptionPayment")==null) {
        #     events.add(EventFactory.createEvent(
        #          model.<LocalDateTime>getAs("CycleAnchorDateOfPrincipalRedemption").minusDays(1), 
        #          EventType.PRF, 
        #          model.getAs("Currency"), 
        #          new POF_RR_PAM(),
        #          new STF_PRF_ANN(),
        #         model.getAs("BusinessDayConvention"), 
        #          model.getAs("ContractID")));
        # }

    return events


def _get_maturity(termset: ContractTermset) -> datetime.datetime:
    """Returns contract maturity date.
    
    """
    if termset.maturity_date is not None:
        return termset.maturity_date
    elif termset.amortization_date is not None:
        return termset.amortization_date
    else:
        raise NotImplementedError()
