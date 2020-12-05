from dataclasses import dataclass
from typing import Tuple
from math import exp


@dataclass
class InputData:
    initial: Tuple[float, float]
    eps: float
    a: float
    b: float
    c: float
    d: float

    # def function(self, x1, x2):
    #     return self.a * x1 * x1 + self.b * x2 * x2
    #
    # def df_dx1(self, x1: float, x2: float) -> float:
    #     return 2 * self.a * x1
    #
    # def df_dx2(self, x1: float, x2: float) -> float:
    #     return 2 * self.b * x2

    def function(self, x1: float, x2: float) -> float:
        return self.a * x1 + self.b * x2 + exp(self.c * x1*x1 + self.d * x2*x2)

    def df_dx1(self, x1: float, x2: float) -> float:
        return self.a * x1 + 2*x1*self.c * exp(self.c * x1 + self.d * x2)

    def df_dx2(self, x1: float, x2: float) -> float:
        return self.b * x2 + 2*x2*self.d * exp(self.c * x1 + self.d * x2)


variant2 = InputData((0, 1), 0.00005, 2, -1.3, 0.04, 0.12)
