from main import add, times


def test_add():
    assert add(2, 3) == 5


def test_add_negative():
    assert add(-1, 1) == 0

def test_times():
    assert times(67, 100) == 6700
