import unittest
from Test import Larger_no


class TestLargerNo(unittest.TestCase):

    def test_larger_number(self):
        self.assertEqual(Larger_no.larger_number(lambda: 10, lambda: 6), 'f')
