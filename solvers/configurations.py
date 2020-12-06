from input_data import InputData
from result import ResultData
from solvers.base import Solver


class ConfigurationsConst(Solver):
    name: str = 'Метод конфигураций (метод Хука и Дживса)'

    h: float
    delta: float
    lambd: float

    def __init__(self, h, delta, l):
        self.h = h
        self.delta = delta
        self.lambd = l

    def __call__(self, data: InputData) -> ResultData:
        (x, y) = data.initial
        h = self.h

        calls_count = 0
        path = [(x, y)]

        while h > self.delta:
            x1 = x
            y1 = y

            f = data.function(x, y)
            if data.function(x + h, y) < f:
                x1 += h
            if data.function(x - h, y) < f:
                x1 -= h

            if data.function(x, y + h) < f:
                y1 += h
            if data.function(x, y - h) < f:
                y1 -= h

            calls_count += 5

            if (x1, y1) == (x, y):
                h /= 2
                continue

            x += self.lambd * (x1 - x)
            y += self.lambd * (y1 - y)
            path.append((x, y))
        return ResultData(self.name, (x, y),data.function(x, y), calls_count, 0, path)
