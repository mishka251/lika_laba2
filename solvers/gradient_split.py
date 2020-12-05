from input_data import InputData
from result import ResultData
from solvers.base import Solver


class GradientSplitSolver(Solver):
    name: str = 'Градиентный метод с дроблением шага'
    alpha: float
    delta: float

    def __init__(self, alpha, delta=0.5):
        self.alpha = alpha
        self.delta = delta

    def __call__(self, data: InputData) -> ResultData:
        (x, y) = data.initial
        path = [(x, y)]

        grad = (data.df_dx1(x, y), data.df_dx2(x, y))
        calls_count = 2
        f_calls = 0

        while (grad[0] ** 2 + grad[1] ** 2) >= data.eps ** 2:

            (t_x, t_y) = (x - self.alpha * grad[0], y - self.alpha * grad[1])
            f_calls += 2
            if data.function(t_x, t_y) > data.function(x, y)-self.delta * self.alpha * (grad[0] ** 2 + grad[1] ** 2):
                self.alpha *= self.delta
                continue

            (x, y) = (t_x, t_y)
            grad = (data.df_dx1(x, y), data.df_dx2(x, y))
            calls_count += 2
            path.append((x, y))

        return ResultData(self.name, (x, y), f_calls, calls_count, path)
