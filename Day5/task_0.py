""" yrange implementation (using yield)
    that take any param (power of number),
    the iterator should NEVER END,
    instead of raising StopIteration -
    the behavior should be to continue from starting element, i.e.
    1,2,3,4,1,2,3,4,1,2,3,4 etc.

An infinite number generator, from 0 to the maximum limit put in the function
Args:
    upper_limit (int):  The upper limit of the range to generate.
Yields:
    The next number in the range of 0 to integers + 1.
    When the maximum value is reached, the cycle is repeated from 0.
Raises:
     AttributeError.
Example:
        t = cycle_number(5)
        next(t)
        0
        next(t)
        1
        next(t)
        3
        next(t)
        4
        next(t)
        0
        next(t)
        1
"""


def cycle_number(upper_limit):
    if not isinstance(upper_limit, int):
        raise AttributeError('It is not a number!')
    if upper_limit < 0:
        for element in range(0, upper_limit, -1):
            yield element
    elif upper_limit == 0:
        while True:
            yield 0
    else:
        while True:
            for element in range(0, upper_limit):
                yield element
