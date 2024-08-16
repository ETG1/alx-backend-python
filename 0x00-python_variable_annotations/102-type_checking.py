"""
This module provides a function to zoom in on elements of a tuple by repeating them.
"""

from typing import Tuple, List, Union

def zoom_array(lst: Tuple[int, ...], factor: int = 2) -> Tuple[int, ...]:
    """
    Return a tuple with elements from the input tuple repeated by the given factor.

    Args:
        lst (Tuple[int, ...]): A tuple of integers.
        factor (int, optional): The number of times to repeat each element. Defaults to 2.
    """
    zoomed_in: Tuple[int, ...] = tuple(
        item for item in lst
        for _ in range(factor)
    )
    return zoomed_in
