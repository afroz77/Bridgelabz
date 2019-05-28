from Week1.Algorithm import BinarySearch
import unittest
from unittest import TestCase


class TestBinarysearch(TestCase):

    def binary_search_with_possitive_num(self):
        result = BinarySearch(0, 5, 5, [10, 20, 5, 45, 1, 7])
        expected = 1
        self.assertEqual(expected, result)


if __name__ == '__main__':

    unittest.main()