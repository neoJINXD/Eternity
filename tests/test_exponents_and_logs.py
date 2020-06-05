import unittest
import exceptions.exceptions as the_exception
import functions.exponents_and_logs as exp
import functions.trignometry as trig
import math as math


class ExponentsTest(unittest.TestCase):

    PI = trig.generate_pi()

    def test_e(self):
        # Tests eurler number function's capacity for generating euler number.
        self.assertAlmostEqual(exp.generate_e(), 2.718281828, 9)


    def test_generate_e_input_0(self):
        # Tests eurler number function's capacity for handling input of 0.
        self.assertAlmostEqual(exp.generate_e(0), 1.0, 1)


    def test_generate_e_input_neg(self):
        # Tests eurler number function's capacity for handling negative inputs.
        self.assertAlmostEqual(exp.generate_e(-10), 0.000045399)
        self.assertAlmostEqual(exp.generate_e(-19), 0.000000005)


    def test_generate_e_input_rational(self):
        # Tests eurler number function's capacity for handling non-integer inputs.
        self.assertAlmostEqual(exp.generate_e(0.5), 1.648721271)
        self.assertAlmostEqual(exp.generate_e(5 / 8), 1.868245957)


    def test_exponent_input_pos(self):
        # Tests exponent function's capacity for handling positive integer inputs.
        self.assertAlmostEqual(exp.calculate_exponent(2, 3), 2 ** 3)


    def test_exponent_input_neg(self):
        # Tests exponent function's capacity for handling negative integer inputs.
        self.assertAlmostEqual(exp.calculate_exponent(200, -99), 200 ** -99)
        self.assertAlmostEqual(exp.calculate_exponent(997, -15), 997 ** -15)
        self.assertAlmostEqual(exp.calculate_exponent(8000, -150), 8000 ** -150)


    def test_exponent_input_rational(self):
        # Tests exponent function's capacity for handling non-integer inputs.
        self.assertAlmostEqual(exp.calculate_exponent(3, (1 / 3)), 3 ** (1 / 3), delta=0.02)
        self.assertAlmostEqual(exp.calculate_exponent(100, (1 / 20)), 100 ** (1 / 20), delta=0.03)
        self.assertAlmostEqual(exp.calculate_exponent(200, (1 / 40)), 200 ** (1 / 40), delta=0.03)
        self.assertAlmostEqual(exp.calculate_exponent((63 / 40), (1 / 40)), (63 / 40) ** (1 / 40), delta=0.03)


    def test_exponent_exceptions(self):
        # Tests exponent function's exception handling capacity.
        with self.assertRaises(the_exception.CalculationError):
            exp.calculate_exponent('x-Value', 5)
        with self.assertRaises(the_exception.CalculationError):
            exp.calculate_exponent(5, 'y-Value')


    def test_logarithm_input_int(self):
        # Tests logarithm function's capacity for handling positive integer inputs.
        # Logarithms are undefined for negative arguments and negative base in addition to arguments and bases of 0 and bases of 1.
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
        with self.assertRaises(ValueError):
            exp.log(20, 0)
        with self.assertRaises(ValueError):
            exp.log(20, 1)
        with self.assertRaises(ValueError):
            exp.log(20, -1)
        with self.assertRaises(TypeError):
            exp.log(20, "hello")
        #Test handling of invalid argument
        with self.assertRaises(ValueError):
            exp.log(-5, 2)
        with self.assertRaises(ValueError):
            exp.log(0, 2)
        with self.assertRaises(TypeError):
            exp.log(complex(2, 1), 2)
        with self.assertRaises(TypeError):
            exp.log(None, 2)
            
            
    def test_power_of_ten(self):
        # Tests power of ten function.
        self.assertAlmostEqual(exp.power_of_ten(0), 1)
        self.assertAlmostEqual(exp.power_of_ten(1), 10)
        self.assertAlmostEqual(exp.power_of_ten(2), 100)
        self.assertAlmostEqual(exp.power_of_ten(-4), 10**(-4))
        self.assertAlmostEqual(exp.power_of_ten(0.01), 10**(0.01))
        self.assertAlmostEqual(exp.power_of_ten(self.PI), 10**self.PI)
        self.assertRaises(the_exception.CalculationError, exp.power_of_ten, 'invalid')

        
    def test_power_of_pi(self):
        # Tests power of pi function.
        self.assertAlmostEqual(exp.power_of_pi(0), 1)
        self.assertAlmostEqual(exp.power_of_pi(1), self.PI)
        self.assertAlmostEqual(exp.power_of_pi(2), self.PI**2)
        self.assertAlmostEqual(exp.power_of_pi(-4), self.PI**(-4))  # TODO still innacurate
        self.assertAlmostEqual(exp.power_of_pi(0.01), self.PI**0.01)
        self.assertAlmostEqual(exp.power_of_pi(self.PI), self.PI**self.PI)  # TODO still innacurate
        self.assertRaises(the_exception.CalculationError, exp.power_of_pi, True)


if __name__ == '__main__':
    unittest.main()
