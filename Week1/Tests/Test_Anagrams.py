from Week1.Util import IsAnagram
import unittest
from unittest import TestCase


class AnagramsTesting(TestCase):

    # def test_anagram_program(self):
    # self.runTests(self)

    def anagram_test_true(self):
            result = IsAnagram("earth", "heart")
            expected = True
            self.assertTrue(expected, result)

    def anagram_test_false(self):
            result = IsAnagram("test", "sets")
            expected = False
            self.assertFalse(expected, result)

if __name__ == '__main__':
    unittest.main()
