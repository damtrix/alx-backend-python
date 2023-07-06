#!/usr/bin/env python3
'''Task 11's module'''
from typing import Any, Mapping, Union, TypeVar


T = TypeVar('T')
Ret = Union[Any, T]
DefNone = Union[T, None]


def safely_get_value(dct: Mapping, key: Any, default: DefNone = None) -> Ret:
    '''Returns a value from a dict using a given key.
    '''
    if key in dct:
        return dct[key]
    else:
        return default
