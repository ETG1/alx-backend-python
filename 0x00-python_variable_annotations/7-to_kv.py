#!/usr/bin/env python3
"""
This module provides a function that returns a tuple with a string and the square of a number.
"""

from typing import Union, Tuple

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Return a tuple with a string and the square of an integer or float.

    Args:
        k (str): The string to be the first element of the tuple.
        v (Union[int, float]): The number to be squared for the second element of the tuple.
    """
    return k, float(v ** 2)
