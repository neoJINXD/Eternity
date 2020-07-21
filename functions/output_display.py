import functions.trigonometry as trig
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