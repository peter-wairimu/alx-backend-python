#!/usr/bin/env python3
'''
Asynchronous coroutine that takes in an integer argument max_delay
waits for a random delay between 0 and max_delay
seconds and eventually returns it.
'''


import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ wait for a ramdom time and returns the waiting time"""
    wait = max_delay * random.random()
    await asyncio.sleep(wait)
    return wait
