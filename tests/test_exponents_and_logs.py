import unittest
import exceptions.exceptions as the_exception
import functions.exponents_and_logs as exp
import functions.trignometry as trig


class ExponentsTest(unittest.TestCase):

    PI = trig.generate_pi()

    def test_e(self):
        self.assertAlmostEqual(exp.generate_e(), 2.718281828, 9)

    def test_generate_e_input_of_0(self):
        self.assertAlmostEqual(exp.generate_e(0), 1.0, 1)

    def test_generate_e_input_of_neg(self):
        self.assertAlmostEqual(exp.generate_e(-10), 0.000045399)
        self.assertAlmostEqual(exp.generate_e(-19), 0.000000005)

    def test_generate_e_input_of_rational(self):
        self.assertAlmostEqual(exp.generate_e(0.5), 1.648721271)
        self.assertAlmostEqual(exp.generate_e(5 / 8), 1.868245957)

    def test_exponentPosNumbers(self):
        self.assertAlmostEqual(exp.calculate_exponent(2, 3), 2 ** 3)

    def test_exponentNegNumber(self):
        self.assertAlmostEqual(exp.calculate_exponent(200, -99), 200 ** -99)
        self.assertAlmostEqual(exp.calculate_exponent(997, -15), 997 ** -15)
        self.assertAlmostEqual(exp.calculate_exponent(8000, -150), 8000 ** -150)

    def test_exponentFractions(self):
        self.assertAlmostEqual(exp.calculate_exponent(3, (1 / 3)), 3 ** (1 / 3), delta=0.02)
        self.assertAlmostEqual(exp.calculate_exponent(100, (1 / 20)), 100 ** (1 / 20), delta=0.03)
        self.assertAlmostEqual(exp.calculate_exponent(200, (1 / 40)), 200 ** (1 / 40), delta=0.03)

    def test_power_of_ten(self):
        self.assertAlmostEqual(exp.power_of_ten(0), 1)
        self.assertAlmostEqual(exp.power_of_ten(1), 10)
        self.assertAlmostEqual(exp.power_of_ten(2), 100)
        self.assertAlmostEqual(exp.power_of_ten(-4), 10**(-4))
        self.assertAlmostEqual(exp.power_of_ten(0.01), 10**(0.01))
        self.assertAlmostEqual(exp.power_of_ten(self.PI), 10**self.PI)
        self.assertRaises(the_exception.CalculationError, exp.power_of_ten, 'invalid')

    def test_power_of_pi(self):
        self.assertAlmostEqual(exp.power_of_pi(0), 1)
        self.assertAlmostEqual(exp.power_of_pi(1), self.PI)
        self.assertAlmostEqual(exp.power_of_pi(2), self.PI**2)
        self.assertAlmostEqual(exp.power_of_pi(-4), self.PI**(-4))  # TODO still innacurate
        self.assertAlmostEqual(exp.power_of_pi(0.01), self.PI**0.01)
        self.assertAlmostEqual(exp.power_of_pi(self.PI), self.PI**self.PI)  # TODO still innacurate
        self.assertRaises(the_exception.CalculationError, exp.power_of_pi, True)

    # I will need to fix this test
    def test_exceptions(self):
        self.assertRaises(the_exception.CalculationError, exp.calculate_exponent, 'x-Value', 5)
        self.assertRaises(the_exception.CalculationError, exp.calculate_exponent, 5, 'y-Value')


if __name__ == '__main__':
    unittest.main()
