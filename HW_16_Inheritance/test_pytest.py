from task_2_hw16 import Mathematician

m = Mathematician()


def test_square_nums():
    assert m.square_nums([1, 2, -3]) == [1, 4, 9]
    assert m.square_nums([]) == []
    assert m.square_nums([0]) == [0]

def test_remove_positives():
    assert m.remove_positives([-1, 2, 0]) == [2, 0]
    assert m.remove_positives([-0, -2, -1]) == [0]
    assert m.remove_positives([2, 3, 0]) == [2, 3, 0]
    assert m.remove_positives([-9]) == []

def test_filter_leaps():
    assert m.filter_leaps([2001, 1884, 1995, 2003, 2020]) == [1884, 2020]
    assert m.filter_leaps([]) == []
