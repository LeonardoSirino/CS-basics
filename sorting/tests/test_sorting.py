from unittest import TestCase

import numpy as np
from main import insertion_sort, merge_sort, quick_sort

arr = list(range(10, 0, -1))

arr = list(np.random.random(20))


def test_insertion_sorting():
    TestCase().assertListEqual(sorted(arr), insertion_sort(arr))


def test_merge_sorting():
    TestCase().assertListEqual(sorted(arr), merge_sort(arr))


def test_quick_sorting():
    TestCase().assertListEqual(sorted(arr), quick_sort(arr))
