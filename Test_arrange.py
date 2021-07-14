import unittest
import arrange


class TestArrange(unittest.TestCase):
    '''
    Will test if arguments are equal, not equal and
    '''

    def test_words(self):
        self.assertEqual(arrange.words(["g", "e", "o"], [0, 1, 2]), 'geo')
        self.assertEqual(arrange.words(["e","l", "l", "o", "h"], [4, 0, 1, 2, 3]), 'hello')

    def test_words_reject_argument(self):
        self.assertNotEqual(arrange.words(["g", "e", "o"], [0, 1, 2]), 'ge o')
        self.assertNotEqual(arrange.words(["e", "l", "l", "o", "h"], [4, 0, 1, 2, 3]), 'he llo')

    def test_words_god(self):
        self.assertNotIn(arrange.words(["g", "e", "o"],[0, 1, 2]), 'hello')
        self.assertNotIn(arrange.words(["e", "l", "l", "o", "h"], [4, 0, 1, 2, 3]), 'geo')

