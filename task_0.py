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

<<<<<<< HEAD

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
=======
# TODO: Don't use cryptic vars like i,n - especially if they're params of your init method
# give them semantic names, like upper_limit
class yrange_cycle:

    """ Iterator protocol without StopIteration/
        Args:
            n (int): parametr (power of number)
            i (int): counter
    """
    def __init__(self, n):
        """ Initilisation of class.
            __init__ get n(power of number).
            Variable n is checked
        """
        # TODO: use isinstance instead of type(x) == Y checks
        if type(n) != int or n is None:
            # TODO: use ValueError or AttributeError exceptions
            # pls read doc to understand what is different in them
            raise Exception("It's not a number!")
        self.i = 0
        self.n = n

    def __iter__(self):
        # TODO: In some cases especiall for __X__ magic methods of pythons
        # you don't need to provide docstrs as it's clear the purpose of the method
        # to dev. The same for __init__ - anyone lknows it's constructor.

        # TODO: Your docstrs are hard to read, make them nicer
        """ __iter__ need for iterator protocol.
            Thanks to i = 0 list is not empty(list(n) != [])
        """
        self.i = 0
        return self

    def __next__(self):
        # TODO: Complex code
        # Use yield here as well with range. Make smaller code.
        # Avoid to many (and nested) if/else while etc.
        """ Realization next"""
        if self.i < self.n:
            i = self.i
            self.i += 1
            return i
        else:
            """ Zero the counter instead of StopIteration"""
            self.i = 0
            if self.i < self.n:
                i = self.i
                self.i += 1
                return i

# TODO: YOu should also have a generator function implementing the same logic as above
>>>>>>> master
