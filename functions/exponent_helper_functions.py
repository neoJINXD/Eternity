# This class is for all the helper functions that were used to calculate the exponent function.
import numpy as np


def exponentiation_by_squaring(x, y):
    # This function calculates x^y when y is an integer.
    result = 1
    # if y is negative, we will use the fact that x^y = (1/x)^-y
    if is_negative(y):
        x = 1 / x
        y *= -1
    # Exponentiation by squaring
    while y > 0:
        # If y is odd, we can use the fact that x^y = x(x^2)^((n-1)/2)
        if y & 1 == 1:
            result *= x
            y -= 1
        # Now that y is even, we can use the fact that x^y = (x^2)^(n/2) when y is even
        x *= x
        y >>= 1
    return result


def nth_root(x, y, d=1E-10):
    # This function approximates the nth root of x using Newton's method to the desired level of precision.
    approx = 1
    old_approx = approx
    while True:
        power = exponentiation_by_squaring(approx, y)
        approx = (y - 1 + x / power) * (approx / y)
        # Return current approximation when the absolute difference is within the desired range.
        diff = power - x if power > x else x - power
        if diff < d:
            return approx
        # Sometimes, floating point numbers are not precise enough to yield the desired level of precision. Under
        # these circumstances, we see that the approximation eventually stops improving. We need to check for that.
        diff = old_approx - approx if old_approx > approx else approx - old_approx
        if diff < 1E-15:
            return approx
        old_approx = approx


# This function checks if an exponent is negative
def is_negative(x):
    if x >= 0:
        return False
    return True


# This function takes the inverse of a number
def take_inverse(x):
    return 1 / x
