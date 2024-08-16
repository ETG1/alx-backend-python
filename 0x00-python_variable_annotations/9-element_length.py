#!/usr/bin/env python3
"""
This module provides a function that computes the length of each string in a list.
"""

from typing import List, Tuple

def element_length(lst: List[str]) -> List[Tuple[str, int]]:
    """
    Return a list of tuples where each tuple contains a string and its length.

    Args:
        lst (List[str]): A list of strings.
    """
    return [(i, len(i)) for i in lst]
