from typing import Protocol
from ..transition.step import Step
from ..action.action import Action


class ValueEstimator(Protocol):
    def __call__(self, steps: [Step], action: Action) -> float:
        ...


def sample_average(steps: [Step], action: Action) -> float:
    num, den = zip(
        *[
            (step.reward * (step.action == action.id), step.action == action.id)
            for step in steps
        ]
    )
    return sum(num) / sum(den)
