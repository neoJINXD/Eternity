import unittest
import functions.inverse_trigonometry as trig
import math

# temporary const for PI
PI: float = 3.1415926535897932384626433832795


class TestInverseTrigonometry(unittest.TestCase):
    '''
    Unit tests for most common cases where sin inverse function is used
    '''

    def test_inverse_sin_random_number(self):
        self.assertAlmostEqual(trig.sin(-1), -1.57079633, 9)
        self.assertAlmostEqual(trig.sin(1), 1.57079633, 9)
        self.assertAlmostEqual(trig.sin(-0.5), -0.523598776, 9)
        self.assertAlmostEqual(trig.sin(0.5), 0.523598776, 9)
        self.assertAlmostEqual(trig.sin(0), 0, 9)
        self.assertAlmostEqual(trig.sin(-0.75), -0.848062079, 9)
        self.assertAlmostEqual(trig.sin(0.75), 0.848062079, 9)
        self.assertAlmostEqual(trig.sin(0.25), 0.252680255, 9)

    def test_inverse_cos_random_numbers(self):
        self.assertAlmostEqual(trig.cos(-1), 3.14159265, 9)
        self.assertAlmostEqual(trig.cos(1), 0, 9)
        self.assertAlmostEqual(trig.cos(-0.5), 2.0943951, 9)
        self.assertAlmostEqual(trig.cos(0.5), 1.04719755, 9)
        self.assertAlmostEqual(trig.cos(0), 1.57079633, 9)
        self.assertAlmostEqual(trig.cos(-0.75), 2.41885841, 9)
        self.assertAlmostEqual(trig.cos(0.75), 0.722734248, 9)
        self.assertAlmostEqual(trig.cos(0.25), 1.31811607, 9)

    def test_inverse_tan_random_numbers(self):
        self.assertAlmostEqual(trig.tan(-1), -0.785398163, 9)
        self.assertAlmostEqual(trig.tan(1), 0.785398163, 9)
        self.assertAlmostEqual(trig.tan(-0.5), -0.463647609, 9)
        self.assertAlmostEqual(trig.tan(0.5), 0.463647609, 9)
        self.assertAlmostEqual(trig.tan(0), 0, 9)
        self.assertAlmostEqual(trig.tan(-0.75), -0.643501109, 9)
        self.assertAlmostEqual(trig.tan(0.75), 0.643501109, 9)
        self.assertAlmostEqual(trig.tan(0.25), 0.244978663, 9)





if __name__ == '__main__':
    unittest.main()