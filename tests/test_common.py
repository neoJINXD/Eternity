import unittest
import functions.common as common
import math
import exceptions.exceptions as the_exception


# test class
class TestCommon(unittest.TestCase):

    def test_factorial(self):
        self.assertEqual(common.factorial(6), math.factorial(6))
        self.assertEqual(common.factorial(0), math.factorial(0))  # Test input of 0
        self.assertEqual(common.factorial(345), math.factorial(345))  # Test large number

    def test_factorial_neg_raise_error(self):
        with self.assertRaises(the_exception.InputError):
            common.factorial(-1)

    def test_factorial_float_raise_error(self):
        with self.assertRaises(the_exception.InputError):
            common.factorial(56.3)

    def test_exponent_negative(self):
        self.assertEqual(common.is_negative(-5), True)
        self.assertEqual(common.is_negative(5), False)

    def test_inverse(self):
        self.assertEqual(common.inverse(5), 1 / 5)
        self.assertEqual(common.inverse(-5), - 1 / 5)
        self.assertEqual(common.inverse(-1 / 5), - 5)


# Allows us to run the tests immediately when this file is run
if __name__ == '__main__':
    unittest.main()
