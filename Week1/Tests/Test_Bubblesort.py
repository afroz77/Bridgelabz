import Week1.Algorithm.BubbleSort
from Week1.Util import bubble_sort
import unittest
from unittest import TestCase


class Test_Bubblesort_Program(TestCase):

    def test_bubblesort_with_possitive_array(self):
        result = bubble_sort([12, 1, 0, 5, 4, 2])
        expected = [0, 1, 2, 4, 5, 12]
        self.assertEqual(expected, result)

    def test_bubblesort_with_array(self):
        result = bubble_sort([12, 1, 0, 5, 4, 2])
        expected = [0, 1, 2, 4, 5, 1]
        self.assertNotEqual(expected, result)

    def test_bubblesort_with_True(self):
        result = bubble_sort([12, 1, 0, 5, 4, 2]), [0, 1, 2, 4, 5, 12]
        expected = True
        self.assertTrue(expected, result)

if __name__ == '__main__':
    unittest.main()

