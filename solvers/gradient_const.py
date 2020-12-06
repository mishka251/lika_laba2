from input_data import InputData
from result import ResultData
from solvers.base import Solver


class GradientSolver(Solver):
    name: str = 'Градиентный метод с постоянным шагом'
    alpha: float

    def __init__(self, alpha):
        self.alpha = alpha

    def __call__(self, data: InputData) -> ResultData:
        (x, y) = data.initial
        path = [(x, y)]

        grad = (data.df_dx1(x, y), data.df_dx2(x, y))
        calls_count = 2

        while (grad[0] * grad[0] + grad[1] * grad[1]) >= data.eps * data.eps:
            (x, y) = (x - self.alpha * grad[0], y - self.alpha * grad[1])
            grad = (data.df_dx1(x, y), data.df_dx2(x, y))
            calls_count += 2
            path.append((x, y))

        return ResultData(self.name, (x, y),data.function(x, y), 0, calls_count, path)
