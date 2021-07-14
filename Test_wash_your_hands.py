import unittest
import wash_your_hands


class TestWashYourHands(unittest.TestCase):

    def test_WYH(self):
       self.assertEqual(wash_your_hands.WYH(7, 9), '661minutes, 30seconds')
       self.assertEqual(wash_your_hands.WYH(0, 0), '0minutes, 0seconds')

if __name__ == '__main__':
    unittest.main()