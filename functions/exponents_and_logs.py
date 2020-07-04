import functions.common as common
import functions.trigonometry as trig
import exceptions.exceptions as exceptions
import math as math


def pow_int(base: float, exponent: int) -> float:
    """Returns value of 'base' to the power of 'exponent' using exponentiation by squaring where the latter is an integer.

    Args:
        base (float): Base of power to be returned
        exponent (int): Exponent of power to be returned

    Returns:
        float: Value of 'base' to the power of 'exponent'
        
    Raises:
        InputError: If 'exponent' is not an integer
    """
    # Ensure that exponent is an integer.
    if not isinstance(exponent, int):
        raise exceptions.InputError(exponent, "Exponentiation by squaring does not work with non-integer exponents.")
        
    # If exponent is negative, use the property x^y = (1/x)^-y.
    if common.is_negative(exponent):
        base = common.inverse(base)
        exponent *= -1
        
    # Iterate over bits in exponent
    result = 1
    while common.is_positive(exponent):
        # If exponent is odd, we can use the fact that x^y = x(x^2)^((n-1)/2)
        if common.is_odd(exponent):
            result *= base
            # Normally, we'd subtract 1 from y here but we don't actually need to since it will be lost in the coming bit-shift.
        # Now that y is even, we can use the fact that x^y = (x^2)^(n/2) when y is even
        base *= base
        exponent >>= 1
    return result


def radical(radicand: float, index: int, delta: float = 1E-10) -> float:
    """Returns an approximation of the real value of some radical using Newton's method for finding roots of functions if such a value exists.
    
    Value returned is positive if a positive radical exists and negative otherwise. If no real root exists, an exception is raised.

    Args:
        radicand (float): Radicand of radical to be determined
        index (int): Index of radical to be determined
        delta (float): Error tolerance

    Returns:
        float: Approximation of radical defined by arguments
        
    Raises:
        InputError: If no real root exists for provided arguments
    """
    # Ensure that real value of root exists.
    if common.is_negative(radicand) and common.is_even(index):
        raise exceptions.InputError(None, "Radical with negative radicand and even index is undefined over set of real numbers.")
        
    # Approximate radicand using Newton's method.
    approx = 1
    old_mantissa, _ = math.frexp(approx)
    while True:
        power = pow_int(approx, index)
        approx = (index - 1 + radicand / power) * (approx / index)
        
        # Return current approximation when the absolute difference is within the desired range.
        diff = abs(power - radicand)
        if diff < delta:
            return approx
            
        # Return early if approximation stops improving
        crrt_mantissa, _ = math.frexp(approx)
        diff = abs(old_mantissa - crrt_mantissa)
        # We use 1E-15 here because a double precision floating point mantissa can hold no more than 52 bits of precision.
        if diff < 1E-15:
            return approx
        old_mantissa = crrt_mantissa

def pow_e_taylor(exponent: float = 1, term_count: int = 50) -> float:
    """Returns an approximation of the value of e to the power of some real number 'exponent' using the Maclaurin series expansion of e^x.
    
    This function is typically only used with values of 'exponent' close to 0 (the center of the Maclaurin series). 
    For further values, a larger number of terms is required for convergence.
    
    Args:
        exponent (float): Exponent used in power of e being approximated
        term_count (int): Number of terms used in approximation of power of e

    Returns:
        float: Approximation of e to the power of 'exponent'
    """
    result = 1
    numerator = 1
    denominator = 1
    for i in range(1, term_count):
        numerator *= exponent
        denominator *= i
        result += numerator / denominator
        
    return result


def pow_e(exponent: float = 1) -> float:
    """Returns an approximation of the value of e to the power of some real number 'exponent'.
    
    This function combines exponentiation by squaring with the Maclaurin series expansion of e^x 
    to achieve high levels of accuracy for all reasonable values of 'exponent'.
    
    Args:
        exponent (float): Exponent used in power of e being approximated

    Returns:
        float: Approximation of e to the power of 'exponent'
    """
    # Get integer and decimal parts of exponent.
    integer_part_of_exponent = int(exponent)
    fractional_part_of_exponent = exponent - integer_part_of_exponent
    
    # Approximate power of e.
    e = pow_e_taylor(1)
    return pow_int(e, integer_part_of_exponent) * pow_e_taylor(fractional_part_of_exponent)


def pow(base: float, exponent: float, root_used: int = int(1E10)) -> float:
    """Returns an approximation of some power with base 'base' and exponent 'exponent'. 
    
    Function implementation does not accept powers with negative bases and real exponents.
    
    Args:
        base (float): Base of power being approximated
        exponent (float): Exponent of power being approximated
        root_used (float): Root used to approximate real part of exponent. Larger roots yield greater accuracy but risk overflow problems for large bases.

    Returns:
        float: Approximation of power with base 'base' and exponent 'exponent'
        
    Raises:
        InputError: If 'base' is negative and 'exponent' is not an integer.
    """
    # Get integer and decimal parts of exponent.
    integer_part_of_exponent = int(exponent)
    fractional_part_of_exponent = exponent - integer_part_of_exponent
    # Ensure that base is not negative if exponent is not a integer.
    if common.is_negative(base) and fractional_part_of_exponent != 0:
        raise exceptions.InputError(None, "Implementation of exponent function for real exponents does not support negative bases because the power function for negative bases is non-continuous over the set of real numbers.")
    
    # Calculate integer part using exponentiation by squaring
    result = pow_int(float(base), integer_part_of_exponent)
    
    # If fractional part remains, approximate it using Newton's method for the denominator and exponentiation by
    # squaring for the numerator
    if fractional_part_of_exponent != 0:
        result *= pow_int(radical(float(base), root_used), int(root_used * fractional_part_of_exponent))
    
    return result


def ln_taylor(argument: float, term_count: int = 50) -> float:
    """Returns an approximation of the value of the natural logarithm of some argument using the Maclaurin series expansion of ln(1-x).
    
    Maclaurin series used only converges when 'argument' is a real value between 0 and 2.
    
    Args:
        argument (float): Argument to natural logarithm being approximated
        term_count (int): Number of terms used in approximation of natural logarithm

    Returns:
        float: Approximation of natural logarithm of 'argument'
        
    Raises:
        InputError: If 'argument' is not within interval of convergence for Taylor series used.
    """
    # Ensure that series will converge for argument provided.
    if argument <= 0 or argument >= 2:
        raise exceptions.InputError(argument, "This expansion of natural logarithms only converges for arguments between 0 and 2.")

    # Perform calculation.
    x = 1 - argument
    result = 0
    numerator = 1
    for denominator in range(1, term_count):
        numerator *= x
        result -= numerator / denominator

    return result


def ln(argument: float) -> float:
    """Returns an approximation of the value of the natural logarithm of some argument.
    
    Args:
        argument (float): Argument to natural logarithm being approximated

    Returns:
        float: Approximation of natural logarithm of 'argument'
        
    Raises:
        InputError: If 'argument' is not within domain of natural logarithm (set of positive real numbers).
    """
    # Ensure that argument is within domain of natural logarithm.
    if not common.is_positive(argument):
        raise exceptions.InputError(argument, "The value of a logarithm is undefined for non-positive arguments.")
    
    # We use frexp to fetch mantissa and exponent of argument in a platform agnostic way.
    mantissa, exponent = math.frexp(argument)

    # It follows from the properties of logarithms that ln(m*2^p)=ln(m)+p*ln(2).
    ln_2 = 0.6931471805599453
    ln_mantissa = ln_taylor(mantissa)
    return ln_mantissa + exponent * ln_2


def log(argument: float, base: float = 10) -> float:
    """Returns an approximation of the value of some logarithm with base 'base' and argument 'argument'.
    
    Args:
        argument (float): Argument to logarithm being approximated
        base (float): Base of logarithm being approximated

    Returns:
        float: Approximation of value of logarithm of with base 'base' and argument 'argument'
        
    Raises:
        InputError: If 'argument' and/or 'base' are outside of domain of logarithm.
    """
    # Ensure that base is not equal to 1.
    if base == 1:
        raise exceptions.InputError(base, "Logarithm with base of 1 is undefined.")
    # Ensure that base is positive.
    if not common.is_positive(base):
        raise exceptions.InputError(base, "Logarithm with non-positive base is undefined.")

    # Calculate logarithm with arbitrary base using conversion of base property of logarithms.
    return ln(argument) / ln(base)


def pow_10(exponent: float) -> float:
    """Returns an approximation of the value of 10 to the power of 'exponent'.
    
    Args:
        exponent (float): Exponent used in power of 10 being approximated

    Returns:
        float: Approximation of the value of 10 to the power of 'exponent'
    """
    return pow(10, exponent)


def pow_pi(exponent: float) -> float:
    """Returns an approximation of the value of pi to the power of 'exponent'.
    
    Args:
        exponent (float): Exponent used in power of pi being approximated
 
    Returns:
        float: Approximation of the value of pi to the power of 'exponent'
    """
    return pow(trig.generate_pi(), exponent)
