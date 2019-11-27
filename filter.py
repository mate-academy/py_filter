"""imports"""
from typing import Callable, Iterable, Any, List


def filter_(func: Callable[[Any], Any], lst: Iterable[Any]) -> List[Any]:
    """filter"""
    return [el for el in lst if func(el)]
