import functions.common as common
import functions.exponents_and_logs as exp
from typing import List


def mean(*list: float) -> float:
    """Returns the mean value of a list of floats.
    
    Args:
        *list (float): List of elements from which the mean must be determined

    Returns:
        float: Mean value of list of elements
    """
    # Get number of list elements.
    size = len(list)
    # Get sum of list elements.
    total = 0
    for e in list:
        total += e
    
    # Get mean of list elements.
    return total / size


def mad(*list: float) -> float:
    """Returns the mean absolute deviation (MAD) of a list of floats.
    
    Args:
        *list (float): List of elements from which the mean absolute deviation must be determined

    Returns:
        float: Mean absolute deviation of list of elements
    """
    # Get mean of list elements.
    mean_value = mean(*list)
    
    # Get number of list elements.
    size = len(list)
    # Get sum of absolute deviations.
    total = 0
    for e in list:
        total += common.abs(e - mean_value)
    
    # Get mean absolute deviation of list of elements.
    return total / size


def std(*list: float) -> float:
    """Returns the standard deviation of a list of floats.
    
    Args:
        *list (float): List of elements from which the standard deviation must be determined
 
    Returns:
        float: Standard deviation of list of elements
    """
    # Get mean of list elements.
    mean_value = mean(*list)
    
    # Get number of list elements.
    size = len(list)
    # Get sum of squared deviations.
    total = 0
    for e in list:
        diff = e - mean_value
        total +=  diff * diff
    
    # Get standard deviation of list of elements.
    return exp.radical(total/size, 2)
