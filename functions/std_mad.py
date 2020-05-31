import numpy as np
import exceptions.exceptions as the_exception


def mad(*arg):
    sum = 0
    values = list(arg)
    for e in values:
        sum += e
    size = len(values)
    mean = sum / size
    distance = 0
    for e in values:
        distance += (mean - e, e - mean)[e - mean > 0]
    result = distance / size
    # print(result)
    return result


def std(*arg):
    sum = 0
    values = list(arg)
    for e in values:
        sum += e
    size = len(values)
    mean = sum / size
    distance_square = 0
    for e in values:
        distance_square += (e - mean) * (e - mean)
    result = (distance_square / size) ** (.5)
    # print(result)
    return result

