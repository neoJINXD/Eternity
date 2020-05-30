import functions.common as common
import functions.exponent_helper_functions as helper_functions
import exceptions.exceptions as exceptions


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
    if isinstance(y, int):
        second_calculation = helper_functions.calculate_exponent_int_only(x, y)
    else:
        first_calculation = helper_functions.calculate_root(x)
        numerator = int(y * 100)
        second_calculation = helper_functions.calculate_exponent_int_only(first_calculation, numerator)
    return second_calculation
