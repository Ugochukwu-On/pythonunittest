import unittest
import Employee_data

class TestEmployeeData(unittest.TestCase):

    def test_Employee_Data(self):
        pass

    def test_email(self):
        x = Employee_data.Employee('uncle','ben')
        email = 'uncle' + 'ben' + '@gmail.com'
        self.assertEqual((x.email), 'uncleben@gmail.com')


if __name__ == '__main__':
    unittest.main()