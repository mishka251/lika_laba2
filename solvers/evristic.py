from input_data import InputData
from result import ResultData
from solvers.base import Solver


class Evristic(Solver):
    name: str = 'Эвристические алгоритмы'
    alpha1: float
    alpha2: float
    delta1: float = 1e-3
    delta2: float = 1e2

    def __init__(self, alpha1, alpha2):
        self.alpha1 = alpha1
        self.alpha2 = alpha2

    def __call__(self, data: InputData) -> ResultData:
        (x, y) = data.initial
        path = [(x, y)]

        grad = (data.df_dx1(x, y), data.df_dx2(x, y))
        g = (grad[0] if abs(grad[0]) > self.delta1 else 0, grad[1] if abs(grad[1]) > self.delta1 else 0)
        calls_count = 2

        while True:
            (x_k, y_k) = (x, y)

            while any([gr != 0 for gr in g]):
                (x, y) = (x - self.alpha1 * g[0], y - self.alpha1 * g[1])
                grad = (data.df_dx1(x, y), data.df_dx2(x, y))
                g = (grad[0] if abs(grad[0]) > self.delta1 else 0, grad[1] if abs(grad[1]) > self.delta1 else 0)
                calls_count += 2
                path.append((x, y))

            grad = (data.df_dx1(x, y), data.df_dx2(x, y))
            g = (grad[0] if abs(grad[0]) < self.delta2 else 0, grad[1] if abs(grad[1]) < self.delta2 else 0)
            calls_count += 2
            while any([gr != 0 for gr in g]):
                (x, y) = (x - self.alpha2 * g[0], y - self.alpha2 * g[1])
                grad = (data.df_dx1(x, y), data.df_dx2(x, y))
                g = (grad[0] if abs(grad[0]) < self.delta2 else 0, grad[1] if abs(grad[1]) < self.delta2 else 0)
                calls_count += 2
                path.append((x, y))

            if (x - x_k) ** 2 + (y - y_k) ** 2 <= data.eps ** 2 and (grad[0] ** 2 + grad[1] ** 2) <= data.eps ** 2:
                break

        return ResultData(self.name, (x, y),data.function(x, y), 0, calls_count, path)
