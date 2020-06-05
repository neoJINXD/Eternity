import functions.common as common
import functions.exponent_helper_functions as helper_functions
import exceptions.exceptions as exceptions
import math as math  # used only for frexp() to get mantissa sign
import functions.trignometry as trig


def generate_e_taylor(x=1):
    # Calculate e to the power of some input value x using the Maclaurin series expansion of e^x.
    e = 1
    numerator = 1
    denominator = 1

    for n in range(1, 50):
        numerator *= x
        denominator *= n
        e += numerator / denominator
    return e


def generate_e(x=1):
    # Calculate e to the power of some input value x using both the Maclaurin series expansion of e^x and exponentiation by squaring
    e = 2.7182818284590452
    integerPartOfX = int(x)
    fractionalPartOfX = x - integerPartOfX
    return helper_functions.exponentiation_by_squaring(e, integerPartOfX) * generate_e_taylor(fractionalPartOfX)


def calculate_exponent(x, y, rootUsed=int(1E5)):
    # Calculate value of x to the power of y.
    # Check type of parameters
    if not isinstance(x, (int, float)) or isinstance(x, bool):
        raise exceptions.CalculationError(x + " is not a number")
    if not isinstance(y, (int, float)) or isinstance(y, bool):
        raise exceptions.CalculationError(y + " is not a number")

    # Calculate exponent in two parts (integer and fractional part)
    # Calculate integer part using exponentiation by squaring
    integerPartOfY = int(y)
    result = helper_functions.exponentiation_by_squaring(x, integerPartOfY)
    # If fractional part remains, approximate it using Newton's method for the denominator and exponentiation by squaring for the numerator
    fractionalPartOfY = y - integerPartOfY
    if fractionalPartOfY != 0:
        result *= helper_functions.exponentiation_by_squaring(helper_functions.nth_root(x, rootUsed), int(rootUsed * fractionalPartOfY))

    return result


def ln_taylor(argument, iterations=50):
    # Calculate the natural logarithm of some argument using the Maclaurin series expansion of ln(1-x) around x=0.
    # Argument must be a real number between 0 and 2 for expansion to converge.
    # Check type of argument.
    if not isinstance(argument, (int, float)):
        raise TypeError("Logarithm of non-numeral argument is undefined.")
    # Check for values for which the series will not converge.
    if argument <= 0 or argument >= 2:
        raise ValueError("This expansion of the natural logarithm only converges for arguments between 0 and 2.")

    # Perform calculation.
    x = 1 - argument
    sum = 0
    numerator = 1

    for denominator in range(1, iterations):
        numerator *= x
        sum -= numerator / denominator

    return sum


def ln(argument):
    # Calculate the natural logarithm of some argument. Argument must be a real number.
    # Check type of argument.
    if not isinstance(argument, (int, float)):
        raise TypeError("Logarithm of non-numeral argument is undefined.")
    # Range check is handled by ln_taylor.

    # We use frexp to fetch mantissa and exponent of argument in a platform agnostic way.
    mantissa, exponent = math.frexp(argument)

    # It follows from the properties of logarithms that ln(m*2^p)=ln(m)+p*ln(2).
    LN_2 = 0.6931471805599453
    lnMantissa = ln_taylor(mantissa)
    return lnMantissa + exponent * LN_2


def log(argument, base=10):
    # Calculate logarithm of some argument for a given base.
    # Check type of base (we could leave this to ln but we will do it here to make message more specific).
    if not isinstance(base, (int, float)):
        raise TypeError("Logarithm with non-numeral base is undefined.")
    # Check for base of 1
    if base == 1:
        raise ValueError("Logarithm with base of 1 is undefined.")
    # Check range of base (we could leave this to ln but we will do it here to make message more specific).
    if base <= 0:
        raise ValueError("Logarithm with negative base is undefined.")

    # Calculate log with arbitrary base using conversion of base property of logarithms.
    return ln(argument) / ln(base)


def power_of_ten(x):
    # Returns the result of 10^x, delegating calculations to functions.exponent_helper_functions.calculate_exponent.
    return calculate_exponent(10, x)


def power_of_pi(x):
    # Returns the result of pi^x, delegating calculations to functions.exponent_helper_functions.calculate_exponent.
    return calculate_exponent(trig.generate_pi(), x)
