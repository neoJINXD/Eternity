import exceptions.exceptions as exceptions
import functions.trigonometry as trig
import functions.exponents_and_logs as exponents
from decimal import *


def rad(deg: float) -> float:
    """Returns the radians corresponding to input angle.
    
    Args:
        deg (float): Angle in degree
           
    Returns:
        float: Radian of input
    """
    return float(Decimal(deg) * Decimal(trig.generate_pi()) / Decimal(180.0))
    # TO SHOW ACCURACY: return float(Decimal(deg) * Decimal(math.pi) / Decimal(180.0))


def deg(rad: float) -> float:
    """Returns the degree corresponding to input angle.
    
    Args:
       rad (float): Angle in radians
          
    Returns:
        float: Degree of input
    """
    return float(Decimal(rad) * Decimal(180.0) / Decimal(trig.generate_pi()))
    # TO SHOW ACCURACY: return float(Decimal(rad) * Decimal(180.0) / Decimal(math.pi))


def decimal_to_binary_integer(value: int) -> str:
    """Returns a string that contains the binary equivalent of a decimal integer.

    Args:
        value (int): Value in decimal
        
    Returns:
        str: Value in binary
    """
    bits = list()
    if value == 0:
        return ""
    while value != 0:
        number_to_store = value % 2
        value = value // 2
        bits.append(number_to_store)
    binary_string = ""
    for x in reversed(bits):
        binary_string = binary_string + str(x)
    return binary_string


def decimal_to_binary_fraction(value: float) -> str:
    """Returns a string that contains the binary equivalent of a decimal fraction.

    Args:
        value (float): Value in decimal
        
    Returns:
        str: Value in binary
    """
    bits = list()
    while value != 0 and (len(bits) <= 15):
        new_value = float(value * 2)
        number_to_store = int(new_value)
        value = new_value % 1
        bits.append(number_to_store)
    binary_string = "0."
    for x in bits:
        binary_string = binary_string + str(x)
    return binary_string


def decimal_to_binary(number: float) -> str:
    """Returns a string that contains the binary equivalent of a decimal number.
    
    Args:
        number (float): Value in decimal
        
    Returns:
        str: Value in binary
    """
    if number >= 0:
        binary_result = ""
    else:
        binary_result = "-"
        number *= -1
    if number % 1 == 0: # Means that there isn't a fraction
        binary_result += decimal_to_binary_integer(int(number))
    else:  # Means that it's not a whole number and integer and fraction will be calculated individually
        binary_result += decimal_to_binary_integer(int(number)) + decimal_to_binary_fraction(number % 1)[1:]
    return binary_result


def binary_to_decimal_integer(value: str) -> int:
    """Returns an integer that contains the decimal equivalent of a binary integer.

    Args:
        value (str): Value in binary
        
    Returns:
        int: Value in decimal
    """
    if not is_binary(value):
        raise exceptions.InputError(value, "Binary numbers can only contain 1s and 0s.")
        
    the_number = str(value)
    position = 0
    value = 0
    for char in reversed(the_number):
        value += int(char) * exponents.pow(2,position)
        position += 1
    return value


def binary_to_decimal_fraction(value: str) -> float:
    """Returns a float that contains the decimal equivalent of a binary fraction.

    Args:
        value (str): Value in binary
        
    Returns:
        float: Value in decimal
    """
    if not is_binary(value):
        raise exceptions.InputError(value, "Binary numbers can only contain 1s and 0s.")
        
    the_number = str(value)[2:]
    position = -1
    value = 0
    for char in the_number:
        value += int(char) * exponents.pow(2,position)
        position -= 1
    return value


def binary_to_decimal(number: str) -> float:
    """Returns a float that contains the decimal equivalent of a binary number.

     Args:
         number (str): Value in binary
         
     Returns:
         float: Value in decimal
     """
    if number[0] == '-':
        decimal_result = -1
        number = number[1:]
    else:
        decimal_result = 1
    try:
        decimal_index = number.index('.')
        decimal_result *= binary_to_decimal_integer(number[:decimal_index]) + binary_to_decimal_fraction("0" + number[decimal_index:])
    # If the number is an integer, number.index('.') will throw a ValueError.
    except ValueError:
        decimal_result *= binary_to_decimal_integer(number)
    return decimal_result
        
def is_binary(number: str) -> bool:
    """Returns true if input is a valid binary number and false otherwise.

     Args:
         number (str): Number to check
         
     Returns:
         bool: True if 'number' is a valid binary number and false otherwise.
     """
    for char in str(number):
        if not (char in "01."):
            return False
    return True
