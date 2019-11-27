"""Module with custom filter function"""
from typing import Callable, Iterable, Any, List


def filter_(func: Callable[[Any], Any], objects: Iterable[Any]) -> List[Any]:
    """
    custom filter function
    :param func: function for filtration
    :param objects: any iterable objects
    :return: result list
    """
    return [x for x in objects if func(x)]
