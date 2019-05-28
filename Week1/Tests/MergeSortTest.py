from Week1.Util import merge_sort
from unittest import *
import unittest

class MergeSorttest(TestCase):

    def MergeSort(self):
        self.result = merge_sort([1, 5, 1, 4, 0, 12, -1]),[-1, 0, 1, 1, 2, 4, 5, 12]
        expected = True
        self.assertTrue(expected. result)

    def MergeSort(self):
        self.result = merge_sort([1, 5, 1, 4, 0, 12, -1])
        expected = [-1, 0, 1, 1, 2, 4, 5]
        self.assertEqual(expected. result)


if __name__ == '__main__':
    unittest.main()

