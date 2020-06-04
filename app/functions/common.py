from . import exceptions as exceptions


def add(x, y):
    if y % 2 == 0:
        raise ValueError
    return x + y


def factorial(num):
    if not isinstance(num, int):
        raise exceptions.InputError(num, "Error: non-integer factorial")  # Input should be an integer
    elif num < 0:
        raise exceptions.InputError(num, "Error: negative factorial")  # Input should be non-negative
    elif num == 0:
        return 1
    return num * factorial(num - 1)
