# This class is for all the helper functions that were used to calculate the exponent function.
import numpy as np


# This function obtain a dictionary with a number and the corresponding result of that number to the 100th root
def calculate_approx_square():
    a = np.arange(1, 1.44, 0.000001)  # Not sure if numpy can be used
    dictionary = {}
    new_list = []
    for items in a:
        new_list.append(calculate_exponent_int_only(items, 100))
    value = 0
    for i in a:
        dictionary[i] = new_list[value]
        value = value + 1
    return dictionary


# This function calculates x^y when y is an integer
def calculate_exponent_int_only(x, y):
    new_value = 1
    if is_negative(y):
        y = y * -1
        for value in range(1, y):
            new_value = new_value * x
        new_value = take_inverse(new_value)
    else:
        for value in range(y):
            new_value = new_value * x
    return new_value


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
    a = ListOfValues
    the_number = 0
    for values in a:
        temp = calculate_exponent_int_only(values, 100)
        if temp >= b:
            the_number = values
            break
    return the_number


# Static variables
ListOfValues = calculate_approx_square()
