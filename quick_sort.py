from typing import List
from random import randint


def quick_sort(array: List[int], reverse=False):
    # Recursive 
    def helper(left: int, right: int) -> bool:
        def partition() -> int:
            i = randint(left, right)
            array[i], array[right] = array[right], array[i]
            i = left
            for j in range(left, right):
                if not reverse and array[j] < array[right]:
                    array[i], array[j] = array[j], array[i]
                    i += 1
                elif reverse and array[j] > array[right]:
                    array[i], array[j] = array[j], array[i]
                    i += 1
            array[i], array[right] = array[right], array[i]
            return i
        
        if left < right:
            p = partition()
            helper(left, p - 1)
            helper(p + 1, right)
    
    helper(0, len(array) - 1)
 

def quick_sort_2(array: List[int], reverse=False):
    # Iterative
    def partition(left: int, right: int) -> int:
        i = randint(left, right)
        array[i], array[right] = array[right], array[i]
        i = left
        for j in range(left, right):
            if not reverse and array[j] < array[right]:
                array[i], array[j] = array[j], array[i]
                i += 1
            elif reverse and array[j] > array[right]:
                array[i], array[j] = array[j], array[i]
                i += 1
        array[i], array[right] = array[right], array[i]
        return i

    stack = []
    stack.append((0, len(array) - 1))

    while len(stack) > 0:
        left, right = stack.pop()
        p = partition(left, right)
        if p - 1 > left:
            stack.append((left, p - 1))
        if p + 1 < right:
            stack.append((p + 1, right))

