import filter


def test_empty():
    assert filter.filter_(lambda x: x % 2, []) == []


def test_odd():
    assert filter.filter_(lambda x: x % 2, [1, 2, 3, 4]) == [1, 3]


def test_string():
    assert filter.filter_(lambda x: x in "aouie", "Hello") == ["e", "o"]