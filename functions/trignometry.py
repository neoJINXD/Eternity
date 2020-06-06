import functions.exponents_and_logs as exp
import functions.exponent_helper_functions as exp_help


def generate_pi():
    # Calculate pi using Nilakantha's infinite series which converges faster than the Maclaurin series
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
    num = x
    denom = 1

    for n in range(3, 50, 2):
        num *= -x * x
        denom *= n * (n - 1)
        result += num / denom

    return result


def sinh(x):
    # Calculate hyperbolic function using value of e
    e = exp.generate_e(x)
    return (e - exp_help.take_inverse(e)) / 2


def cosh(x):
    return (exp.generate_e(x) + exp.generate_e(-x)) / 2


def tanh(x):
    return sinh(x) / cosh(x)
