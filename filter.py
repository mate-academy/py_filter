"""
filter
"""
from typing import Callable, Iterable, Any, List


def filter_(
        func: Callable[[Any], Any], list_to_filter: Iterable[Any]
) -> List[Any]:
    """

    :param func: callback
    :param list_to_filter: list
    :return: filtered list
    """
    result = []
    for item in list_to_filter:
        if func(item):
            result.append(item)
    return result
