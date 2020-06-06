import unittest
import functions.trignometry as trig
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
        self.assertAlmostEqual(trig.sin(2*PI), 0, 9)
        self.assertAlmostEqual(trig.sin(-1*PI), 0, 9)

    def test_trig_unit_circle(self):
        self.assertAlmostEqual(trig.sin(PI/6), 0.5, 9)
        self.assertAlmostEqual(trig.sin(PI/4), 0.707106781186, 9)
        self.assertAlmostEqual(trig.sin(PI/3), 0.866025403784, 9)
        self.assertAlmostEqual(trig.sin(PI/2), 1, 9)
        self.assertAlmostEqual(trig.sin(2*PI/3), 0.866025403784, 9)
        self.assertAlmostEqual(trig.sin(3*PI/4), 0.707106781186, 9)
        self.assertAlmostEqual(trig.sin(5*PI/6), 0.5, 9)
        self.assertAlmostEqual(trig.sin(-PI/6), -0.5, 9)
        self.assertAlmostEqual(trig.sin(-PI/4), -0.707106781186, 9)
        self.assertAlmostEqual(trig.sin(-PI/3), -0.866025403784, 9)
        self.assertAlmostEqual(trig.sin(-PI/2), -1, 9)
        self.assertAlmostEqual(trig.sin(-2*PI/3), -0.866025403784, 9)
        self.assertAlmostEqual(trig.sin(-3*PI/4), -0.707106781186, 9)
        self.assertAlmostEqual(trig.sin(-5*PI/6), -0.5, 9)

    def test_sinh_(self):
        # test for hyberbolic function sinh
        self.assertAlmostEqual(trig.sinh(6), math.sinh(6), 9)
        self.assertAlmostEqual(trig.sinh(1.75), math.sinh(1.75), 9)
        self.assertAlmostEqual(trig.sinh(3.6), math.sinh(3.6), 9)
        self.assertAlmostEqual(trig.sinh(-0.7), math.sinh(-0.7),  9)
        self.assertAlmostEqual(trig.sinh(PI), math.sinh(math.pi), 9)


if __name__ == '__main__':
    unittest.main()
