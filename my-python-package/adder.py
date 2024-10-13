import numpy as np
from numbers import Number
from typing import Union

def adder(a: Union[np.ndarray, Number], b: Union[np.ndarray, Number]) -> Union[np.ndarray, Number]:
    return a + b