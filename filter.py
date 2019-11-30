"""Create your own implementation of filter() function."""
from typing import Callable, Iterable, Any, List


def filter_(func: Callable[[Any], Any], array: Iterable[Any]) -> List[Any]:
    """Filter function custom realization"""
    return [elem for elem in array if func(elem) == elem or func(elem)]
