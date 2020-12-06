from dataclasses import dataclass
from typing import Tuple, List
import os

@dataclass()
class ResultData:
    method:str
    result_point: Tuple[float, float]
    result:float
    f_call_count:int
    df_call_count: int
    path: List[Tuple[float, float]]

    def __str__(self):
        return f'{self.method}{os.linesep} x={self.result_point} y={self.result}, расчётов функции {self.f_call_count} расчётов производных {self.df_call_count} путь {self.path}'
