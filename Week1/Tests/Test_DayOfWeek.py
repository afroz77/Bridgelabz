from Week1.Util import DayOfWeek
import unittest
from unittest import TestCase

class Test_DayOfWeek(TestCase):
    def DayOfWeek(self):
        result = (DayOfWeek(16, 5, 2019))
        expected = 'Thursday'
        self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()