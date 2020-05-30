import unittest
import functions.exponents_and_logs as exp


class EulerTest(unittest.TestCase):
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

if __name__ == '__main__':
    unittest.main()