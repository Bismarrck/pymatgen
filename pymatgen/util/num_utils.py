"""
This module provides utilities for basic math operations.
"""
from __future__ import division, print_function

import itertools
import collections
import numpy as np

def iterator_from_slice(s):
    """
    Constructs an iterator given a slice object s.

    :note: The function returns an infinite iterator if s.stop is None
    """
    start = s.start if s.start is not None else 0
    step  = s.step  if s.step is not None else 1

    if s.stop is None: 
        # Infinite iterator.
        return itertools.count(start=start, step=step)
    else:
        # xrange-like iterator that suppors float.
        return iter(np.arange(start, s.stop, step))

def sort_dict(d, key=None, reverse=False):
    """
    Returns an OrderedDict object whose keys are ordered according to their value.

    Args:
        d:
            Input dictionary
        key: 
            function which takes an tuple (key, object) and returns a value to compare and sort by. 
            By default, the function compares the values of the dict i.e. key = lambda t : t[1]
        reverse: 
            allows to reverse sort order.
    """
    kv_items = [kv for kv in d.items()]

    # Sort kv_items according to key.
    if key is None:
        kv_items.sort(key= lambda t : t[1], reverse=reverse)
    else:
        kv_items.sort(key=key, reverse=reverse)

    # Build ordered dict.
    return collections.OrderedDict(kv_items)
