"""
module filter
"""
from typing import Callable, Iterable, Any, List


def filter_(func: Callable[[Any], Any], lst: Iterable[Any]) -> List[Any]:
    """
    Implementation of filter() function.
    :param func: Callable[[Any], Any]
    :param lst: Iterable[Any]
    :return: List[Any]
    """
    filter_result_lst = []
    for element in lst:
        if func(element) == element or func(element):
            filter_result_lst.append(element)
    return filter_result_lst
