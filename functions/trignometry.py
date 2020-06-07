import functions.exponents_and_logs as exp
import functions.exponent_helper_functions as exp_help


def generate_pi() -> float:
    """
    Calculate pi using Nilakantha's infinite series which
    converges faster than the Maclaurin series
    """
    sign = 1
    pi = 3
    for num in range(2, 15000, 2):
        num1 = num + 1
        num2 = num + 2
        pi += (sign * 4 / (num * num1 * num2))
        sign *= -1
    return pi


def sin(x: float) -> float:
    """
    Optimized version of sin using taylor expansion.
    Based on Emanuel's suggestion to avoid factorial
    and exponent calls.

    Each term is it's previous value multiplied by
    -(x*x)/(n(n-1)), where the starting point is x
    """
    # Initial values
    result = x  # accumulator for the result

    # keeping track of the previous term
    numerator = x
    denominator = 1

    for n in range(3, 50, 2):
        numerator *= -x * x
        denominator *= n * (n - 1)
        result += numerator / denominator

    return result


def cos(x: float) -> float:
    """
    Following the same logic as sin
    """
    # Initial values
    result = 1  # accumulator for the result

    # keeping track of the previous term
    num = 1
    denom = 1

    for n in range(2, 50, 2):
        num *= -x * x
        denom *= n * (n - 1)
        result += num / denom

    return result


def sinh(x: float) -> float:
    """ Calculate hyperbolic function using value of e """
    e = exp.generate_e(x)
    return (e - exp_help.take_inverse(e)) / 2


def cosh(x: float) -> float:
    return (exp.generate_e(x) + exp.generate_e(-x)) / 2


def tanh(x: float) -> float:
    return sinh(x) / cosh(x)
