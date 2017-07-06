"""
TODO:
    Implement state-aware integers() generator.

        def integers():
        i = 1
        while True:
            yield i
            i = i + 1

    desired outcome:

            i1 = integers()
            next(i1)
            1
            next(i1)
            2
            next(i1)
            3
            i2 = integers()
            next(i2)
            4
"""

class IntegerGenerator:
    """ Class Implement state-aware integers() generator """
    i = 0

    def integer(self):
        IntegerGenerator.i += 1
        while True:
            yield IntegerGenerator.i

    def __next__(self):
        return next(self.integer())