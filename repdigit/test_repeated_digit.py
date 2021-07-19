import unittest
from Test.repdigit import repeated_digit


class TestRepeatedDigit(unittest.TestCase):

    def test_repdigit(self):
        self.assertTrue(repeated_digit.repdigit('88'))
        self.assertTrue(repeated_digit.repdigit('77'))


    def test_repdigit_if_false(self):
        self.assertFalse(repeated_digit.repdigit('81'))
