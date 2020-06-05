# This class is for all the helper functions that were used to calculate the exponent function.
import numpy as np


# This function obtain a dictionary with a number and the corresponding result of that number to the 100th root
def calculate_approx_square():
    a = np.arange(1, 1.44, 0.000001)  # Not sure if numpy can be used
    dictionary = {}
    new_list = []
    for items in a:
        new_list.append(exponentiation_by_squaring(items, 100))
    value = 0
    for i in a:
        dictionary[i] = new_list[value]
        value = value + 1
    return dictionary


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


# This function checks if an exponent is negative
def is_negative(x):
    if x >= 0:
        return False
    return True


# This function takes the inverse of a number
def take_inverse(x):
    return 1 / x


# This function is used to calculate the approximate value of a number to the 100th root
# This is used if the exponent is a fraction.
def calculate_root(b):
    a = listOfValues
    the_number = 0
    for values in a:
        temp = exponentiation_by_squaring(values, 100)
        if temp >= b:
            the_number = values
            break
    return the_number


# Static variables
listOfValues = calculate_approx_square()
