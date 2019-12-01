"""module"""
from typing import Callable, Iterable, Any, List


def filter_(func: Callable[[Any], Any], itrbl: Iterable[Any]) -> List[Any]:
    """filter"""

    return [i for i in itrbl if func(i)]
