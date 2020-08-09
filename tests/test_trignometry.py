import unittest
import functions.trigonometry as trig
import math

# temporary const for PI
PI: float = 3.1415926535897932384626433832795


class TestTrigonometry(unittest.TestCase):
    '''
    Unit tests for most common cases where sin is used
    '''

    def test_sin_random_number(self):
        self.assertAlmostEqual(trig.sin(6), -0.2794154982, 9)
        self.assertAlmostEqual(trig.sin(1.75), 0.9839859468, 9)
        self.assertAlmostEqual(trig.sin(3.6), -0.4425204432, 9)
        self.assertAlmostEqual(trig.sin(-0.7), -0.6442176872, 9)

    def test_sin_pi_multiples(self):
        self.assertAlmostEqual(trig.sin(3.1415926535), 0, 9)
        self.assertAlmostEqual(trig.sin(0), 0, 9)
        self.assertAlmostEqual(trig.sin(PI), 0, 9)
        self.assertAlmostEqual(trig.sin(2 * PI), 0, 9)
        self.assertAlmostEqual(trig.sin(-1 * PI), 0, 9)

    def test_trig_unit_circle(self):
        self.assertAlmostEqual(trig.sin(PI / 6), 0.5, 9)
        self.assertAlmostEqual(trig.sin(PI / 4), 0.707106781186, 9)
        self.assertAlmostEqual(trig.sin(PI / 3), 0.866025403784, 9)
        self.assertAlmostEqual(trig.sin(PI / 2), 1, 9)
        self.assertAlmostEqual(trig.sin(2 * PI / 3), 0.866025403784, 9)
        self.assertAlmostEqual(trig.sin(3 * PI / 4), 0.707106781186, 9)
        self.assertAlmostEqual(trig.sin(5 * PI / 6), 0.5, 9)
        self.assertAlmostEqual(trig.sin(-PI / 6), -0.5, 9)
        self.assertAlmostEqual(trig.sin(-PI / 4), -0.707106781186, 9)
        self.assertAlmostEqual(trig.sin(-PI / 3), -0.866025403784, 9)
        self.assertAlmostEqual(trig.sin(-PI / 2), -1, 9)
        self.assertAlmostEqual(trig.sin(-2 * PI / 3), -0.866025403784, 9)
        self.assertAlmostEqual(trig.sin(-3 * PI / 4), -0.707106781186, 9)
        self.assertAlmostEqual(trig.sin(-5 * PI / 6), -0.5, 9)

    def test_cos_random_numbers(self):
        self.assertAlmostEqual(trig.cos(6), 0.9601702867, 9)
        self.assertAlmostEqual(trig.cos(1.75), -0.1782460556, 9)
        self.assertAlmostEqual(trig.cos(3.6), -0.8967584163, 9)
        self.assertAlmostEqual(trig.cos(-0.7), 0.7648421873, 9)

    def test_cos_pi_multiples(self):
        self.assertAlmostEqual(trig.cos(3.1415926535), -1, 9)
        self.assertAlmostEqual(trig.cos(0), 1, 9)
        self.assertAlmostEqual(trig.cos(PI), -1, 9)
        self.assertAlmostEqual(trig.cos(2 * PI), 1, 9)
        self.assertAlmostEqual(trig.cos(-1 * PI), -1, 9)

    # TODO need more test cases for cos later

    def test_tan(self):
        # test for tan function
        self.assertAlmostEqual(trig.tan(1), math.tan(1), 9)
        self.assertAlmostEqual(trig.tan(PI), math.tan(math.pi), 9)

    def test_sinh(self):
        # test for hyberbolic function sinh
        self.assertAlmostEqual(trig.sinh(6), math.sinh(6), 9)
        self.assertAlmostEqual(trig.sinh(1.75), math.sinh(1.75), 9)
        self.assertAlmostEqual(trig.sinh(3.6), math.sinh(3.6), 9)
        self.assertAlmostEqual(trig.sinh(-0.7), math.sinh(-0.7), 9)
        self.assertAlmostEqual(trig.sinh(PI), math.sinh(math.pi), 9)

    def test_cosh(self):
        # test for hyberbolic function cosh
        self.assertAlmostEqual(trig.cosh(6), math.cosh(6), 9)
        self.assertAlmostEqual(trig.cosh(1.75), math.cosh(1.75), 9)
        self.assertAlmostEqual(trig.cosh(3.6), math.cosh(3.6), 9)
        self.assertAlmostEqual(trig.cosh(-0.7), math.cosh(-0.7), 9)
        self.assertAlmostEqual(trig.cosh(PI), math.cosh(math.pi), 9)

    def test_tanh(self):
        # test for hyberbolic function cosh
        self.assertAlmostEqual(trig.tanh(6), math.tanh(6), 9)
        self.assertAlmostEqual(trig.tanh(1.75), math.tanh(1.75), 9)
        self.assertAlmostEqual(trig.tanh(3.6), math.tanh(3.6), 9)
        self.assertAlmostEqual(trig.tanh(-0.7), math.tanh(-0.7), 9)
        self.assertAlmostEqual(trig.tanh(PI), math.tanh(math.pi), 9)

    def test_generate_pi(self):
        # test for pi constant
        self.assertAlmostEqual(trig.generate_pi(), math.pi, 9)

    def test_process_angle_mode(self):
        # test wrapper for trigonometry functions used in parser
        # no need to extensively test for when is_rad is True as this is covered by other trig functions
        self.assertAlmostEqual(trig.process_angle_mode(1, True, trig.sin), math.sin(1), 9)
        self.assertAlmostEqual(trig.process_angle_mode(-2, True, trig.sin), math.sin(-2), 9)
        self.assertAlmostEqual(trig.process_angle_mode(260, True, trig.sin), math.sin(260), 9)
        # basic trig
        self.assertAlmostEqual(trig.process_angle_mode(0, False, trig.cos), math.cos(math.radians(0)), 9)
        self.assertAlmostEqual(trig.process_angle_mode(-1, False, trig.tan), math.tan(math.radians(-1)), 9)
        # hyperbolic
        self.assertAlmostEqual(trig.process_angle_mode(16, False, trig.sinh), math.sinh(math.radians(16)), 9)
        self.assertAlmostEqual(trig.process_angle_mode(9, False, trig.cosh), math.cosh(math.radians(9)), 9)
        self.assertAlmostEqual(trig.process_angle_mode(34, False, trig.tanh), math.tanh(math.radians(34)), 9)
        # larger values
        self.assertAlmostEqual(trig.process_angle_mode(532, False, trig.cos), math.cos(math.radians(532)), 9)
        self.assertAlmostEqual(trig.process_angle_mode(165, False, trig.tan), math.tan(math.radians(165)), 9)


if __name__ == '__main__':
    unittest.main()
