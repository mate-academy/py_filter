"""
Create your own implementation of filter() function
"""


from typing import Callable, Iterable, Any, List


def filter_(func: Callable[[Any], Any], lst: Iterable[Any]) -> List[Any]:
    """my filter function"""
    return [value for value in lst if func(value)]
