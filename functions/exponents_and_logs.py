import functions.common as common
import functions.exponent_helper_functions as helper_functions
import exceptions.exceptions as exceptions
import math as math


def generate_e(x=1):
    # Calculate e to the power of some input value x using the Maclaurin series expansion of e^x.
    e = 0
    for n in range(100):
        e += calculate_exponent(x, n) / common.factorial(n)
    return e


def calculate_exponent(x, y):
    # Calculate value of x to the power of y.
    # Check type of parameters
    if not isinstance(x, (int, float)) or isinstance(x, bool):
        raise exceptions.CalculationError(x + " is not a number")
    if not isinstance(y, (int, float)) or isinstance(y, bool):
        raise exceptions.CalculationError(y + " is not a number")

    # Calculate exponent
    if isinstance(y, int):
        second_calculation = helper_functions.calculate_exponent_int_only(x, y)
    else:
        first_calculation = helper_functions.calculate_root(x)
        numerator = int(y * 100)
        second_calculation = helper_functions.calculate_exponent_int_only(first_calculation, numerator)

    return second_calculation


def ln_taylor(argument, iterations=50):
    # Calculate the natural logarithm of some argument using the Maclaurin series expansion of ln(1-x) around x=0. Argument must be a real number between 0 and 2 for expansion to converge.
    # Check type of argument.
    if (not isinstance(argument, (int, float))):
        raise TypeError("Logarithm of non-numeral argument is undefined.")
    # Check for values for which the series will not converge.
    if (argument <= 0 or argument >= 2):
        raise ValueError("This expansion of the natural logarithm only converges for arguments between 0 and 2.")

    #Perform calculation.
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

    # Calculate log with arbitrary base using conversion of base property of logarithms.
    return ln(argument) / ln(base)
