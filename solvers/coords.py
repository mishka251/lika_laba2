from input_data import InputData
from result import ResultData
from solvers.base import Solver


class CoordsSolver(Solver):
    name: str = 'Метод покоординатного спуска'
    alpha: float

    def __init__(self, alpha):
        self.alpha = alpha

    def __call__(self, data: InputData) -> ResultData:
        (x, y) = data.initial
        path = [(x, y)]

        dx = data.df_dx1(x, y)
        x1 = x - self.alpha * dx
        dy = data.df_dx2(x1, y)
        y1 = y - self.alpha * dy
        calls_count = 2
        f_calls = 0

        while ((x1 - x) ** 2 + (y1 - y) ** 2) >= data.eps ** 2:
            (x, y) = (x1, y1)
            dx = data.df_dx1(x, y)
            x1 = x - self.alpha * dx
            dy = data.df_dx2(x1, y)
            y1 = y - self.alpha * dy
            calls_count += 2
            path.append((x, y))

        path.append((x1, y1))
        return ResultData(self.name, (x1, y1),data.function(x, y), f_calls, calls_count, path)
