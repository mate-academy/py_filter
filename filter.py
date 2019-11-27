"""doc-string"""
from typing import Callable, Iterable, Any, List


def filter_(func: Callable[[Any], Any], iterable: Iterable[Any]) -> List[Any]:
    """
    Returns list of elements from iterable,
    for which func returns True
    :param func: Callable
    :param iterable: Iterable[Any]
    :return: List[Any]
    """
    return [item for item in iterable if func(item)]
