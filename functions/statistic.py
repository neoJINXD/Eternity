# import numpy as np
# import exceptions.exceptions as the_exception
import functions.exponents_and_logs as exp
import functions.exponent_helper_functions as helper_functions


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
    result = helper_functions.nth_root((distance_square/size), 2)
    return result
