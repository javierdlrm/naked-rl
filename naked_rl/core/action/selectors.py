import random

from .action import Action
from ..transition.step import Step
from ..value.estimators import ValueEstimator


def greedy(steps: [Step], actions: [Action], value_estimator: ValueEstimator) -> int:
    estimations = [value_estimator(steps, action) for action in actions]
    return actions[estimations.index(max(estimations))]


def e_greedy(
    steps: [Step], actions: [Action], value_estimator: ValueEstimator, e: float,
) -> int:
    return (
        random.sample(actions, 1)
        if random.uniform(0, 1) < e
        else greedy(steps, actions, value_estimator)
    )
