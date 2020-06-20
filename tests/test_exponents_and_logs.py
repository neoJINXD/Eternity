import unittest
import exceptions.exceptions as exceptions
import functions.exponents_and_logs as exp
import functions.trignometry as trig
import math as math


class ExponentsTest(unittest.TestCase):
    PI = trig.generate_pi()

    def test_e(self):
        # Tests euler number function's capacity for generating euler number.
        self.assertAlmostEqual(exp.exp(), math.e, 15)

    def test_exp_input_0(self):
        # Tests euler number function's capacity for handling input of 0.
        self.assertAlmostEqual(exp.exp(0), math.pow(math.e, 0), 12)

    def test_exp_input_neg(self):
        # Tests euler number function's capacity for handling negative inputs.
        self.assertAlmostEqual(exp.exp(-10), math.pow(math.e, -10), 12)
        self.assertAlmostEqual(exp.exp(-3), math.pow(math.e, -3), 12)

    def test_exp_input_rational(self):
        # Tests euler number function's capacity for handling non-integer inputs.
        self.assertAlmostEqual(exp.exp(0.5), math.pow(math.e, 0.5), 12)
        self.assertAlmostEqual(exp.exp(5 / 8), math.pow(math.e, 5/8), 12)

    def test_exp_input_big(self):
        # Tests euler number function's capacity for handling big numbers
        self.assertAlmostEqual(exp.exp(32), pow(math.e, 32))  # Accuracy needs work for big numbers, decimal places incorrect
        self.assertAlmostEqual(exp.exp(18), pow(math.e, 18))

    def test_exp_input_transcendental(self):
        # Tests euler number function's capacity for handling other transcendental numbers such as pi as input
        self.assertAlmostEqual(exp.exp(trig.generate_pi()), pow(math.e, math.pi))
        self.assertAlmostEqual(exp.exp(exp.exp()), pow(math.e, math.e))

    def test_exponent_input_pos(self):
        # Tests exponent function's capacity for handling positive integer inputs.
        self.assertAlmostEqual(exp.pow(2, 3), 2 ** 3)

    def test_exponent_input_neg(self):
        # Tests exponent function's capacity for handling negative integer inputs.
        self.assertAlmostEqual(exp.pow(200, -99), 200 ** -99)
        self.assertAlmostEqual(exp.pow(997, -15), 997 ** -15)
        self.assertAlmostEqual(exp.pow(8000, -150), 8000 ** -150)

    def test_zero_power_zero(self):
        # Tests 0 to the power of 0
        self.assertAlmostEqual(exp.pow(0, 0), 0 ** 0)

    def test_exponent_input_rational(self):
        # Tests exponent function's capacity for handling non-integer inputs.
        self.assertAlmostEqual(exp.pow(3, (1 / 3)), 3 ** (1 / 3))
        self.assertAlmostEqual(exp.pow(100, (1 / 20)), 100 ** (1 / 20))
        self.assertAlmostEqual(exp.pow(200, (1 / 40)), 200 ** (1 / 40))
        self.assertAlmostEqual(exp.pow((63 / 40), (1 / 40)), (63 / 40) ** (1 / 40))

    def test_rational_power_rational(self):
        # Tests a rational number to the power of a rational number
        self.assertAlmostEqual(exp.pow((1 / 3), (1 / 3)), (1 / 3) ** (1 / 3), 5)
        self.assertAlmostEqual(exp.pow((1 / 20), (2 / 9)), (1 / 20) ** (2 / 9), 5)
        self.assertAlmostEqual(exp.pow((2 ** (1 / 2)), (2 ** (1 / 2))), math.sqrt(2) ** math.sqrt(2), 5)

    def test_logarithm_input_int(self):
        # Tests logarithm function's capacity for handling positive integer inputs.
        # Logarithms undefined for negative arguments &  base in addition to arguments and bases of 0 and 1.
        self.assertAlmostEqual(exp.log(3), math.log(3, 10))
        self.assertAlmostEqual(exp.log(4), math.log(4, 10))
        self.assertAlmostEqual(exp.log(1, 20), math.log(1, 20))

    def test_logarithm_input_rational(self):
        # Tests exponent function's capacity for handling negative integer inputs.
        self.assertAlmostEqual(exp.log(1.5), math.log(1.5, 10))
        self.assertAlmostEqual(exp.log(math.pi), math.log(math.pi, 10))
        self.assertAlmostEqual(exp.log(2, math.pi), math.log(2, math.pi))
        self.assertAlmostEqual(exp.log(3, 1.45), math.log(3, 1.45))
        self.assertAlmostEqual(exp.log(1000000, 0.5), math.log(1000000, 0.5))

    def test_logarithm_exceptions(self):
        # Tests exponent function's exception handling capacity.
        # Test handling of invalid base
        with self.assertRaises(exceptions.InputError):
            exp.log(20, 0)
        with self.assertRaises(exceptions.InputError):
            exp.log(20, 1)
        with self.assertRaises(exceptions.InputError):
            exp.log(20, -1)
        # Test handling of invalid argument
        with self.assertRaises(exceptions.InputError):
            exp.log(-5, 2)
        with self.assertRaises(exceptions.InputError):
            exp.log(0, 2)

    def test_pow_10(self):
        # Tests power of ten function.
        self.assertAlmostEqual(exp.pow_10(0), 1)
        self.assertAlmostEqual(exp.pow_10(1), 10)
        self.assertAlmostEqual(exp.pow_10(2), 100)
        self.assertAlmostEqual(exp.pow_10(-4), 10 ** (-4))
        self.assertAlmostEqual(exp.pow_10(0.01), 10 ** 0.01)
        self.assertAlmostEqual(exp.pow_10(self.PI), 10 ** self.PI)

    def test_pow_pi(self):
        # Tests power of pi function.
        self.assertAlmostEqual(exp.pow_pi(0), 1)
        self.assertAlmostEqual(exp.pow_pi(1), self.PI)
        self.assertAlmostEqual(exp.pow_pi(2), self.PI ** 2)
        self.assertAlmostEqual(exp.pow_pi(-4), self.PI ** (-4))
        self.assertAlmostEqual(exp.pow_pi(0.01), self.PI ** 0.01)
        self.assertAlmostEqual(exp.pow_pi(self.PI), self.PI ** self.PI)


if __name__ == '__main__':
    unittest.main()
