#!/usr/bin/env python3
'''Task 6's'''
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''Returns the float sum of a floating-point and integer list of numbers'''
    return float(sum(mxd_lst))
