import functions.trigonometry as trig
from decimal import *
import math

def rad(deg: float) -> float:
    """Returns the radians corresponding to input angle
       Args:
           deg (float): Angle in degree
       Returns:
           float: Radian of input
    """

    return float(Decimal(deg) * Decimal(trig.generate_pi()) / Decimal(180.0))
     # TO SHOW ACCURACY: return float(Decimal(deg) * Decimal(math.pi) / Decimal(180.0))


def deg(rad: float) -> float:
    """Returns the degree corresponding to input angle
       Args:
          rad (float): Angle in radians
       Returns:
           float: Degree of input
    """

    return float(Decimal(rad) * Decimal(180.0) / Decimal(trig.generate_pi()))
    # TO SHOW ACCURACY: return float(Decimal(rad) * Decimal(180.0) / Decimal(math.pi))

