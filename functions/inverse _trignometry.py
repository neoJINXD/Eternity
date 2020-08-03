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

def arcsin(x: float) -> float:
    """ Calculate inverse function """
    return ((generate_pi()/2 )*(1  - ((1 - x)**(1/2))) )


def arccos(x: float) -> float:
    if x<0:
        x = -1*x
        return ((generate_pi())-(arcsin(x)))
    else:
        return ((generate_pi()/2 )-(arcsin(x)))


def arctan(x: float) -> float:
    x2 = x*x
    return (arcsin(x/((x2+1)**(1/2))))