import functions.common as common


def generate_e(x=1):
    e = 0
    for n in range(100):
        e += power(x, n) / common.factorial(n)
    return e


# Will replace with Tara's function which also accounts for neg/real num --Just added because I need it for my part
def power(x, n):
    result: int = 1
    for i in range(n):
        result *= x
    return result
