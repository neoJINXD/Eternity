import unittest
from functions.sin import sin
from math import pi


class TestSin(unittest.TestCase):

    def test_sin_(self):
        self.assertAlmostEqual(sin(6), -0.2794154982, 9)

    def test_sin_pi_multiples(self):
        self.assertAlmostEqual(sin(0), 0, 9)
        self.assertAlmostEqual(sin(pi), 0, 9)
        self.assertAlmostEqual(sin(2*pi), 0, 9)
        self.assertAlmostEqual(sin(-1*pi), 0, 9)

    def test_trig_unit_circle(self):
        pass
        # self.assertAlmostEqual(sin(), , 9)


if __name__ == '__main__':
    unittest.main()
