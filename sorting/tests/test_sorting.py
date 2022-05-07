from unittest import TestCase

from main import insertion_sort, merge_sort

arr = list(range(10, 0, -1))


def test_insertion_sorting():
    TestCase().assertListEqual(sorted(arr), insertion_sort(arr))


def test_merge_sorting():
    TestCase().assertListEqual(sorted(arr), merge_sort(arr))
