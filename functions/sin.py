def sin(x: float) -> float:
    '''
    Optimized version of sin using taylor expansion.
    Based on Emanuel's suggestion to avoid factorial
    and exponent calls.

    Each term is it's previous value multiplied by
    -(x*x)/(n(n-1)), where the starting point is x
    '''
    # Initial values
    result = x  # accumulator for the result

    # keeping track of the previous term
    num = x
    denom = 1

    for n in range(3, 50, 2):
        num *= -x*x
        denom *= n*(n-1)
        result += num/denom

    return result
