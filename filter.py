"""module docstring"""
#from typing import Callable, Iterable, Any, List
import functools


def filter_(function, listing):
    """docstring"""
    return functools.reduce(lambda x, y: x + [y] if function(y) else x, listing, [])
