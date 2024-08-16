#!/usr/bin/env python3
"""
This module provides a function to return the sum of a list of floating-point numbers.
"""

from typing import List

def sum_list(input_list: List[float]) -> float:
    """
    Return the sum of a list of floating-point numbers.

    Args:
        input_list (List[float]): A list of floating-point numbers.
    """
    return sum(input_list)
