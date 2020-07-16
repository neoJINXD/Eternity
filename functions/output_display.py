import functions.trigonometry as trig


def rad(deg: float) -> float:
    """Returns the radians corresponding to input angle
       Args:
           deg (float): Angle in degree
       Returns:
           float: Radian of input
    """

    return deg * (trig.generate_pi()/ 180)


def deg(rad: float) -> float:
    """Returns the degree corresponding to input angle
       Args:
          rad (float): Angle in radians
       Returns:
           float: Degree of input
    """

    return rad * (180 / trig.generate_pi())