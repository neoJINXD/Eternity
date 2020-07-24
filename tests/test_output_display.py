import unittest
import functions.output_display as display
import math


class TestOutputDisplayFunctions(unittest.TestCase):
    """
    Unit tests for deg, radian, scientific notation, binary functions
    """

    def test_deg(self):
        self.assertAlmostEqual(display.deg(1), math.degrees(1), 9)
        self.assertAlmostEqual(display.deg(0), math.degrees(0), 9)
        self.assertAlmostEqual(display.deg(180), math.degrees(180), 9)
        self.assertAlmostEqual(display.deg(290.57), math.degrees(290.57), 9)
        self.assertAlmostEqual(display.deg(math.pi), math.degrees(math.pi), 9)
        self.assertAlmostEqual(display.deg(-11), math.degrees(-11), 9)

    def test_rad(self):
        self.assertAlmostEqual(display.rad(1), math.radians(1), 9)
        self.assertAlmostEqual(display.rad(0), math.radians(0), 9)
        self.assertAlmostEqual(display.rad(180), math.radians(180), 9)
        self.assertAlmostEqual(display.rad(39532), math.radians(39532), 9)
        self.assertAlmostEqual(display.rad(290.57), math.radians(290.57), 9)
        self.assertAlmostEqual(display.rad(math.pi), math.radians(math.pi), 9)
        self.assertAlmostEqual(display.rad(-11), math.radians(-11), 9)

    def test_decimal_to_binary(self):  # 0b is removed from bin result for all unit tests
        self.assertEqual((int(display.convert_to_binary(6))),
                         (int(bin(6).replace("0b", ""))))  # Test for positive integer
        self.assertEqual((int(display.convert_to_binary(-6))),
                         (int(bin(-6).replace("0b", ""))))  # Test for negative integer
        self.assertEqual(float(display.convert_to_binary(8.25)), float(1000.01))  # Test for positive fraction
        self.assertEqual(float(display.convert_to_binary(-6.75)), float(-110.11))  # Test for negative fraction

    def test_binary_to_decimal(self):
        self.assertEqual(display.convert_to_decimal(10011111011101),
                         10205)  # Test for converting positive binary number
        self.assertEqual(display.convert_to_decimal(1000.01), 8.25)  # Test for converting positive binary numbers
        # with fractions
        self.assertEqual(display.convert_to_decimal(-10), -2)  # Test for converting positive binary numbers with
        # fractions
        self.assertEqual(display.convert_to_decimal(-101111.101), -47.625)  # Test for converting positive binary
        # numbers with fractions

