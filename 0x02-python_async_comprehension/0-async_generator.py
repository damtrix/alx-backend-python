#!/usr/bin/env python3
'''Task's 0 modules'''
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    '''A coroutine the loop over sleep 10 times'''
    for k in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
