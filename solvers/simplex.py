from input_data import InputData
from result import ResultData
from solvers.base import Solver


class Simplex(Solver):
    name: str = 'Метод симплекса'
    length: float

    def __init__(self, length):
        self.length = length

    def __call__(self, data: InputData) -> ResultData:
        (x, y) = data.initial

        x0 = (x, y)
        x1 = (x + self.length, y)
        x2 = (x, y + self.length)

        xk = [x0, x1, x2]

        f_calls = 3
        path = [x0]
        fk = [data.function(xi[0], xi[1]) for xi in xk]

        while sum([(xk[i][0] - xk[0][0]) ** 2 + (xk[i][1] - xk[0][1]) ** 2 for i in range(1, 3)]) / 2 > data.eps ** 2:

            min_i = min(range(3), key=lambda i: fk[i])
            max_i = max(range(3), key=lambda i: fk[i])

            c_x = 0
            c_y = 0

            for i in range(3):
                if i != max_i:
                    c_x += xk[i][0]
                    c_y += xk[i][1]
            c_x /= 2
            c_y /= 2

            u_k = (2 * c_x - xk[max_i][0], 2 * c_y - xk[max_i][1])
            f_u = data.function(u_k[0], u_k[1])

            if f_u < fk[max_i]:
                xk[max_i] = u_k
                fk[max_i] = f_u
                f_calls += 1
            else:
                for i in range(0, 3):
                    xk[i] = ((xk[i][0] + xk[min_i][0]) / 2, (xk[i][1] + xk[min_i][1]) / 2)
                    fk[i] = data.function(xk[i][0], xk[i][1])
                    f_calls += 2
            path.append(xk[0])

        return ResultData(self.name, xk[0], fk[0], f_calls, 0, path)
