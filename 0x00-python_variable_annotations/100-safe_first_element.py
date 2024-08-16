#!/usr/bin/env python3
"""
This module provides a function to safely retrieve the first element of a list.
"""

from typing import List, Optional, Any

def safe_first_element(lst: List[Any]) -> Optional[Any]:
    """
    Return the first element of a list if it is not empty, otherwise return None.

    Args:
        lst (List[Any]): A list of elements of any type.
    """
    if lst:
        return lst[0]
    else:
        return None
