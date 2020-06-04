import numpy as np
from . import exceptions as exceptions
from . import exponents_and_logs as exp


def cal_mean(arg):
    total = 0
    for e in arg:
        total += e
    size = len(arg)
    result = total / size
    return result


def mad(*arg):
    values = list(arg)
    size = len(arg)
    mean = cal_mean(values)
    distance = 0
    for e in values:
        distance += (mean - e) if(mean - e > 0) else(e - mean)
    result = distance / size
    return result


def std(*arg):
    values = list(arg)
    size = len(values)
    mean = cal_mean(values)
    distance_square = 0
    for e in values:
        distance_square += (e - mean) * (e - mean)
    result = exp.calculate_exponent((distance_square/size), (1/2))
    return result

