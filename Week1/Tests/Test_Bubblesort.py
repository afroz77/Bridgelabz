import Week1.Algorithm.BubbleSort
from Week1.Util import bubble_sort
import unittest
from unittest import TestCase

class Test_Bubblesort_Program(unittest.TestProgram):

    def test_bubblesort_with_userinput(self):
        self.runTests(self)

class Test_bubblesort_functiion(TestCase):
    def test_bubblesort_with_possitive_array(self):
        result=bubble_sort([12, 1, 0, 5, 4, 2]),[0, 1, 2, 4, 5, 12]
        expected=True
        self.assertTrue(expected, result)

if __name__ == '__main__':
    unittest.main()