#!/usr/bin/env python3
"""
This module provides a function that creates a multiplier function.
"""

from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Create a multiplier function that multiplies a float by the given multiplier.

    Args:
        multiplier (float): The value to multiply by.
    """
    def multiplier_function(value: float) -> float:
        """
        Multiply the input value by the multiplier.

        Args:
            value (float): The number to be multiplied.
        """
        return value * multiplier

    return multiplier_function
