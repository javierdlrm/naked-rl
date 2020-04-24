from dataclasses import dataclass
from .step import Step


@dataclass
class Run:
    steps: [Step]
