import HelperFunctions as Common
from EulerExceptions import CalculatorException


def calculate_exponent(x, y):
    if isinstance(x, str):
        raise CalculatorException(x + " is not a number")
    if isinstance(y, str):
        raise CalculatorException(y + " is not a number")
    if isinstance(y, int):
        second_calculation = Common.calculate_exponent_int_only(x, y)
    else:
        first_calculation = Common.calculate_root(x)
        numerator = int(y * 100)
        second_calculation = Common.calculate_exponent_int_only(first_calculation, numerator)
    return second_calculation


