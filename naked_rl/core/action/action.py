from dataclasses import dataclass
from abc import abstractmethod


@dataclass
class Action:
    id: int

    @abstractmethod
    def take(self, **kwargs):
        pass
