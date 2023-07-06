#!/usr/bin/env python3
'''Task 10's modules'''
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    '''Returnin the value of the first element of a sequence if it exist'''
    if lst:
        return lst[0]
    else:
        return None
