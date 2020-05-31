import unittest
from functions.sin import sin

# temporary const for PI
PI: float = 3.1415926535897932384626433832795


class TestSin(unittest.TestCase):
    '''
    Unit tests for most common cases where sin is used
    '''

    def test_sin_random_number(self):
        self.assertAlmostEqual(sin(6), -0.2794154982, 9)
        self.assertAlmostEqual(sin(1.75), 0.9839859468, 9)
        self.assertAlmostEqual(sin(3.6), -0.4425204432, 9)
        self.assertAlmostEqual(sin(-0.7), -0.6442176872, 9)

    def test_sin_pi_multiples(self):
        self.assertAlmostEqual(sin(3.1415926535), 0, 9)
        self.assertAlmostEqual(sin(0), 0, 9)
        self.assertAlmostEqual(sin(PI), 0, 9)
        self.assertAlmostEqual(sin(2*PI), 0, 9)
        self.assertAlmostEqual(sin(-1*PI), 0, 9)

    def test_trig_unit_circle(self):
        self.assertAlmostEqual(sin(PI/6), 0.5, 9)
        self.assertAlmostEqual(sin(PI/4), 0.707106781186, 9)
        self.assertAlmostEqual(sin(PI/3), 0.866025403784, 9)
        self.assertAlmostEqual(sin(PI/2), 1, 9)
        self.assertAlmostEqual(sin(2*PI/3), 0.866025403784, 9)
        self.assertAlmostEqual(sin(3*PI/4), 0.707106781186, 9)
        self.assertAlmostEqual(sin(5*PI/6), 0.5, 9)
        self.assertAlmostEqual(sin(-PI/6), -0.5, 9)
        self.assertAlmostEqual(sin(-PI/4), -0.707106781186, 9)
        self.assertAlmostEqual(sin(-PI/3), -0.866025403784, 9)
        self.assertAlmostEqual(sin(-PI/2), -1, 9)
        self.assertAlmostEqual(sin(-2*PI/3), -0.866025403784, 9)
        self.assertAlmostEqual(sin(-3*PI/4), -0.707106781186, 9)
        self.assertAlmostEqual(sin(-5*PI/6), -0.5, 9)


if __name__ == '__main__':
    unittest.main()
