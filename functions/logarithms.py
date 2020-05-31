import math

import unittest

def lnTaylor(argument):
    sum = 0
    x = 1 - argument
    numerator = 1

    for i in range(1, 50):
        numerator *= x
        sum -= numerator / i

    return sum

def ln(argument):
    #Check for negative values
    if (argument <= 0):
        return math.nan

    #We use frexp to fetch mantissa and exponent of argument in a platform agnostic way.
    mantissa, exponent = math.frexp(argument)
    print("Mantissa: ", mantissa)
    print("Exponent: ",exponent)

    #It follows from the properties of logarithms that ln(m*2^p)=ln(m)+p*ln(2)
    ln2 = 0.6931471805599453
    lnm = lnTaylor(mantissa)
    return lnm + exponent*ln2

def log(argument, base = 10):
    #Check for negative values
    if (argument <= 0):
        return math.nan

    return ln(argument) / ln(base)

class TempTest(unittest.TestCase):
    def test(self):
        self.assertAlmostEqual(log(1), math.log(1, 10))
        self.assertAlmostEqual(log(2), math.log(2, 10))
        self.assertAlmostEqual(log(3), math.log(3, 10))
        self.assertAlmostEqual(log(4), math.log(4, 10))

if __name__ == '__main__':
    unittest.main()