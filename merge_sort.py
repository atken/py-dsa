from typing import List


def merge_sort(array: List[int], reverse=False):
    def helper(left: int, right: int):
        def merge():
            left_len, right_len = mid - left + 1, right - mid
            left_tmp_array, right_tmp_array = [0] * left_len, [0] * right_len
            for i in range(0, left_len):
                left_tmp_array[i] = array[left + i]
            for j in range(0, right_len):
                right_tmp_array[j] = array[mid + 1 + j]
            i, j, k = 0, 0, left
            while i < left_len and j < right_len:
                if not reverse:
                    if left_tmp_array[i] < right_tmp_array[j]:
                        array[k] = left_tmp_array[i]
                        i += 1
                    else:
                        array[k] = right_tmp_array[j]
                        j += 1
                else:
                    if left_tmp_array[i] > right_tmp_array[j]:
                        array[k] = left_tmp_array[i]
                        i += 1
                    else:
                        array[k] = right_tmp_array[j]
                        j += 1
                k += 1
            while i < left_len:
                array[k] = left_tmp_array[i]
                i += 1
                k += 1
            while j < right_len:
                array[k] = right_tmp_array[j]
                j += 1
                k += 1

        if left < right:
            mid = left + (right - left) // 2
            helper(left, mid)
            helper(mid + 1, right)
            merge()
    
    helper(0, len(array) - 1)

