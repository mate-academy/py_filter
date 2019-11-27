"""
docstring
"""
import filter


def test_empty():
    """

    :return:
    """
    assert filter.filter_(lambda x: x%2, []) == []


def test_odd():
    """

    :return:
    """
    assert filter.filter_(lambda x: x%2, [1, 2, 3, 4]) == [1, 3]


def test_string():
    """

    :return:
    """
    assert filter.filter_(lambda x: x in "aouie", "Hello") == ["e", "o"]
