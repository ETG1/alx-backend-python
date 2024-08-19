#!/usr/bin/env python3
"""
This module contains an asynchronous coroutine that waits for a random
delay between 0 and a specified max_delay and returns the delay value.
"""

import asyncio
import random
from typing import Union

async def wait_random(max_delay: int = 10) -> Union[float, int]:
    """
    Waits for a random delay between 0 and max_delay (inclusive) seconds,
    and returns the duration of the wait.

    Args:
        max_delay (int): The maximum delay in seconds. Default is 10 seconds.

    Returns:
        Union[float, int]: The actual time waited.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

