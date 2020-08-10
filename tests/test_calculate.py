import unittest
import calculate
import math
import exceptions.exceptions as the_exception

# test class
class TestCalculate(unittest.TestCase):
    def test_evaluate(self):
        # test misc inputs to get ~100% coverage on the parser
        self.assertEqual(calculate.evaluate('', False, False), '')
        self.assertEqual(calculate.evaluate('6+6', False, False), 6+6)
        self.assertEqual(calculate.evaluate('1+1', False, True), str(bin(2))[2:])
        self.assertEqual(calculate.evaluate('(-1)', False, False), -1)
        self.assertEqual(calculate.evaluate('(+1)', False, False), 1)
        self.assertEqual(calculate.evaluate('4!', False, False), math.factorial(4))
    
    def test_asq_eval(self):
        # Test ASQ calculations
        self.assertAlmostEqual(calculate.evaluate('cos(8*pi)', True, False), math.cos(8*math.pi))
        self.assertAlmostEqual(calculate.evaluate('mad(e,π,e^2,π^2)', False, False), 2.84969, 4)
        self.assertAlmostEqual(calculate.evaluate('sqrt(log(12))', False, False), math.sqrt(math.log(12)))

    def test_parsing_error(self):
        self.assertEqual(calculate.evaluate('a', False, False), 'Parsing Error: Invalid input entered.')
        self.assertEqual(calculate.evaluate('(log(5)', False, False), 'Parsing Error: Invalid input entered.')
        self.assertEqual(calculate.evaluate('log(5))', False, False), 'Parsing Error: Invalid input entered.')
        self.assertEqual(calculate.evaluate('mad(5,)', False, False), 'Parsing Error: Invalid input entered.')
        self.assertEqual(calculate.evaluate('mad(,5)', False, False), 'Parsing Error: Invalid input entered.')

    def test_input_error(self):
        self.assertEqual(calculate.evaluate('log(-1)', False, False), 'Input Error: Not in domain of log function.')
        self.assertEqual(calculate.evaluate('(-1)!', False, False), 'Input Error: Input to factorial must be a positive integer.')
        self.assertEqual(calculate.evaluate('(1.1)!', False, False), 'Input Error: Input to factorial must be a positive integer.')
        self.assertEqual(calculate.evaluate('0^(-1)', False, False), 'Input Error: Inverse of 0 is undefined.')
        self.assertEqual(calculate.evaluate('sqrt(-2)', False, False), 'Input Error: Not in domain of radical function.')
        self.assertEqual(calculate.evaluate('(-5)^2.1', False, False), 'Input Error: Negative base with fractional exponent.')
        self.assertEqual(calculate.evaluate('5', False, True), 'Input Error: Not in binary.')
        self.assertEqual(calculate.evaluate('1.5', False, True), 'Input Error: Not in binary.')


    def test_arithmetic_error(self):
        self.assertEqual(calculate.evaluate('1/0', False, False), 'Arithmetic Error: Division by 0 is undefined.')
        self.assertEqual(calculate.evaluate('5%0', False, False), 'Arithmetic Error: Division by 0 is undefined.')

# Allows us to run the tests immediately when this file is run
if __name__ == '__main__':
    unittest.main()
