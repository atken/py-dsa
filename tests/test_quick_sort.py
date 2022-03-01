from quick_sort import quick_sort, quick_sort_2


def test_quick_sort_asc():
    a = [1, 3, 2, -1, 2]
    quick_sort(array=a)
    assert a == [-1, 1, 2, 2, 3]

def test_quick_sort_asc_reverse_arg():
    a = [1, 3, 2, -1, 2]
    quick_sort(array=a, reverse=False)
    assert a == [-1, 1, 2, 2, 3]

def test_quick_sort_dsc():
    a = [1, 3, 2, -1, 2]
    quick_sort(array=a, reverse=True)
    assert a == [3, 2, 2, 1, -1]

def test_quick_sort_2_asc():
    a = [1, 3, 2, -1, 2]
    quick_sort_2(array=a)
    assert a == [-1, 1, 2, 2, 3]

def test_quick_sort_2_asc_reverse_arg():
    a = [1, 3, 2, -1, 2]
    quick_sort_2(array=a, reverse=False)
    assert a == [-1, 1, 2, 2, 3]

def test_quick_sort_2_dsc():
    a = [1, 3, 2, -1, 2]
    quick_sort_2(array=a, reverse=True)
    assert a == [3, 2, 2, 1, -1]

