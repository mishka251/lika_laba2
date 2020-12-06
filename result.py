from dataclasses import dataclass
from typing import Tuple, List


@dataclass()
class ResultData:
    method:str
    result_point: Tuple[float, float]
    result:float
    f_call_count:int
    df_call_count: int
    path: List[Tuple[float, float]]

