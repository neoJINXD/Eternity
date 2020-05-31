import unittest
import functions.exponent_helper_functions as helper_functions


class HelperTest(unittest.TestCase):

    def test_exponent_ints(self):
        self.assertEqual(helper_functions.calculate_exponent_int_only(5, 8), 5 ** 8)

    def test_exponent_negative(self):
        self.assertEqual(helper_functions.is_negative(-5), True)
        self.assertEqual(helper_functions.is_negative(5), False)

    def test_inverse(self):
        self.assertEqual(helper_functions.take_inverse(5), 1 / 5)
        self.assertEqual(helper_functions.take_inverse(-5), - 1 / 5)
        self.assertEqual(helper_functions.take_inverse(-1 / 5), - 5)

    def test_root(self):
        self.assertAlmostEqual(helper_functions.calculate_root(1), 1 ** (1 / 100), delta=0.000001)
        self.assertAlmostEqual(helper_functions.calculate_root(200), 200 ** (1 / 100), delta=0.0000001)
        self.assertAlmostEqual(helper_functions.calculate_root(100000), 100000 ** (1 / 100), delta=0.000001)
        self.assertAlmostEqual(helper_functions.calculate_root(9000000), 9000000 ** (1 / 100), delta=0.000001)
        self.assertAlmostEqual(helper_functions.calculate_root(9000000000), 9000000000 ** (1 / 100), delta=0.000001)


if __name__ == '__main__':
    unittest.main()
