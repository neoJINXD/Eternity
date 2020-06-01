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
    older = x   # keeps track of the previous term
    sign = -1   # the sign needs to flip for every term

    for i in range(1, 50):
        n = (i * 2) + 1
        num = x * x
        denom = n * (n - 1)
        latest = older * (num / denom)
        result += sign * latest
        older = latest
        sign *= -1

    return result
