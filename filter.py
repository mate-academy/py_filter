'''
Module
'''
from typing import Callable, Iterable, Any, List


def filter_(func: Callable[[Any], Any], lst: Iterable[Any]) -> List[Any]:
    '''

    :param func:
    :param lst:
    :return:
    '''
    return list(filter(func, lst))
