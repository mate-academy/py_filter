"""Own implementation of filter() function"""

from typing import Callable, Iterable, Any, List


def filter_(func: Callable[[Any], Any], iterable: Iterable[Any]) -> List[Any]:
    """General func"""
    return [i for i in iterable if func(i)]
