import exceptions.exceptions as exceptions


def factorial(num):
    if not isinstance(num, int):
        raise exceptions.InputError(num, "Error: non-integer factorial")  # Input should be an integer
    elif num < 0:
        raise exceptions.InputError(num, "Error: negative factorial")  # Input should be non-negative
    elif num == 0:
        return 1
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result
