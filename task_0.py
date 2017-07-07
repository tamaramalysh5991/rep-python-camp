"""
TODO:
    make yrange implementation (using class/iterator protocol)
    that take any param (power of number),
    plus the iterator should NEVER END,
    instead of raising StopIteration -
    the behavior should be to continue from starting element, i.e.
    1,2,3,4,1,2,3,4,1,2,3,4 etc.

    make the same solution using generator function.
    No use of itertools (Cycle) is allowed here.

    The class use iterator protocol.

    Example:
        t = yrange_cycle(5)
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
