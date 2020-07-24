import unittest
import calculate
import math
import exceptions.exceptions as the_exception

# test class
class TestCalculate(unittest.TestCase):
    def test_evaluate(self):
        self.assertEqual(calculate.evaluate('', False), '')
        self.assertEqual(calculate.evaluate('6+6', False), 6+6)

# Allows us to run the tests immediately when this file is run
if __name__ == '__main__':
    unittest.main()
