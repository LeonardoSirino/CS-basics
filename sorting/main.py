from typing import List


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


if __name__ == '__main__':
    arr = list(range(10, 0, -1))

    print(merge_sort(arr))
