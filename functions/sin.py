from math import factorial


def sin(x: float) -> float:
    result = 0
    sign = 1

    for i in range(50):
        result += ((x**((i*2) + 1)) / factorial(((i*2) + 1))) * sign
        sign *= -1

    return result
    # math based on
    # https://en.wikibooks.org/wiki/Trigonometry/Power_Series_for_Cosine_and_Sine
