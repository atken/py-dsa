from heap_sort import heap_sort


def test_heap_sort_asc():
    a = [1, 3, 2, -1, 2]
    heap_sort(array=a)
    assert a == [-1, 1, 2, 2, 3]

def test_heap_sort_asc_reverse_arg():
    a = [1, 3, 2, -1, 2]
    heap_sort(array=a, reverse=False)
    assert a == [-1, 1, 2, 2, 3]

def test_heap_sort_dsc():
    a = [1, 3, 2, -1, 2]
    heap_sort(array=a, reverse=True)
    assert a == [3, 2, 2, 1, -1]

