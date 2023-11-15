import datetime
import typing

from pyactus.types.core.states import StateSpace


# A payoff function executed during the course of event sequence derivation.
FnPayoff = typing.Callable[
    [
        # Time.
        datetime.datetime,
        # States.
        float,
        # Terms.
        float,
        # Risk factor model.
        float,
        # Day counter.
        float,
        # Time adjuster.
        float,
    ],
    StateSpace
]

# A state transition function executed during the course of event sequence derivation.
FnStateTransition = typing.Callable[
    [
        # Time.
        datetime.datetime,
        # States.
        float,
        # Terms.
        float,
        # Risk factor model.
        float,
        # Day counter.
        float,
        # Time adjuster.
        float,
    ],
    StateSpace
]
