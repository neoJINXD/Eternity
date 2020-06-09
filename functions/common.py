import exceptions.exceptions as exceptions


def factorial(num: int) -> int:
    if not isinstance(num, int):
        # Input should be an integer
        raise exceptions.InputError(num, "Error: non-integer factorial")
    elif num < 0:
        # Input should be non-negative
        raise exceptions.InputError(num, "Error: negative factorial")
    elif num == 0:
        return 1
    result = 1
    for i in range(1, num + 1):
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
