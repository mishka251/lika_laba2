from abc import ABC

from input_data import InputData
from result import ResultData


class Solver(ABC):
    name:str=None
    def __call__(self, data:InputData)->ResultData:
        pass