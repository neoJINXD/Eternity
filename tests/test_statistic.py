import unittest
import functions.statistic as stats
import functions.trigonometry as trig
import math
import numpy as np
import pandas as pd
# import exceptions.exceptions as the_exception


class StdMadTest(unittest.TestCase):
    def test_std(self):
        self.assertAlmostEqual(stats.std(1, 4, 7, 2, 6), 2.280350850198276, 9)
        self.assertAlmostEqual(stats.std(5, 4, 7, 1, 9, 18, 22, 33), 10.270558650823235, 9)

    def test_mad(self):
        self.assertAlmostEqual(stats.mad(3, 15, 21, 13), 5.0, 9)
        self.assertAlmostEqual(stats.mad(43, 20, 18, 5, 41, 25, 11), 11.183673469387754, 9)

    def test_std_input_of_0(self):
        self.assertAlmostEqual(stats.std(1, 4, 7, 2, 6, 0), np.std([1, 4, 7, 2, 6, 0]), 9)

    def test_mad_input_of_0(self):
        self.assertAlmostEqual(stats.mad(3, 15, 21, 13, 0), pd.Series([3, 15, 21, 13, 0]).mad(), 9)

    def test_std_input_of_pi(self):
        self.assertAlmostEqual(stats.std(1.1, 4.6, 7.2, 2.5, 6.3, trig.generate_pi()),
                               np.std([1.1, 4.6, 7.2, 2.5, 6.3, math.pi]), 7)

    def test_std_input_of_neg(self):
        self.assertAlmostEqual(stats.std(1, 4, 7, 2, 6, -10), np.std([1, 4, 7, 2, 6, -10]), 9)

    def test_mad_input_of_neg(self):
        self.assertAlmostEqual(stats.mad(3, 15, 21, 13, -10), pd.Series([3, 15, 21, 13, -10]).mad(), 9)

    def test_std_input_of_rational(self):
        self.assertAlmostEqual(stats.std(1.1, 4.6, 7.2, 2.5, 6.3, 0.8),
                               np.std([1.1, 4.6, 7.2, 2.5, 6.3, 0.8]))

    def test_mad_input_of_rational(self):
        self.assertAlmostEqual(stats.mad(3.4, 15.8, 21.6, 13.2, 0.1),
                               pd.Series([3.4, 15.8, 21.6, 13.2, 0.1]).mad())

    def test_std_input_of_large_number(self):
        self.assertAlmostEqual(stats.std(5849, 4167, 78510, 15482, 9167, 18187, 22518, 33784), np.std([5849, 4167, 78510, 15482, 9167, 18187, 22518, 33784]))

    def test_mad_input_of_large_number(self):
        self.assertAlmostEqual(stats.mad(430, 2000, 1857, 587, 4118, 2530, 1185), pd.Series([430, 2000, 1857, 587, 4118, 2530, 1185]).mad())

    # def test_exceptions(self):
    #     self.assertRaises(the_exception.CalculationError, exp.calculate_exponent, 'x-Value', 5)
    #     self.assertRaises(the_exception.CalculationError, exp.calculate_exponent, 'x-Value', 5)
    #     self.assertRaises(the_exception.CalculationError, exp.calculate_exponent, 5, 'y-Value')


if __name__ == '__main__':
    unittest.main()
