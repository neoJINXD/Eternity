import math
import unittest


def ln_taylor(argument, iterations=50):
    # Calculate the natural logarithm of some argument using the Maclaurin series expansion of ln(1-x) around x=0. Argument must be a real number between 0 and 2 for expansion to converge.
    # Check type of argument.
    if (not isinstance(argument, (int, float))):
        raise TypeError("Logarithm of non-numeral argument is undefined.")
    # Check for values for which the series will not converge.
    if (argument <= 0 or argument >= 2):
        raise ValueError("This expansion of the natural logarithm only converges for arguments between 0 and 2.")

    sum = 0
    x = 1 - argument
    numerator = 1

    for denominator in range(1, iterations):
        numerator *= x
        sum -= numerator / denominator

    return sum


def ln(argument):
    # Calculate the natural logarithm of some argument. Argument must be a real number.
    # Check type of argument.
    if (not isinstance(argument, (int, float))):
        raise TypeError("Logarithm of non-numeral argument is undefined.")
    # Range check is handled by ln_taylor.

    # We use frexp to fetch mantissa and exponent of argument in a platform agnostic way.
    mantissa, exponent = math.frexp(argument)

    # It follows from the properties of logarithms that ln(m*2^p)=ln(m)+p*ln(2).
    LN_2 = 0.6931471805599453
    lnMantissa = ln_taylor(mantissa)
    return lnMantissa + exponent*LN_2


def log(argument, base=10):
    # Calculate logarithm of some argument for a given base.
    # Check type of base (we could leave this to ln but we will do it here to make message more specific).
    if (not isinstance(base, (int, float))):
        raise TypeError("Logarithm with non-numeral base is undefined.")
    # Check for base of 1
    if (base == 1):
        raise ValueError("Logarithm with base of 1 is undefined.")
    # Check range of base (we could leave this to ln but we will do it here to make message more specific).
    if (base <= 0):
        raise ValueError("Logarithm with negative base is undefined.")

    # Calcukate log with arbitrary base using conversion of base property of logarithms.
    return ln(argument) / ln(base)


class TempTest(unittest.TestCase):
    def test(self):
        self.assertAlmostEqual(log(1.5), math.log(1.5, 10))
        self.assertAlmostEqual(log(math.pi), math.log(math.pi, 10))
        self.assertAlmostEqual(log(3), math.log(3, 10))
        self.assertAlmostEqual(log(4), math.log(4, 10))
        self.assertAlmostEqual(log(1, 20), math.log(1, 10))
        self.assertAlmostEqual(log(2, math.pi), math.log(2, math.pi))
        self.assertAlmostEqual(log(3, 1.45), math.log(3, 1.45))
        self.assertAlmostEqual(log(1000000, 2), math.log(1000000, 2))


if __name__ == '__main__':
    unittest.main()
