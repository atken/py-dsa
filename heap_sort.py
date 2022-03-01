from typing import List


def heap_sort(array: List[int], reverse=False):
    def heapify(hr: int, hs: int):
        # hr: heap root
        # hs: heap size
        minmax = hr 
        left = 2 * hr + 1
        right = 2 * hr + 2
        if reverse == False:
            if left < hs and array[minmax] < array[left]:
                minmax = left
            if right < hs and array[minmax] < array[right]:
                minmax = right
        else:
            if left < hs and array[minmax] > array[left]:
                minmax = left
            if right < hs and array[minmax] > array[right]:
                minmax = right
        if minmax != hr:
            # Change root
            array[hr], array[minmax] = array[minmax], array[hr]
            heapify(minmax, hs)

    n = len(array)
    for i in range(n//2-1, -1, -1):
        heapify(i, n)
    for i in range(n-1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heapify(0, i)

