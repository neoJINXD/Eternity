import functions.common as common
import functions.exponent_helper_functions as helper_functions
import exceptions.exceptions as exceptions
import functions.trignometry as trig

def generate_e(x=1):
    e = 0
    for n in range(100):
        e += calculate_exponent(x, n) / common.factorial(n)
    return e


def calculate_exponent(x, y):
    if isinstance(x, str):
        raise exceptions.CalculationError(x + " is not a number")
    if isinstance(y, str):
        raise exceptions.CalculationError(y + " is not a number")
    if isinstance(y, int):  # and not isinstance(y, bool):
        second_calculation = helper_functions.calculate_exponent_int_only(x, y)
    elif isinstance(x, (int)):  # and not isinstance(x, bool):
        first_calculation = helper_functions.calculate_root(x)
        numerator = int(y * 100)
        second_calculation = helper_functions.calculate_exponent_int_only(first_calculation, numerator)
    else:  # Error raised as this means that the value is not an integer or float
        raise exceptions.CalculationError("invalid information entered")
    return second_calculation

def power_of_ten(x):
    # returns the result of 10^x, delegating calculations to functions.exponent_helper_functions.calculate_exponent
    return calculate_exponent(10, x)

def power_of_pi(x):
     # returns the result of pi^x, delegating calculations to functions.exponent_helper_functions.calculate_exponent
    return calculate_exponent(trig.generate_pi(), x)