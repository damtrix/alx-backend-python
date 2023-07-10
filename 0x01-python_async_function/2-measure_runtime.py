#!/usr/bin/env python3
'''Task's 2 module'''
import asyncio
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    '''Return that is used to compute the concurrent_coroutines'''
    starting_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    ending_time_for_each = (time.time() - starting_time) / n
    return ending_time_for_each
