import numpy as np

import functions.trigonometry as trig
import functions.exponents_and_logs as exponents
from decimal import *
import math


def rad(deg: float) -> float:
    """Returns the radians corresponding to input angle
       Args:
           deg (float): Angle in degree
       Returns:
           float: Radian of input
    """

    return float(Decimal(deg) * Decimal(trig.generate_pi()) / Decimal(180.0))
    # TO SHOW ACCURACY: return float(Decimal(deg) * Decimal(math.pi) / Decimal(180.0))


def deg(rad: float) -> float:
    """Returns the degree corresponding to input angle
       Args:
          rad (float): Angle in radians
       Returns:
           float: Degree of input
    """

    return float(Decimal(rad) * Decimal(180.0) / Decimal(trig.generate_pi()))
    # TO SHOW ACCURACY: return float(Decimal(rad) * Decimal(180.0) / Decimal(math.pi))


def decimal_to_binary_integer(value: int) -> str:
    """Returns a string that contains the binary result of an integer
        Args:
            value (int): Value in decimal
        Returns:
            str: Value in binary
    """
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


def decimal_to_binary_decimal(value: float) -> str:
    """Returns a string that contains the binary result of an decimal value
        Args:
            value (float): Value in decimal
        Returns:
            str: Value in binary
    """
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


def convert_to_binary(number: float) -> str:
    """Returns the the decimal equivalent of a binary number
        Args:
            number (float): Value in decimal
        Returns:
            str: Value in binary
    """
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


def convert_to_decimal(number: float) -> float:
    """Returns a float that contains the equivalent of the binary value entered
         Args:
             number (float): Value in binary
         Returns:
             float: Value in decimal
     """
    if number >= 0:
        pos_sign = True
    else:
        pos_sign = False
    if number % 1 == 0:  # Means that there isn't a fraction
        decimal_result = int_binary_to_decimal(number)
    else:  # Means that it's not a whole number and integer and fraction will be calculated individually
        string_number = str(number)
        decimal_index = string_number.index('.')
        decimal_number = float(string_number[decimal_index:])
        decimal_result = int_binary_to_decimal(int(number)) + float_binary_to_decimal(decimal_number % 1)
    if pos_sign:
        return decimal_result
    else:
        return decimal_result * -1

def int_binary_to_decimal(value: float) -> float:
    """Returns the decimal equivalent of a binary integer
        Args:
            value (float): Value in binary
        Returns:
            float: Value in decimal
    """
    the_number = str(value)
    position = 0
    value = 0
    for char in reversed(the_number):
        # print(int(char))
        value = value + (int(char) * exponents.pow(2,position))
        position = position + 1
    return value


def float_binary_to_decimal(value: float) -> float:
    """Returns a float that contains the decimal equivalent of the binary value entered
        Args:
            value (float): Value in binary
        Returns:
            float: Value in decimal
    """
    the_number = str(value)[2:]
    position = -1
    value = 0
    for char in the_number:
        value = value + (int(char) * exponents.pow(2,position))
        position = position - 1
    return value