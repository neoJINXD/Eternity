import functions.common as common
import functions.exponents_and_logs as exp


def generate_pi():
    sign = 1
    pi = 3
    for num in range(2, 15000, 2):
        num1 = num + 1
        num2 = num + 2
        pi += (sign * 4 / (num * num1 * num2))
        sign *= -1
    return pi


def cosh(x):
    return (exp.generate_e(x) + exp.generate_e(-x)) / 2


def sinh(x):
    return (exp.generate_e(x) - exp.generate_e(-x)) / 2


def tanh(x):
    return sinh(x) / cosh(x)
