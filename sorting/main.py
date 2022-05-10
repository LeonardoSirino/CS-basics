from typing import List, Optional

import numpy as np


def insertion_sort(arr: List[int]) -> List[int]:
    for s in range(len(arr)):
        x = arr[s]

        for k, value in enumerate(arr[:s]):
            if x < value:
                del arr[s]
                arr.insert(k, x)
                break

    return arr


def merge_sort(arr: List[int]) -> List[int]:
    if len(arr) == 1:
        return arr

    h = len(arr) // 2
    L = merge_sort(arr[:h])
    R = merge_sort(arr[h:])

    s_arr = []
    while L or R:
        if not L or R[-1] > L[-1]:
            s_arr.append(R.pop())
        elif not R or L[-1] > R[-1]:
            s_arr.append(L.pop())
        else:
            # NOTE both sub parts has elements and current position
            # has the same value for both parts. This is necessary to make
            # to make the algorithm stable
            s_arr.append(R.pop())

    return s_arr[::-1]


def partition(arr: List[int], init: int, end: int) -> int:
    pivot = arr[end]

    pi = end
    i = init

    while i < pi:
        value = arr[i]
        if value > pivot:
            arr[pi], arr[pi-1] = arr[pi-1], arr[pi]
            if pi-1 != i:
                arr[i], arr[pi] = arr[pi], arr[i]

            pi -= 1
        else:
            i += 1

    return pi


def quick_sort(arr: List[int], init: Optional[int] = None, end: Optional[int] = None) -> List[int]:
    if init is None or end is None:
        init = 0
        end = len(arr) - 1

    if end <= init:
        return []

    pi = partition(arr, init, end)

    quick_sort(arr, init, pi-1)
    quick_sort(arr, pi+1, end)

    return arr


if __name__ == '__main__':
    # arr = list(range(10, 0, -1))
    arr = list(np.random.random(10))

    print(arr)
    print(quick_sort(arr))
