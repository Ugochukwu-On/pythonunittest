import unittest
import pin


class TestPin(unittest.TestCase):

    def test_valid_pin(self):
        self.assertEquals(pin.valid_pin('1234'),True)
        self.assertEquals(pin.valid_pin('0000'),True)

    def test_valid_pin_rejects_white_space(self):
        self.assertEquals(pin.valid_pin('78 98'), False, msg=' Whitespace detected ')

    def test_valid_pin_is_true(self):
        self.assertTrue(pin.valid_pin('1234'))
        self.assertTrue(pin.valid_pin('0000'))


