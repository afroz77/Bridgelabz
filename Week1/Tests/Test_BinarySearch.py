from Week1.Algorithm import BinarySearch
import unittest
from unittest import TestProgram

class TestBinarysearch(TestProgram):

    def test_binarysearch_program(self):
        self.runTests()

    # def binary_search_with_possitive_num(self):
    #     result = binarysearch(0, 5, 5, [10, 20, 5, 45, 1, 7])
    #     expected = True
    #     self.assertTrue(expected, result)


if __name__ == '__main__':
    unittest.main()