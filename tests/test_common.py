import unittest
import functions.common as common
import math
import exceptions.exceptions as the_exception


class TestCommon(unittest.TestCase):
    """A class used to test common functions."""

    def test_factorial(self):
        """Test factorial function."""
        self.assertEqual(common.factorial(6), math.factorial(6))
        self.assertEqual(common.factorial(0), math.factorial(0))
        self.assertEqual(common.factorial(345), math.factorial(345))
        with self.assertRaises(the_exception.InputError):
            common.factorial(-1)
        with self.assertRaises(the_exception.InputError):
            common.factorial(56.3)

    def test_mod(self):
        """Test mod function."""
        self.assertEqual(common.mod(6,3), 6 % 3)
        self.assertEqual(common.mod(32.5,11.1), 32.5 % 11.1)
        self.assertEqual(common.mod(10,3), 10 % 3)
        self.assertEqual(common.mod(-64.32,-9.34), -64.32 % -9.34)
        with self.assertRaises(the_exception.InputError):
            common.mod(6,0)

    def test_is_negative(self):
        """Test is_negative function."""
        self.assertEqual(common.is_negative(-5), True)
        self.assertEqual(common.is_negative(5), False)
        self.assertEqual(common.is_negative(0), False)

    def test_is_positive(self):
        """Test is_positive function."""
        self.assertEqual(common.is_positive(-5), False)
        self.assertEqual(common.is_positive(5), True)
        self.assertEqual(common.is_positive(0), False)

    def test_is_even(self):
        """Test is_even function."""
        self.assertEqual(common.is_even(0), True)
        self.assertEqual(common.is_even(1), False)
        self.assertEqual(common.is_even(-100), True)
        with self.assertRaises(the_exception.InputError):
            common.is_even(56.3)

    def test_is_odd(self):
        """Test is_odd function."""
        self.assertEqual(common.is_odd(0), False)
        self.assertEqual(common.is_odd(1), True)
        self.assertEqual(common.is_odd(-101), True)
        with self.assertRaises(the_exception.InputError):
            common.is_odd(56.3)

    def test_inverse(self):
        """Test inverse function."""
        self.assertEqual(common.inverse(5), 1 / 5)
        self.assertEqual(common.inverse(-5), - 1 / 5)
        self.assertEqual(common.inverse(-1 / 5), - 5)
        # Test divisor of 0.
        with self.assertRaises(the_exception.InputError):
            common.inverse(0)

    def test_abs(self):
        """Test absolute function."""
        self.assertEqual(common.abs(5), 5)
        self.assertEqual(common.abs(-5), 5)
        self.assertEqual(common.abs(0), 0)
        self.assertEqual(common.abs(-1.22), 1.22)


# Allows us to run the tests immediately when this file is run
if __name__ == '__main__':
    unittest.main()
