import numpy as np


# This is a helper function that calculates x^y when y is an integer
def calculate_exponent_int_only(x, y):
    new_value = x
    try:
        if is_exponent_negative(y):
            y = y * -1
            for value in range(1, y):
                new_value = new_value * x
            new_value = take_inverse(new_value)
        else:
            for value in range(1, y):
                new_value = new_value * x
        return new_value
    except:
        print("Values entered were not numbers, try again")


def is_exponent_negative(x):
    if x >= 0:
        return False
    return True


# This function takes the inverse of a number
def take_inverse(x):
    return 1 / x


# This is a helper function that is used to calculate the approximate value of a number to the 100th root
def calculate_root(b):
    a = calculate_approx_square()
    the_number = 0
    to_continue = True
    while to_continue:
        index = 0
        for values in a:
            the_value = a.get(values)
            temp = calculate_exponent_int_only(values, 100)
            if temp < b:
                continue
                index = index + 1
            if temp > b:
                to_continue = False
                the_number = values
                break
    return the_number


# This is a helper function to obtain a dictionary with a number and the corresponding result of that number to the
# 100th root
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
