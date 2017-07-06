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
        if type(n) != int or n is None:
            raise Exception("It's not a number!")
        self.i = 0
        self.n = n

    def __iter__(self):
        """ __iter__ need for iterator protocol.
            Thanks to i = 0 list is not empty(list(n) != [])
        """
        self.i = 0
        return self

    def __next__(self):
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
