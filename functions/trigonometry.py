import functions.common as common
import functions.exponents_and_logs as exp


def generate_pi(term_count: int = 150) -> float:
    """Returns an approximation of the value of PI.
    
    PI is approximated using Nilakantha's infinite series. 
    
    Args:
        term_count (int): Number of terms of Nilakantha's series used to approximate PI
 
    Returns:
        float: Approximation of the value of PI
    """
    sign = 1
    pi = 3
    for i in range(2, term_count, 2):
        pi += (sign * 4 / (i * (i + 1) * (i + 2)))
        sign *= -1
        
    return pi


def sin_taylor(angle: float, term_count: int = 150) -> float:
    """Returns an approximation of the value of sin('angle') using the Maclaurin series expansion of sin(x).
    
    This approximation is typically used for values of 'angle' close to the center of the expansion (0).
    Larger values of x require more terms to converge.
    
    Args:
        angle (float): Input to sin function
        term_count (int): Number of terms of Maclaurin series used to approximate value of sin('angle')
 
    Returns:
        float: Approximation of the value of sin('angle')
    """
    result = angle
    numerator = angle
    denominator = 1
    for i in range(3, term_count, 2):
        numerator *= -angle * angle
        denominator *= i * (i - 1)
        result += numerator / denominator

    return result


def cos_taylor(angle: float, term_count: int = 150) -> float:
    """Returns an approximation of the value of cos('angle') using the Maclaurin series expansion of cos(x).
    
    This approximation is typically used for values of 'angle' close to the center of the expansion (0).
    Larger values of x require more terms to converge.
    
    Args:
        angle (float): Input to cos function
        term_count (int): Number of terms of Maclaurin series used to approximate value of cos('angle')
 
    Returns:
        float: Approximation of the value of cos('angle')
    """
    result = 1
    numerator = 1
    denominator = 1
    for i in range(2, term_count, 2):
        numerator *= -angle * angle
        denominator *= i * (i - 1)
        result += numerator / denominator

    return result


def sin(angle: float) -> float:
    """Returns an approximation of the value of sin('angle').
    
    Args:
        angle (float): Input to sin function
 
    Returns:
        float: Approximation of the value of sin('angle')
    """
    # Leverage cyclical property of trigonometric functions to keep angle close to center of Taylor series expansion.
    return sin_taylor(angle % (2 * generate_pi()))


def cos(angle: float) -> float:
    """Returns an approximation of the value of cos('angle').
    
    Args:
        angle (float): Input to cos function
 
    Returns:
        float: Approximation of the value of cos('angle')
    """
    # Leverage cyclical property of trigonometric functions to keep angle close to center of Taylor series expansion.
    return cos_taylor(angle % (2 * generate_pi()))


def tan(angle: float) -> float:
    """Returns an approximation of the value of tan('angle').
    
    Args:
        angle (float): Input to tan function
 
    Returns:
        float: Approximation of the value of tan('angle')
    """
    # Leverage cyclical property of trigonometric functions to keep angle close to center of Taylor series expansion.
    angle %= 2 * generate_pi()
    # Taylor series expansion of tan(x) is a little bit complicated. We will use tan(x)=sin(x)/cos(x) instead.
    sin = sin_taylor(angle)
    cos = cos_taylor(angle)
    return sin/cos

def sinh(argument: float) -> float:
    """Returns an approximation of the value of sinh('argument').
    
    Args:
        argument (float): Input to hyperbolic sin function
 
    Returns:
        float: Approximation of the value of sinh('argument')
    """
    e = exp.exp(argument)
    return (e - common.inverse(e)) / 2


def cosh(argument: float) -> float:
    """Returns an approximation of the value of cosh('argument').
    
    Args:
        argument (float): Input to hyperbolic cos function
 
    Returns:
        float: Approximation of the value of cosh('argument')
    """
    e = exp.exp(argument)
    return (e + common.inverse(e)) / 2


def tanh(argument: float) -> float:
    """Returns an approximation of the value of tanh('argument').
    
    Args:
        argument (float): Input to hyperbolic tan function
 
    Returns:
        float: Approximation of the value of tanh('argument')
    """
    e = exp.exp(argument)
    return (e - common.inverse(e)) / (e + common.inverse(e))
