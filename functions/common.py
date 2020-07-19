import exceptions.exceptions as exceptions
import numpy as np


def factorial(argument: int) -> int:
    """Returns the product of all non-negative integers less than or equal to some non-negative integer.

    Args:
        argument (int): Non-negative integer used as input to factorial function

    Returns:
        int: Product of all non-negative integers less than or equal to 'argument'

    Raises:
        InputError: If 'argument' is not a non-negative integer
    """
    # Ensure that input is an integer.
    if int(argument) != argument:
        raise exceptions.InputError(argument, "Input to factorial should be a non-negative integer.")
    argument = int(argument)
    # Ensure that input is non-negative.
    if argument < 0:
        raise exceptions.InputError(argument, "Input to factorial should be a non-negative integer.")

    # Calculate factorial using repeated multiplication.
    result = 1
    for i in range(1, argument + 1):
        result *= i
    return result


def mod(dividend: float, divisor: float) -> float:
    # TODO not sure on the typing for this,
    # and should check if can be optimized
    while dividend > divisor:
        dividend -= divisor
    while dividend < divisor:
        dividend += divisor
    return dividend


def decimal_to_binary_integer(value):
    """Returns a string that contains the binary result of an integer"""
    the_array = np.array([])
    while value != 0:
        number_to_store = value % 2
        value = int(value / 2)
        the_array = np.append(the_array, number_to_store)
    binary_string = ""
    array_length = the_array.size
    for x in reversed(range(array_length)):
        binary_string = binary_string + str(int(the_array[x]))
    return binary_string


def decimal_to_binary_decimal(value):
    """Returns a string that contains the binary result of an decimal value"""
    the_array = np.array([])
    while value != 0 and (the_array.size <= 10):
        new_value = float(value * 2)
        number_to_store = int(new_value)
        value = new_value % 1
        the_array = np.append(the_array, int(number_to_store))
    binary_string = "0."
    for x in the_array:
        binary_string = binary_string + str(int(x))
    return binary_string


def convert_to_binary(number):
    """Returns the binary of a number"""
    if number >= 0:
        pos_sign = True
    else:
        pos_sign = False
    if number % 1 == 0:  # Means that there isn't a fraction
        binary_result = decimal_to_binary_integer(number)
    else:  # Means that it's not a whole number and integer and fraction will be calculated individually
        binary_result = decimal_to_binary_integer(int(number)) + decimal_to_binary_decimal(number % 1)
    if pos_sign:
        return binary_result
    else:
        return "-" + binary_result


def is_even(argument: int) -> bool:
    """Returns true is input is even and false otherwise.

    Args:
        argument (int): Value to be checked

    Returns:
        bool: True if 'argument' is even and false otherwise

    Raises:
        InputError: If 'argument' is not an integer
    """
    # Ensure that argument is an integer.
    if not isinstance(argument, int):
        raise exceptions.InputError(argument, "Parity of non-integers is undefined.")

    return not (argument & 1)


def is_odd(argument: int) -> bool:
    """Returns true is input is odd and false otherwise.

    Args:
        argument (int): Value to be checked

    Returns:
        bool: True if 'argument' is odd and false otherwise

    Raises:
        InputError: If 'argument' is not an integer
    """
    # Ensure that argument is an integer.
    if not isinstance(argument, int):
        raise exceptions.InputError(argument, "Parity of non-integers is undefined.")

    return argument & 1


def is_positive(argument: float) -> bool:
    """Returns true is input is positive and false otherwise.

    Args:
        argument (float): Value to be checked

    Returns:
        bool: True if 'argument' is positive and false otherwise
    """
    return argument > 0


def is_negative(argument: float) -> bool:
    """Returns true is input is negative and false otherwise.

    Args:
        argument (float): Value to be checked

    Returns:
        bool: True if 'argument' is negative and false otherwise
    """
    return argument < 0


def inverse(argument: float) -> float:
    """Returns inverse of input.

    Args:
        argument (float): Non-zero input to inverse function

    Returns:
        float: Inverse of 'argument'.

    Raises:
        InputError: If 'argument' is equal to 0
    """
    # Ensure that input is not equal to 0.
    if argument == 0:
        raise exceptions.InputError(argument, "Inverse of 0 is undefined.")

    # Calculate inverse of argument.
    return 1 / argument


def abs(argument: float) -> float:
    """Returns absolute value of input.

    Args:
        argument (float): Input to function

    Returns:
        float: Absolute value of 'argument'.
    """
    return -argument if argument < 0 else argument

# This was used for testing
# if __name__ == "__main__":
#     print(convert_to_binary(10.68))