import unittest
import EulerExceptions
import EulersNumber as Calculator


class EulerTest(unittest.TestCase):
    def test_exponentPosNumbers(self):
        self.assertAlmostEqual(Calculator.calculate_exponent(2, 3), 2 ** 3)

    def test_exponentNegNumber(self):
        self.assertAlmostEqual(Calculator.calculate_exponent(200, -99), 200 ** -99)
        self.assertAlmostEqual(Calculator.calculate_exponent(997, -15), 997 ** -15)
        self.assertAlmostEqual(Calculator.calculate_exponent(8000, -150), 8000 ** -150)

    def test_exponentFractions(self):
        self.assertAlmostEqual(Calculator.calculate_exponent(3, (1 / 3)), 3 ** (1 / 3), delta=0.02)
        self.assertAlmostEqual(Calculator.calculate_exponent(100, (1 / 20)), 100 ** (1 / 20), delta=0.03)
        self.assertAlmostEqual(Calculator.calculate_exponent(200, (1 / 40)), 200 ** (1 / 40), delta=0.03)

    def test_exceptions(self):
        self.assertRaises(EulerExceptions.CalculatorException,Calculator.calculate_exponent, 'x-Value', 5)
        self.assertRaises(EulerExceptions.CalculatorException, Calculator.calculate_exponent, 5, 'y-Value')


if __name__ == '__main__':
    unittest.main()
