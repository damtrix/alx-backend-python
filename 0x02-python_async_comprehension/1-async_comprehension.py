#!/usr/bin/env python3
'''Returns a genrated list of random numbers'''
import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''list of 10 random numbers from async_generator'''
    return [ran async for ran in async_generator()]
