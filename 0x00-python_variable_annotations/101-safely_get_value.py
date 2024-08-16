#!/usr/bin/env python3
"""
This module provides a function to safely get a value from a dictionary with a default fallback.
"""
from typing import Dict, TypeVar, Optional

K = TypeVar('K')  
V = TypeVar('V') 
T = TypeVar('T', bound=Optional[V])

def safely_get_value(dct: Dict[K, V], key: K, default: T = None) -> T:
    """
    Return the value associated with the key in the dictionary if it exists, otherwise return the default value.

    Args:
        dct (Dict[K, V]): The dictionary to get the value from.
        key (K): The key whose associated value is to be returned.
        default (T, optional): The default value to return if the key is not found. Defaults to None.
    """
    if key in dct:
        return dct[key]
    else:
        return default
